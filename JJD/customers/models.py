from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('name', 'admin')
        extra_fields.setdefault('phone', '1234567890')
        extra_fields.setdefault('village', 'village')
        extra_fields.setdefault('district', 'district')
        extra_fields.setdefault('state', 'state')
        extra_fields.setdefault('country', 'country')
        extra_fields.setdefault('pincode', 123456)

        return self.create_user(email, password, **extra_fields)

class Customer(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    village = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    pincode = models.IntegerField()
    role = models.CharField(max_length=6, choices=ROLE_CHOICES, default='buyer')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField()
    quantity = models.FloatField()
    
    def __str__(self):
        return self.name
    

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product.name
















# from django.db import models

# class Customer(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     phone = models.CharField(max_length=10)
#     email = models.EmailField(max_length=200)
#     village = models.CharField(max_length=200)
#     district = models.CharField(max_length=200)
#     state = models.CharField(max_length=200)
#     country = models.CharField(max_length=200)
#     pincode = models.IntegerField()
#     seller = models.BooleanField(default=False)
#     password = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.name
    

# class Product(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     price = models.FloatField()
#     description = models.TextField()
#     image = models.ImageField()
#     category = models.CharField(max_length=200)
#     quantity = models.FloatField()
    
#     def __str__(self):
#         return self.name
    

# class Order(models.Model):
#     id = models.AutoField(primary_key=True)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     date = models.DateTimeField(auto_now_add=True)
#     status = models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.product.name