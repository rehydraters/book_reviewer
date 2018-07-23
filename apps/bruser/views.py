from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import bcrypt

# the index function is called when root is visited
def index(request):
    if 'logged_in' not in request.session:
        return render(request, 'bruser/index.html')
    else:
        return redirect('/books')

def register(request):
    errors = User.objects.basic_validator_reg(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    hash1 = bcrypt.hashpw(request.POST['pword'].encode(), bcrypt.gensalt())
    User.objects.create(name = request.POST['name'], alias = request.POST['alias'], email = request.POST['email'], password = hash1)
    user = User.objects.last()
    request.session['logged_in'] = user.id
    return redirect('/books')

def login(request):
    errors = User.objects.basic_validator_login(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['logged_in'] = user.id
    return redirect('/books')