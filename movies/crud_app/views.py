from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db import IntegrityError

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

class AddRecommend(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('crud_app:detail', kwargs={'pk':self.kwargs.get('pk')})

    def get(self,request,*args,**kwargs):

        movie = get_object_or_404(models.Movies, pk=self.kwargs.get('pk'))

        try:
            models.RecommendationUser.objects.create(user=self.request.user,movie=movie)
        except IntegrityError:
            messages.warning(self.request, 'Warning already recommend!')
        else:
            messages.success(self.request,'You now recommend the movie!')

        return super().get(request,*args,**kwargs)

################################################################################

def searching(request):

    q = request.GET.get('q', '')

    querys = (Q(name__icontains=q))

    movies_s = models.Movies.objects.filter(querys)

    return render(request, 'search.html', {'movies_s': movies_s})
