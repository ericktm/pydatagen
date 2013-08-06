# Create your views here.
from django.http.response import HttpResponse
import datetime
from django.shortcuts import render_to_response

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render_to_response('app/index.html')
