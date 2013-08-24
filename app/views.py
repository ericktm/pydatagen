#! coding:utf-8
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from app.forms import ModelConection, FormTable
from app.mapper import Mapper
from app.models import Conection, Table


def index(request):
    return render_to_response('app/index.html')


@csrf_exempt
def conexao(request):
    form = ModelConection(request.POST or None)
    if request.method == "POST" and request.is_ajax():
        print request.POST
        print form
        if form.is_valid():
            form.save()
            msg="Registro Salvo com sucesso!"
        else:
            msg="Erro nos dados informados. Preencha os campos corretamente!"

        return HttpResponse(msg)
    else:

        lista = Conection.objects.all()

        return render_to_response('app/conexao/index.html',{'form':form,'lista':lista})

def tabela(request):
    con = Conection.objects.get(pk=1)
    Mapper(con)
    form = FormTable(request.POST or None)
    if request.method == "POST" and request.is_ajax():
        print request.POST
        if form.is_valid():
            form.save()
            msg="Registro Salvo com sucesso!"
        else:
            msg="Erro nos dados informados. Preencha os campos corretamente!"

        return HttpResponse(msg)
    elif request.is_ajax():
         return HttpResponse("teste de msg")
    else:
        lista = Table.objects.all()
        return render_to_response('app/table/index.html',{'form':form,'lista':lista})

def registro_tabela(request,cod=None):

    form = FormTable(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
    elif cod:
        form = form(Table.objects.get(pk=cod))

    return render_to_response('app/table/registro.html',{'form':form})






