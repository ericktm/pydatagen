#! coding: utf-8
import json
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def index(request):
    return render_to_response('project/index.html', RequestContext(request))


def search(request):
    retorno = {}

    try:
        pass
    except Exception, e:
        print(e)

    retorno = json.dumps(retorno)
    return HttpResponse(retorno, mimetype='text/json')
