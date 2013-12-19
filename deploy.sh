#!/bin/bash

set -e
LOGFILE=pydatagen/static/app.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3

# user/group to run as
USER=erick
GROUP=erick
cd /home/erick/projects/pydatagen
source ./bin/activate

cd app/pydatagen

test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn_django -w $NUM_WORKERS
    --log-level=debug
    --log-file=$LOGFILE 2>>$LOGFILE