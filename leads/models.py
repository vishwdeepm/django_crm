from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


#from django.contrib.auth import get_user_model #use user model provided by django
# User = get_user_model()
#for simplicity & large project it is recommended to create custom User Model


#Custom user Model
class User(AbstractUser):
    #add exra filed to existing abstract user
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    #Allowing agents to managed leads (use "" to tell ddjango in this file)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL) #CASCADE = if agent is deleted delete thid lead
    category = models.ForeignKey("Category", related_name = "leads", null=True, blank=True, on_delete=models.SET_NULL)
    date_added = models.DateTimeField(auto_now_add=True)
    SOURCE_CHOICES=(
        ('yt', 'YouTube'),
        ('google', 'Google'),
        ('fb', 'Facebook'),
        ('insta', 'Instagram'),
        ('newsL', 'Newsletter'),
    )
    phone_number = models.CharField(max_length=20)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=50)
    description = models.TextField()
    email = models.EmailField()
    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #every agent is one user
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    #if lead = models.ForeignKey("Lead", on_delete=models.CASCADE),  this means agent can have only one lead, but
    # Single agent can have multiple leads so ForeignKey is placed in a Lead Class

    def __str__(self):
        return self.user.username



class Category(models.Model):
    name = models.CharField(max_length=30)
    organisation = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)