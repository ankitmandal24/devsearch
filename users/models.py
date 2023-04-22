from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch  import receiver
# Create your models here.

class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True,null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    short_intro = models.CharField(max_length=255, blank=True,null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True,upload_to='profiles/', default ="profiles/dp.png"  )
    github = models.CharField(max_length=255, blank=True, null=True)
    stackoverflow = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

# def createProfile(sender,instance,created, **kwargs):
#     # print("trigered")
#     if created:
#         user= instance
#         profile = Profile.objects.create(
#             user=user,
#             username=user.username,
#             email=user.email,
#             name=user.first_name,
#         )
#
# def deleteUser(sender,instance, **kwargs):
#     user= instance.user
#     user.delete()
#
# post_save.connect(createProfile, sender=User)
# post_delete.connect(deleteUser, sender=Profile)
