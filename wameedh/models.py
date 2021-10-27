from django.db import models

# Create your models here.

class Members(models.Model):
    name=models.CharField(max_length=30)
    position=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    photo=models.ImageField(upload_to="members_images", null=True)

    def __str__(self):
        return self.name

class ClubAchivement(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    images=models.ImageField(upload_to="clubAchivemetns" ,blank=True)

    def __str__(self):
        return self.title

class ClubEvents(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    images=models.ImageField(upload_to="clubEvents" ,blank=True)

    def __str__(self):
        return self.title
    

class AboutUsInfo(models.Model):
    description=models.TextField(null=True)
    image=models.ImageField(upload_to="aboutImages",null=True)

    def __str__(self):
        return "description"