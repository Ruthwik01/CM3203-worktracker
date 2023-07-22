from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class theTask(models.Model):
    priority = [('High Priority', 'High Priority'),('Medium Priority', 'Medium Priority'),('Low Priority', 'Low Priority'),]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    accomplished = models.BooleanField(default=False)
    crtd = models.DateTimeField(auto_now_add=True)
    taskpriority = models.CharField(max_length=20, choices=priority, default='Medium Priority')
    
    def __str__(self):
        return self.title
    
  
class Assessment(models.Model):
    module=models.CharField(max_length=250, null=True, blank=True)
    contribution=models.CharField(max_length=250, null=True, blank=True)
    Title=models.CharField(max_length=250, null=True, blank=True)
    type=models.CharField(max_length=250, null=True, blank=True)
    Hand_out_date=models.CharField(max_length=250, null=True, blank=True)
    hand_in_date=models.CharField(max_length=250, null=True, blank=True)
    suggesteddeadline = models.DateField(null=True, blank=True)
    
