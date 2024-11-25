from django.shortcuts import render, redirect
from .models import MyProject, GuestBook
from .forms import GuestBookForm 

def home(request):
    guestbook_entries = GuestBook.objects.all()
    my_projects = MyProject.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')  
        message = request.POST.get('message')

        entry = GuestBook(name=name, address=address, message=message)
        entry.save()

        return redirect('home')  
    
    return render(request, 'personal/home.html', {
        'guestbook_entries': guestbook_entries,
        'my_projects': my_projects,
    })


def about(request):
    return render(request, 'personal/about.html')


def guest_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        message = request.POST.get('message')
        
        GuestBook.objects.create(name=name, address=address, message=message)
        
        return redirect('guest_book')

    guest_book_entries = GuestBook.objects.all()
    return render(request, 'personal/guest_book.html', {'guest_book_entries': guest_book_entries})


def contact(request):
    return render(request, 'personal/contact.html')  

def my_projects(request):
    # Ambil semua data proyek
    my_projects = MyProject.objects.all()
    return render(request, 'personal/my_projects.html', {'my_projects': my_projects})
