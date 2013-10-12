#! coding:utf-8
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render_to_response('app/index.html', RequestContext(request))







