from django.db import models

class Media(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    path = models.CharField(max_length=150)
    type = models.ForeignKey('MediaType')
    category = models.ForeignKey('MediaCategory')
    added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class MediaType(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name


class MediaCategory(models.Model):
    name = models.CharField(max_length=60)
  
    def __unicode__(self):
        return self.name

