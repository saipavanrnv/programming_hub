from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .forms import *
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib import messages
import os
from django.http import HttpResponse
# Create your views here.

class HomepageView(TemplateView): #pylint: disable = no-member
    """
    template for home page
    """
    def instructor_home(request):
        return render(request,'home.html')
    def user_home(request):
        return render(request, 'user_home.html')

class Authentication(TemplateView):
    """
    For Authentication of user
    """
    def login_request(request): #pylint: disable = no-self-argument
        """
        for checking username and password for login
        """
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                group = request.user.groups.values_list('name', flat=True).first()
                if group == 'Java_Instructor' or group == 'Python_Instructor':
                    return redirect('instructor_home')
                else:
                    return redirect('user_home')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'login.html', context)

    def logout_request(request): #pylint: disable = no-self-argument
        """
        logout
        """
        logout(request)
        return redirect('login')

    def register_request(request): #pylint: disable = no-self-argument
        """
        For registering user
        """
        form = NewUserForm()
        if request.method == 'POST':
            form = NewUserForm(request.POST)
            group = request.POST.get('group')
            if form.is_valid():
                user = form.save()
                group = form.cleaned_data['group']
                group = Group.objects.get(name=group)
                user.groups.add(group)
                return redirect('login')
        context = {'form':form}
        return render(request, 'register.html', context)

class ViewFiles(TemplateView):
    def view(request):
        user = auth.get_user(request)
        group = request.user.groups.values_list('name', flat=True).first()
        path = '/home/kiran/Desktop/programming_hub/'+group +'/'  # insert the path to your directory
        file_list = os.listdir(path)
        return render(request, 'view_files.html', {'files': file_list})

    def download_pdf(request,file):
        user = auth.get_user(request)
        group = request.user.groups.values_list('name', flat=True).first()
        path = '/home/kiran/programming_hub/'+group +'/'
        file_path = os.path.join(path, file)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/pdf")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
