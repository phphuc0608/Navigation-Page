from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Page

# Create your views here.
def user_view(request):
    pages = Page.objects.all()
    return render(request, './user/user.html',{'pages': pages})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')       
@login_required
def manage_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        link = request.POST.get('link')
        Page.objects.create(title=title, link=link)
        return redirect('manage')
    pages=Page.objects.all()
    return render(request, './manage/manage.html', {'pages': pages})