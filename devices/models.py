from django.db import models
import uuid
from django_extensions.db.fields import AutoSlugField

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.id}"
