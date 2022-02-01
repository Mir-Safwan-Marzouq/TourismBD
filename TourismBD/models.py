from django.db import models

# Create your models here.
class Division(models.Model):
    heading = models.CharField(max_length=50)
    headline= models.TextField()
    banner=models.ImageField()
    introHead= models.CharField(max_length=50)
    intro=models.TextField()
    image=models.ImageField()
    history=models.TextField()

    def __str__(self):
        return self.heading

class District_info(models.Model):
    divisionName = models.ForeignKey(Division,on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    headquarter = models.CharField(max_length=50)
    area = models.FloatField()
    census2011 = models.IntegerField()

    def __str__(self):
        return self.name


class District_travel(models.Model):
    districtName= models.ForeignKey(District_info,on_delete = models.CASCADE)
    divsion_name= models.ForeignKey(Division,on_delete = models.CASCADE)
    name= models.CharField(max_length=50)
    image=models.ImageField()
    headline=models.TextField()
    description=models.TextField()
    transportationCost=models.TextField()
    FoodCost=models.TextField()
    map=models.TextField()

    def __str__(self):
        return self.name

class Feedback(models.Model):
    fullName=models.CharField(max_length=100)
    emailAddress=models.EmailField()
    feedbackText=models.TextField()

    def __str__(self):
        return self.fullName

class District_popular_thing(models.Model):
    districtName= models.ForeignKey(District_info,on_delete = models.CASCADE)
    divsion_name= models.ForeignKey(Division,on_delete = models.CASCADE)
    name= models.CharField(max_length=50)
    image=models.ImageField()

    def __str__(self):
        return self.name
