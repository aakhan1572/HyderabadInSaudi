from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields.related import ForeignKey, OneToOneField

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None,phone_number=0,company='x'):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        if not phone_number:
            raise ValueError('User must have phone Number')            

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            phone_number=phone_number,
            company=company
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    OWNER = 1
    VENDOR = 2
    AGENT = 3
    SUBAGENT = 4
    TENENT = 5
    ASSOCIATE = 6

    ROLE_CHOICE = (
        (OWNER, 'Owner'),
        (VENDOR, 'Vendor'),
        (AGENT, 'Agent'),
        (SUBAGENT, 'Subagent'),
        (TENENT, 'Tenent'),
        (ASSOCIATE, 'Associate'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True)

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_role(self):
        if self.role == 1:
            user_role = 'Owner'
        elif self.role == 2:
            user_role = 'Vendor'            
        elif self.role == 3:
            user_role = 'Agent'
        elif self.role == 4:
            user_role = 'Subagent'
        elif self.role == 5:
            user_role = 'Tenent'            
        elif self.role == 6:
            user_role = 'Associate'
        elif self.role == 7:
            user_role = 'Customer'
        return user_role

class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='users/cover_photos', blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=20,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # def full_address(self):
    #     return f'{self.address_line_1}, {self.address_line_2}'

    def __str__(self):
        return self.user.email
 
    def save(self, *args, **kwargs):
            self.latitude = 53.30462100000002
            self.longitude=-6.328125
            self.location = 'Hyderabad'
            return super(UserProfile, self).save(*args, **kwargs)


class Contactus(models.Model):
    fullname=models.CharField(max_length=100, blank=True, null=True)
    mobileno=models.CharField(max_length=100, blank=True, null=True)
    email=models.CharField(max_length=100, blank=True, null=True)
    address=models.CharField(max_length=100, blank=True, null=True)
    purpose=models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    last_login= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.fullname




class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

"""     def save(self, *args, **kwargs):
        if self.latitude and self.longitude:
            self.location = Point(float(self.longitude), float(self.latitude))
            return super(UserProfile, self).save(*args, **kwargs)
        return super(UserProfile, self).save(*args, **kwargs)
 """

