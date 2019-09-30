from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from django.contrib.auth import get_user_model
User = get_user_model()

class Movies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=80)
    slug = models.SlugField(allow_unicode=True,unique=True)
    gener = models.TextField(max_length=80, default='drama')
    director = models.TextField(max_length=80,default='Null')
    description = models.TextField()
    recommendations = models.ManyToManyField(User, related_name='recommendations_for_user', through='RecommendationUser')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('crud_app:detail',kwargs={'pk':self.pk})

    class Meta:
        ordering = ['name']

class RecommendationUser(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('movie','user')
