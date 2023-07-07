from PIL import Image
from django.db import models
from users.models import CustomUser


class Account(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default='avatar.jpg',
        upload_to='account_images'
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)