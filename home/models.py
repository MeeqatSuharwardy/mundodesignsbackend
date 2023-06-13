from django.db import models


# Create your models here.


class About(models.Model):
    title_first = models.CharField(max_length=100)
    title_second = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='about_images/')
    image2 = models.ImageField(upload_to='about_images/')
    content = models.TextField()
    exp = models.IntegerField()
    # Assuming "textList" is a related model (ForeignKey, ManyToMany, or OneToOne)
    # you can adjust the field type according to your specific requirement


class Intro(models.Model):
    id = models.IntegerField(primary_key=True)
    title_first = models.CharField(max_length=100)
    title_second = models.CharField(max_length=100)
    content_first = models.CharField(max_length=200)
    content_second = models.CharField(max_length=200)
    image = models.ImageField(upload_to='intro_images/')


class Service(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
