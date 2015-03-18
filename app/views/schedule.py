#! coding: utf-8
import json

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt

from app.business.schedule.search import ScheduleSearch
from app.forms import FormTableFile
from app.models import Project, ProjectFile, TableFile, Table


@login_required
def index(request, id=None):
    print(id)

    try:
        if id:
            # Verificar se existe projeto em rascunho
            project = Project.objects.get(pk=id)
            scheduler, created = ProjectFile.objects.get_or_create(project=project, status=4)
            if created:
                order = 0

                for table in Table.objects.filter(active=True, project=project).all():
                    new = TableFile()
                    new.project_file = scheduler
                    new.order = order
                    new.quantity = 0
                    new.table = table
                    new.save()
                    order += 1

            print(created)
            return render_to_response('schedule/schedules.html', {'schedule': scheduler}, RequestContext(request))
            # return render_to_response('project/schedule.html', {'scheduler': scheduler})
        else:
            raise PermissionDenied
    except Exception as e:
        print(e)


@login_required
def search(request):
    retorno = {}

    print(request.GET)

    try:
        busca = ScheduleSearch(request.GET)
        retorno = busca.buscar()
    except Exception as e:
        print(e)

    retorno = json.dumps(retorno)
    return HttpResponse(retorno, content_type='text/json')


@csrf_exempt
@login_required
def record(request, schedule_id=None, id=None):
    if request.method == 'POST':
        return save(request.POST, id)
    else:
        retorno = {}

        schedule = ProjectFile.objects.get(pk=schedule_id)

        if id:
            table_file = TableFile.objects.get(pk=id)
            form = FormTableFile(instance=table_file)

            retorno['id'] = table_file.id
        else:
            form = FormTableFile()
            # form.fields['table'].queryset = TableFile.project_file.project.app_table_project.all()

        form.fields['table'].queryset = Table.objects.filter(project=schedule.project, active=True).all()

        retorno['form'] = form
        retorno['schedule'] = schedule_id

        return render_to_response('schedule/record.html', retorno)


def save(data, id=None):
    try:
        retorno = {}

        if id:
            form = FormTableFile(data, instance=TableFile.objects.get(pk=id))
        else:
            form = FormTableFile(data)

        if form.is_valid():
            form.save()
            retorno['success'] = True
        else:
            retorno['success'] = False
            retorno['error'] = 'ERRO'

            # for erro in
            print(form.errors)

    except Exception as erro:
        retorno['success'] = False
        retorno['error'] = erro.message

    return HttpResponse(json.dumps(retorno), content_type='text/json')


@login_required
@csrf_exempt
def delete(request, id=None):
    retorno = {}

    try:
        project = Project.objects.get(pk=id)
        project.active = False
        project.save()
        retorno['success'] = True
        retorno['message'] = 'Registro excluído com sucesso!'
    except Exception as error:
        retorno['success'] = False
        retorno['errors'] = 'Erro ao excluir registro!'

    return HttpResponse(json.dumps(retorno), content_type='text/json')


@login_required()
@csrf_exempt
def finish(request, id=None):
    retorno = {}

    if id:
        project_file = ProjectFile.objects.get(pk=id)
        project_file.status = 0
        project_file.save()
        print('salvou')
        retorno['success'] = True
    else:
        raise HttpResponseForbidden('ID NAO INFORMADO')

    return HttpResponse(json.dumps(retorno), content_type='text/json')


@login_required()
def schedule(request, id=None):
    try:
        if id:
            # Verificar se existe projeto em rascunho
            project = Project.objects.get(pk=id)
            scheduler, created = ProjectFile.objects.get_or_create(project=project, status=4)
            if created:
                for table in project.app_table_project.all():
                    new = TableFile()
                    new.project_file = scheduler
                    new.order = 0
                    new.quantity = 0
                    new.table = table
                    new.save()

            print(scheduler)

            return render_to_response('project/schedule.html', {'scheduler': scheduler})
        else:
            raise PermissionDenied
    except Exception as e:
        print(e)



