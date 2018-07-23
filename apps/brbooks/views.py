from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

# the index function is called when root is visited
def books(request):
    recent_reviews = []
    other_reviews = []
    reviews = Review.objects.order_by('-created_at')
    if reviews.count() < 3:
        x = reviews.count()
    else:
        x = 3

    for i in range(x):
        print reviews
        recent_reviews += [reviews[i]]

    if reviews.count() > 3:
        other_reviews = reviews.filter(created_at__lt=recent_reviews[2].created_at)

    data = {
        'user': User.objects.get(id=request.session['logged_in']),
        'other_reviews': other_reviews,
        'recent_reviews': recent_reviews
    }
    return render(request, 'brbooks/books.html', data)

def add(request):
    return render(request, 'brbooks/addbook.html', {'authors': Author.objects.all()})

def add_info(request):
    if request.POST['new_author'] != '':
        this_author = Author.objects.create(writer = request.POST['new_author'])
    else:
        this_author = Author.objects.get(writer = request.POST['listed_author'])
    new_book = Book.objects.create(author=this_author, title=request.POST['title'])
    Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], book=new_book, reviewer=User.objects.get(id=request.session['logged_in']))
    return redirect('/books')

def show_book(request, id):
    return render(request, 'brbooks/showbook.html', {'book': Book.objects.get(id=id)})

def adding_review(request):
    Review.objects.create(book = Book.objects.get(id=request.POST['book']), rating=request.POST['rating'], review=request.POST['adding_review'], reviewer = User.objects.get(id=request.session['logged_in']))
    return redirect('/')

def show_profile(request, id):
    return render(request, 'brbooks/profile.html', {'user': User.objects.get(id=id)})

def logout(request):
    request.session.clear()
    return redirect('/')

def delete(request, id):
    d = Review.objects.get(id=id)
    d.delete()
    return redirect('/')
