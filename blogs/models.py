from django.db import models
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.pk}- {self.title[:20]}"
    
    def get_absolute_url(self):
        # return reverse("detail", args=[self.pk])
        return reverse("detail", kwargs={"pk": self.pk})
    