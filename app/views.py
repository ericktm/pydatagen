#! coding:utf-8
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('app/index.html')

def conexao(request):
    
    return render_to_response('app/conexao/index.html')
