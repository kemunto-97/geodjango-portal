from django.db import models

# Create your models here.

# Create an Incidence model
class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = ("Incidences")
