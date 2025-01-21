from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Page

# Create your views here.


def user_view(request):
    pages = Page.objects.all()
    return render(request, './user/user.html', {'pages': pages})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('manage')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('user')

@login_required
def manage_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        link = request.POST.get('link')
        Page.objects.create(title=title, link=link)
        return redirect('manage')
    pages = Page.objects.all()
    return render(request, './manage/manage.html', {'pages': pages})


def edit_view(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        link = request.POST.get('link')
        page.title = title
        page.link = link
        page.save()
        return redirect('manage')
    return render(request, './manage/edit.html', {'page': page})


@login_required
def delete_view(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    page.delete()
    return redirect('manage')
