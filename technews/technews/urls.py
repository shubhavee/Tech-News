"""technews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from django.conf.urls import include, url
from django.conf import settings

from core import views as cviews
from story import views as sviews

# from apps.core.views import signup

urlpatterns = [

    # path('signup/', signup, name='signup'),
    path('admin/', admin.site.urls),

    path('core/',include('core.urls')),
    path('story/',include('story.urls')),
    path('userprofile/',include('userprofile.urls')),

    # path('', cviews.index, name='index'),
    path('', sviews.frontpage, name='frontpage'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    # path('signup/', cviews.signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
