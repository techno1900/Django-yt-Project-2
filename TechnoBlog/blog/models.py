from django.db import models
import uuid

class blogTable(models.Model):
    name = models.CharField(max_length=200)
    discription = models.TextField(null = True, blank=True)
    image = models.ImageField(default='Screenshot (3).png', null=True, blank=True)
    image1 = models.ImageField(default='Screenshot (3).png', null=True, blank=True)
    image2 = models.ImageField(default='Screenshot (3).png', null=True, blank=True)
    id = models.UUIDField(default =uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self):
        return self.name

class contactUsersTable(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(null = False, blank=False)
    phone = models.CharField(max_length=10)
    comment = models.TextField(null= True, blank=True)
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True , editable=False)
    def __str__(self):
        return self.fname


# Create your models here.
