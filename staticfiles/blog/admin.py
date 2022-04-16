from dataclasses import fields
from django.contrib import admin

from blog.models import Portfolio

# Register your models here.
admin.site.register(Portfolio)
