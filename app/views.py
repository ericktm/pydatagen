#! coding:utf-8
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from app.forms import ModelConection, FormTable
from app.models import Conection, Table


def index(request):
    return render_to_response('app/index.html')


@csrf_exempt
def conexao(request):
    # for i in range(100000):
    #     registro = Conection()
    #     registro.database = 'teste %d' % i
    #     registro.hostname = 'hostname %d' % i
    #     registro.username = 'usuario%d' % i
    #     registro.save()

    form = ModelConection(request.POST or None)
    if request.method == "POST" and request.is_ajax():
        print request.POST
        print form
        if form.is_valid():
            form.save()
            msg = "Registro Salvo com sucesso!"
        else:
            msg = "Erro nos dados informados. Preencha os campos corretamente!"

        return HttpResponse(msg)
    else:

        lista = Conection.objects.all()
        print len(lista)

        return render_to_response('app/conexao/index.html', {'form': form, 'lista': lista},
                                  context_instance=RequestContext(request))


def delete(request, *args):
    msg = 'teste'
    if request.is_ajax():
        post_data = request.POST

    return HttpResponse(msg)


def tabela(request, cod=None):
    lista = Table.objects.filter(database=cod).all()
    print lista

    return render_to_response('app/table/index.html', {'lista': lista}, context_instance=RequestContext(request))


def registro_tabela(request, cod=None):
    form = FormTable(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
    elif cod:
        form = form(Table.objects.get(pk=cod))

    return render_to_response('app/table/registro.html', {'form': form}, context_instance=RequestContext(request))


def execution(request):
    if request.is_ajax():
        Mapper
        map = Mapper()
    return render_to_response('app/execution/index.html', context_instance=RequestContext(request))







