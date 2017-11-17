from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import date


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Tomato(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    duration = models.DurationField()
    task = models.CharField(max_length=50)
    day = models.DateField()


class Deadline(models.Model):
    title = models.CharField(max_length=50)
    due = models.DateField()

    def days_left(self):
        delta = self.due - date.today()
        return delta.days
