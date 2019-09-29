from django.urls import re_path, path, include
from . import views

app_name = 'crup_app'

urlpatterns = [
    path('',views.MoviesList.as_view(),name='all'),
    path('new/', views.CreateMovie.as_view(),name='create'),
    re_path(r'^movie/(?P<pk>\d+)/$', views.MovieDetail.as_view(), name='detail'),
]
