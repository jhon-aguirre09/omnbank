from django.urls import path, include
from . import views

app_name = 'crup_app'

urlpatterns = [
    path('',views.MoviesList.as_view(),name='all'),
]
