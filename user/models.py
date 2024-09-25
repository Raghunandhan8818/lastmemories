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



# MemorialProfile  -> owner (User) , title, about  , users(can_edit, can_view) ,current_storage , current_plan

#media - > file , associated_memorial, size

#Plan -> name , details , cost, storage

#Transaction -> yet to be decided