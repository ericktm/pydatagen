from django.shortcuts import render_to_response
from faker.factory import Factory


def index(request):
    retorno = {}

    factory = Factory.create()

    retorno['nome'] = factory.name()
    return render_to_response('generate/index.html', {retorno})