from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

# Create your views here.
def index(req):
    entries = Entry.objects.all()
    return render(req, 'myapp/index.html', { 'entries': entries })