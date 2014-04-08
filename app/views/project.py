#! coding: utf-8
import json
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from app.business.project.search import ProjectSearch
from app.forms import FormProject
from app.models import Project


def index(request):
    return render_to_response('project/index.html', RequestContext(request))


def search(request):
    retorno = {}

    try:
        busca = ProjectSearch(request.GET)
        retorno = busca.buscar()
    except Exception, e:
        print(e)

    retorno = json.dumps(retorno)
    return HttpResponse(retorno, content_type='text/json')


@csrf_exempt
def record(request, id=None):
    if request.method == 'POST':
        return save(request.POST, id)
    else:
        retorno = {}
        if id:
            form = FormProject(instance=Project.objects.get(pk=id))
            retorno['id'] = id
        else:
            form = FormProject()
        retorno['form'] = form
        return render_to_response('project/record.html', retorno)


def save(data, id=None):
    try:
        retorno = {}

        if id:
            form = FormProject(data, instance=Project.objects.get(pk=id))
        else:
            form = FormProject(data)

        if form.is_valid():
            form.save()
            retorno['success'] = True
        else:
            retorno['success'] = False
            retorno['error'] = 'ERRO'
    except Exception as erro:
        retorno['success'] = False
        retorno['error'] = erro.message

    return HttpResponse(json.dumps(retorno), content_type='text/json')


@csrf_exempt
def delete(request, id=None):
    retorno = {}

    try:
        project = Project.objects.get(pk=id)
        project.active = False
        project.save()
        retorno['success'] = True
    except Exception as error:
        retorno['success'] = False
        retorno['errors'] = 'Erro ao excluir registro!'

    return HttpResponse(json.dumps(retorno), content_type='text/json')

