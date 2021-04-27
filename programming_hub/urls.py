"""programming_hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include #pylint: disable = unused-import
from coding_hub.views import * #pylint: disable = unused-wildcard-import,wildcard-import
from django.contrib import admin
urlpatterns = [
    path('instructor_home/', HomepageView.instructor_home, name='instructor_home'),
    path('user_home/', HomepageView.user_home, name = 'user_home'),
    path('admin/', admin.site.urls),
    path('',Authentication.login_request,name = 'login'),
    path('logout/',Authentication.logout_request,name='logout'),
    path('register/',Authentication.register_request,name = 'register'),
    path('view_files', ViewFiles.view, name = 'view_files'),
    path('download_pdf/<str:file>/', ViewFiles.download_pdf, name='download_pdf'),


]
