#! coding:utf-8
from django.shortcuts import render_to_response
from app.forms import ModelConection

def index(request):
    return render_to_response('app/index.html')

def conexao(request):
    
    form = ModelConection
    return render_to_response('app/conexao/index.html',{'form':form})
