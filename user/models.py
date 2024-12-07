from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default="profile_pics/default_profile_pic.jpg", upload_to='profile_pics/')
    bio = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
    