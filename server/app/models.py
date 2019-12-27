from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    handle_name = models.CharField(max_length=20, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    icon = models.ImageField(upload_to='profile_image', blank=True)
    comment = models.CharField(max_length=30, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.handle_name

class Store(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Good(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)