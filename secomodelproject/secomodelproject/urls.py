"""secomodelproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name = "home"),
    path('blog/<int:blog_id>', blog.views.detail, name="detail"),
    #url을 int:blog_id(path_converter)로 설계할 건데, detail이라는 함수에는 
    #blog_id라는 인자를 넘겨준다.
    path('blog/new/', blog.views.new, name="new"),
    path('blog/create/', blog.views.create, name='create'),
    path('blog/main/', blog.views.main, name="main"),
    path('blog/port/', blog.views.port, name="port"),
    path('blog/blog/', blog.views.blog, name="blog"),
    path('blog/newblog/', blog.views.blogpost, name="newblog"),    
    path('accounts/', include('accounts.urls')),
    #3. newblog를 주소에 쳤을 때 가게 되는 경로
]
