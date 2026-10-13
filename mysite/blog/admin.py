from django.contrib import admin

# Register your models here.
from .models import Post, Voetbalspelers

admin.site.register(Post)
admin.site.register(Voetbalspelers)