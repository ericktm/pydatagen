#! coding: utf-8
import json

from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from app.business.table.search import TableSearch
from app.forms import FormTable
from app.models import Table, Project


def index(request, project=None):
    return_data = {'project': project}

    return render_to_response('table/index.html', return_data)


def search(request):
    return_data = {}
    try:
        busca = TableSearch(request.GET)
        return_data = busca.search()
    except Exception, e:
        print(e)

    return_data = json.dumps(return_data)
    return HttpResponse(return_data, content_type='text/json')


@csrf_exempt
def record(request, id=None, project_id=None):
    print(project_id)

    if request.method == 'POST':
        return save(request.POST, id)
    else:
        return_data = {}
        if id:
            form = FormTable(instance=Table.objects.get(pk=id))
            return_data['id'] = id
        else:
            form = FormTable()

        form.fields['project'] = Project.objects.get(pk=project_id)
        print(form)
        return_data['form'] = form
        return_data['project_id'] = project_id
        return render_to_response('table/record.html', return_data)


def save(data, id=None):
    try:
        return_data = {}

        if id:
            form = FormTable(data, instance=Table.objects.get(pk=id))
        else:
            form = FormTable(data)

        if form.is_valid():
            form.save()
            return_data['success'] = True
        else:
            return_data['success'] = False
            return_data['error'] = 'ERRO'
            print(form.errors)
    except Exception as erro:
        return_data['success'] = False
        return_data['error'] = erro.message

    return HttpResponse(json.dumps(return_data), content_type='text/json')