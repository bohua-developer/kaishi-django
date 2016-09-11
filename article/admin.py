from django.contrib import admin
from article.models import LevelDirectory,SecondaryDirectory,AllContentList

# Register your models here.

admin.site.register(LevelDirectory)
admin.site.register(SecondaryDirectory)
admin.site.register(AllContentList)

