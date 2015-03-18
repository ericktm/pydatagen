import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from app.business.field.search import FieldSearch
from app.forms import FormField
from app.models import Field, Table


@login_required
def index(request, table=None):
    return_data = {'table': table}

    return render_to_response('field/index.html', return_data)


@csrf_exempt
@login_required
def search(request):
    return_data = {}
    try:
        busca = FieldSearch(request.GET)
        return_data = busca.search()
    except Exception as e:
        print(e)

    return_data = json.dumps(return_data)
    return HttpResponse(return_data, content_type='text/json')


@login_required
@csrf_exempt
def record(request, id=None, table_id=None):
    if request.method == 'POST':
        return save(request.POST, id)
    else:
        return_data = {}
        if id:
            form = FormField(instance=Field.objects.get(pk=id))
            return_data['id'] = id
        else:
            form = FormField()

        form.fields['table'].initial = Table.objects.get(pk=table_id)

        return_data['form'] = form
        return_data['table_id'] = table_id
        return render_to_response('field/record.html', return_data)


def save(data, id=None):
    try:
        return_data = {}

        if id:
            form = FormField(data, instance=Field.objects.get(pk=id))
        else:
            form = FormField(data)

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


@login_required
@csrf_exempt
def delete(request, id=None):
    retorno = {}

    try:
        table = Field.objects.get(pk=id)
        table.active = False
        table.save()
        retorno['success'] = True
    except Exception as error:
        retorno['success'] = False
        retorno['errors'] = 'Erro ao excluir registro!'

    return HttpResponse(json.dumps(retorno), content_type='text/json')