#! coding:utf-8
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from app.forms import FormProject, FormTable
from app.models import Project, Table


def index(request):
    return render_to_response('app/index.html', RequestContext(request))


def projects(request):
    record_list = Project.objects.all()
    return render_to_response('app/project/index.html', {'record_list': record_list}, RequestContext(request))


def tables(request, id=None):
    project_record = Project.objects.get(pk=id)
    record_list = Table.objects.all().filter(project=id).order_by('order')
    return render_to_response('app/table/index.html', {'record_list': record_list, 'project': project_record},
                              RequestContext(request))


def table(request, project_id, id=None):
    project_record = Project.objects.get(pk=project_id)
    if request.method == 'POST':
        form = FormTable(request.POST, instance=Table.objects.get(pk=id)) if id else FormTable(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.project = project_record
            record.save()
            return HttpResponseRedirect('/tables/%s' % project_id, RequestContext(request))
        else:
            return render_to_response('record.html', {'form': form}, RequestContext(request))
    else:
        form = FormTable(instance=Table.objects.get(pk=id)) if id else FormTable()

        return render_to_response('record.html', {'form': form}, RequestContext(request))


def project(request, id=None):
    if request.method == 'POST':
        form = FormProject(request.POST, instance=Project.objects.get(pk=id)) if id else FormProject(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/project', RequestContext(request))
        else:
            return render_to_response('record.html', {'form': form}, RequestContext(request))
    else:
        form = FormProject(instance=Project.objects.get(pk=id)) if id else FormProject()

        return render_to_response('record.html', {'form': form}, RequestContext(request))