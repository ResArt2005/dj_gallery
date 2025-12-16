from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.template import loader, Template, Context
from django.core.paginator import Paginator
from django.template.context_processors import csrf
from .models import *
#from site_settings.models import *
from telega.views import *
from telega.models import *
from django.http import JsonResponse
from django.db.models import Q

def page_404(request, exception=None):
    return redirect('/404.html')

def index(request):
    return render(request, 'index.html')