#! coding: utf-8
import json
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from app.business.project.search import ProjectSearch
from app.forms import FormProject


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
    return HttpResponse(retorno, mimetype='text/json')


def record(request, id=None):
    form = FormProject()

    return render_to_response('project/record.html', {'form': form})
