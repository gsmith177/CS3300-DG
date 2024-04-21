from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext as _
from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, skill_level=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, skill_level=skill_level, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, skill_level=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, name, password, skill_level, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField("name", max_length=200)
    email = models.EmailField(('email address'), unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    SKILL_LEVEL = (
        ('Professional', 'Average score under par'),
        ('Intermediate', 'Average score on par'),
        ('Beginner', 'Average score over par'),
    )
    skill_level = models.CharField(max_length=200, choices=SKILL_LEVEL, blank=False)
    date_joined = models.DateField(("Date"), default=date.today)

    password = models.CharField(max_length=128, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # Define custom related names for groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_groups',
        related_query_name='custom_user_group',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission',
        help_text=_('Specific permissions for this user.'),
    )

    # Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    # Returns the URL to access a particular instance of MyModelName.
    # if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('User-detail', args=[str(self.id)])

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200)
    num_joined = models.IntegerField(default=0)

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.location
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('Posts', args=[str(self.id)])