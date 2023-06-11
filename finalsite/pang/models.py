from django.db import models

# Create your models here.
class MindMap(models.Model):
    big_label       = models.CharField(max_length=200)
    small_label     = models.CharField(max_length=200)
    contents        = models.CharField(max_length=200)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contents
