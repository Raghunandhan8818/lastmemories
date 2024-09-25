from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    fullname = models.TextField(max_length=500, blank=True)
    mobile_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.username = self.email
        super(User, self).save(*args, **kwargs)

class Plan(models.Model):
    name = models.TextField()
    cost = models.PositiveIntegerField()
    storage = models.PositiveIntegerField()
    details = models.TextField()

    def __str__(self):
        return self.name

class MemorialProfile(models.Model):
    title = models.CharField(max_length=200,blank=True)
    about = models.TextField()
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="associated_memorial")
    current_storage = models.PositiveIntegerField()
    current_plan = models.ForeignKey(Plan,on_delete=models.DO_NOTHING,related_name="associated_plan")

    def __str__(self):
        return self.title

class ProfilePermission(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="associated_user")
    permission = models.CharField(max_length=20,default="view")
    memorial_profile = models.ForeignKey(MemorialProfile, on_delete=models.DO_NOTHING, related_name="associated_memorial_profile")

    def __str__(self):
            return self.user



#MemorialProfile  -> owner (User) , title, about  , users(can_edit, can_view) ,current_storage , current_plan

#media - > file , associated_memorial, size

#Plan -> name , details , cost, storage

#Transaction -> yet to be decided