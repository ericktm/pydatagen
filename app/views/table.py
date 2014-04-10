#! coding: utf-8
from django.shortcuts import render_to_response


def index(request, project=None):
    retorno = {'project': project}

    return render_to_response('table/index.html', retorno)