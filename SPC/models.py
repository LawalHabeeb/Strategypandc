from django.db import models
from django.urls import reverse
from strategyprosandcons.settings import MEDIA_ROOT,MEDIA_URL


class Insight(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField()
    image = models.ImageField(upload_to ='insight/')
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def get_absolute_url(self):
        return reverse("insight_detail", kwargs={"slug": self.slug})
    


class Team(models.Model):
    picture = models.ImageField(upload_to ='team/')
    name = models.CharField(max_length=99)
    position = models.CharField(max_length=99)
    about = models.TextField()

    
