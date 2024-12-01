# from django.db import models
# from django.contrib.auth.models import User
# from PIL import Image


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    
#     def __str__(self):
#         return f'{self.user.username} Profile'
    
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         img = Image.open(self.image.path)
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
import random

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Updated this field
    otp = models.CharField(max_length=6, null=True, blank=True)  # Added this field
    otp_generated_at = models.DateTimeField(null=True, blank=True)  # Added this field
    is_verified = models.BooleanField(default=False)  # Added this field
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
    def generate_otp(self):
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        self.otp = otp
        self.otp_generated_at = timezone.now()
        self.save()
        print(f"Generated OTP: {otp}")  # Add this line to log the OTP
        return otp