from django.db import models
import math

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    charClass = models.CharField(max_length=100)
    xp = models.IntegerField(default=0)
    gp = models.IntegerField(default=0)
    sp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    maxSP = models.IntegerField(default=0)
    
    #override save function to set level calculated by XP & increase maxSP 
    def save(self, *args, **kwargs):
        #if less than 1500xp, set level to 1
        if math.ceil(self.xp/1500)<1:
            self.level = 1
        #otherwise, set level 1500 per level
        else:
            self.level = math.ceil(self.xp/1500)
        #increase max-SP every 10 levels
        if self.level < 10:
            self.maxSP = 5
        elif self.level < 20:
            self.maxSP = 6
        elif self.level < 30:
            self.maxSP = 7
        elif self.level < 40:
            self.maxSP = 8
        elif self.level < 50:
            self.maxSP = 9
        else:
            self.maxSP = 10
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'student'
    

class Behaviors(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    xp = models.IntegerField(default=0)
    gp = models.IntegerField(default=0)

    class Meta: 
        db_table = "behaviors"


class Skills(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    sp = models.IntegerField(default=0)
    charClass = models.CharField(max_length=50)
    levelReq = models.IntegerField(default=0)
    
    class Meta: 
        db_table = "skills"

class RandomEvents(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    sp = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    gp = models.IntegerField(default=0)
    charClass = models.CharField(max_length=50)
    randomStudent = models.BooleanField(default=False)
    
    class Meta: 
        db_table = "random-events"

class Miracles(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    sp = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)
    gp = models.IntegerField(default=0)

    class Meta: 
        db_table = "miracles"