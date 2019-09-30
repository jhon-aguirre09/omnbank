from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q

from django.contrib.auth.decorators import login_required

from . import models

class MoviesList(LoginRequiredMixin, generic.ListView):
    model = models.Movies

class CreateMovie(LoginRequiredMixin, generic.CreateView):
    redirect_field_name = 'crud_app/movie_detail.html'
    fields = ('name','description','gener','director')
    model = models.Movies

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class MovieDetail(generic.DetailView):
    model = models.Movies

class DeleteClient(LoginRequiredMixin,generic.DeleteView):
    model = models.Movies
    success_url = reverse_lazy('crud_app:all')

class ClientUpdate(LoginRequiredMixin, generic.UpdateView):
    redirect_field_name = 'crud_app/movie_detail.html'
    model = models.Movies
    fields = ['name','description','gener','director']
    template_name_suffix = '_update_form'

################################################################################

def searching(request):

    q = request.GET.get('q', '')

    querys = (Q(name__icontains=q))

    movies_s = models.Movies.objects.filter(querys)

    return render(request, 'search.html', {'movies_s': movies_s})
