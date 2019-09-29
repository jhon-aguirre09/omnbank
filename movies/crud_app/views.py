from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from . import models

class MoviesList(LoginRequiredMixin, generic.ListView):
    model = models.Movies

class CreateMovie(LoginRequiredMixin, generic.CreateView):
    redirect_field_name = 'crud_app/movie_detail.html'
    fields = ('name','description')
    model = models.Movies

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class MovieDetail(generic.DetailView):
    model = models.Movies
