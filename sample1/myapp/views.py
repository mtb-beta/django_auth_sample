from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index_view(request):
    return HttpResponse('hello world')

@login_required
def auth_view(request):
    return HttpResponse('<h1>hello auth world</h1> <a href="/logout/">logout</a>')
