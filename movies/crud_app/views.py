from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from . import models

class MoviesList(LoginRequiredMixin, generic.ListView):
    model = models.Movies
