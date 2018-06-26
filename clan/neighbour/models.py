from django.db import models

 Create your models here.
class UserProfile(models.Model):
    '''
    User class to save app user data
    '''

    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True )
    name = models.CharField(max_length = 100,null = True)
    identification = models.IntegerField(null = True)
    neighbourhood = models.ForeignKey
    location = models.CharField(max_length = 100,null = True)
    avatar = models.ImageField(upload_to = 'avatar/',null = True)

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

class Neighborhood(models.Model):
    '''
    class for saving neighbourhood data
    '''
    name  = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    occupant_count = models.IntegerField()
    def __str__(self):
        return self.name
    def save_neighborhood(self):
        self.save()
