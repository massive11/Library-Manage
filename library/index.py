#from django.http.response import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('main.html', {'title': 'This is Title', 'message': 'This is message'})