from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext as _
from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(('username'), max_length=150, default="default_username", unique=True)
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