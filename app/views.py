#! coding:utf-8
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from app.forms import ModelConection
from app.models import Conection


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





