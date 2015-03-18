#!coding: utf-8
import json

from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def do_login(request, *args, **kwargs):
    data_return = {}
    print("Autenticando")

    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                data_return['status'] = 'success'
        else:
            data_return['status'] = 'error'
            data_return['message'] = 'Usuário ou senha inválidoss'

    except Exception as e:
        print(e)

    return HttpResponse(json.dumps(data_return), content_type='text/json')
