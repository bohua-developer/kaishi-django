from __future__ import unicode_literals

from django.db import models

# Create your models here.

class LevelDirectory(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=30)
    summary = models.TextField()
    image_url = models.CharField(max_length=30)
    pubulish_date = models.DateField()
    series = models.CharField(max_length=30)
    status = models.IntegerField()

class SecondaryDirectory(models.Model):
    uuid = models.CharField(max_length=30)
    title = models.TextField()
    author = models.CharField(max_length=30)
    summary = models.TextField()
    image_url = models.CharField(max_length=30)
    pubulish_date = models.DateField()
    page_url = models.CharField(max_length=30)
    series_name = models.TextField()
    series = models.IntegerField()
    status = models.IntegerField()

class AllContentList(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=30)
    summary = models.TextField(blank=True)
    content = models.TextField()
    image_url = models.CharField(max_length=30,blank=True)
    pubulish_date = models.DateField()
    series = models.IntegerField()
    page = models.IntegerField()
    status = models.IntegerField()

