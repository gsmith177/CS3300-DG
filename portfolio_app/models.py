from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField("name",max_length=200)
    email = models.CharField(max_length=200)
    is_active = models.BooleanField()
    SKILL_LEVEL = (
    ('Professional' , 'Average score under par')
    ('Intermediate' , 'Average score on par')
    ('Beginner' , 'Average score over par')
    )
    skill_level = models.CharField(max_length=200, choices=SKILL_LEVEL, blank = False)
    date_joined = models.CharField(max_length=200)

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.title
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('portfoilio-detail', args=[str(self.id)])
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    location = models.CharField(max_length=200)