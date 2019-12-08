from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=30)
    body = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Good(models.Model):
    from_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    to_store = models.ForeignKey('Store', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)