#!/bin/bash
#
#set -e
#LOGFILE=pydatagen/static/app.log
#LOGDIR=$(dirname ${LOGFILE})
#NUM_WORKERS=5
#
## user/group to run as
#USER=erick
#GROUP=erick
#cd /home/erick/projects/pydatagen
#source ./bin/activate
#
#cd app/pydatagen
#
#test -d ${LOGDIR} || mkdir -p ${LOGDIR}
#exec gunicorn_django -w ${NUM_WORKERS}
#    --log-level=debug
#    --log-file=${LOGFILE} 2>>${LOGFILE}

NAME="pydatagen_app" # Name of the application
ENV_DIR=/home/erick/projects/pydatagen
DJANGODIR=${ENV_DIR}/app # Django project directory
SOCKFILE=$ENV_DIR/run/gunicorn.sock #we will communicte using this unix socket
USER=erick # the user to run as
GROUP=erick # the group to run as
NUM_WORKERS=5 # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=pydatagen.settings # which settings file should Django use
DJANGO_WSGI_MODULE=pydatagen.wsgi # WSGI module name

echo "Starting Application $NAME as `whoami`"

# Activate the virtual environment
cd ${DJANGODIR}
source ../bin/activate
export DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}
export PYTHONPATH=${DJANGODIR}:${PYTHONPATH}

## Copy Static files
./manage.py collectstatic --noinput

## Migrate Database
./manage.py migrate

# Remove python compiled files
find . -name '*.pyc' |xargs rm -f

# Create the run directory if it doesn't exist
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--name ${NAME} \
--workers ${NUM_WORKERS} \
--user=${USER} --group=${GROUP} \
--log-level=debug \
--bind=unix:${SOCKFILE}