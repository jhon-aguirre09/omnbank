"""movies URL Configuration

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
from. import views
from crud_app.models import Movies
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class MoviesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movies
        fields = ['name', 'director', 'gener']

class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

router = routers.DefaultRouter()
router.register(r'movies', MoviesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('test/',views.TestPage.as_view(), name='test'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),
    path('movies/', include('crud_app.urls',namespace='crud_app')),
    re_path(r'^api-auth/', include('rest_framework.urls')),
]
