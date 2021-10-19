from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

from django.conf import settings

# from strategyprosandcons.settings import MEDIA_ROOT,MEDIA_URL


class Insight(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="insight/")
    body = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("SPC:insight_detail", kwargs={"slug": self.slug, "id": self.id})


class Team(models.Model):
    picture = models.ImageField(upload_to="team/")
    name = models.CharField(max_length=99)
    position = models.CharField(max_length=99)
    about = RichTextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
