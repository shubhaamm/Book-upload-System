from django.shortcuts import render , redirect
from .models import Class_name
from .forms import BookForm
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.db.models import Q


# Create your views here.

def shubh(request):
    value = Class_name.objects.all()
    if 'query' in request.GET :
        value = Class_name.objects.filter(
            Q(first_name__icontains=request.GET['query']) |
            Q(last_name__icontains=request.GET['query'])  |
            Q(contact__icontains=request.GET['query'])    |
            Q(email__icontains=request.GET['query'])
        )
    return render(request, 'abcd.html' ,  {'name11' : value } )

def shiv(request):
  count = User.objects.count()
  return render(request, 'shiv.html' , { 'count' : count })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('shubh')
    else :
        form = UserCreationForm()
        return render(request, 'signup.html',{ 'form':form })

@login_required
def secret_page(request):
    return render(request, 'secret_page.html')

class SecretPage(LoginRequiredMixin , TemplateView):
      template_name = 'secret_page.html'

def upload(request):
  context ={}
  if request.method == 'POST':
      uploaded_file = request.FILES['document']
      fs = FileSystemStorage()
      name = fs.save(uploaded_file.name , uploaded_file)
      url  = fs.url(name)
      context['url'] = fs.url(name)
  return render(request, 'upload.html', context)



@login_required
def book_list(request):
  books = Book.objects.all()
  return render(request, 'book_list.html', { 'books': books})

@login_required     
def upload_book(request):
  if request.method == 'POST':
    form = BookForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('book_list')
  else:
    form = BookForm()
  return render(request, 'upload_book.html', { 'form' : form })

 


