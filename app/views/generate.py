import random

from django.shortcuts import render_to_response
import exrex
from faker.factory import Factory


def index(request):
    retorno = []

    factory = Factory.create()

    for i in range(100000):
        record = {}
        record['nome'] = factory.name()
        record['telefone'] = exrex.getone('(\d{2}) \d{4}-\d{4}')
        record['cep'] = exrex.getone('\d{5}-\d{3}')
        record['numero'] = exrex.getone('\d{%d}' % random.randint(1, 8))
        record['nascimento'] = exrex.getone('(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d')
        retorno.append(record)
    return render_to_response('generate/index.html', {'retorno': retorno})