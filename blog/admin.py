#!/bin/python3.4
#Django
#author: David Buckle
#
from django.contrib import admin
from .models import Post

admin.site.register(Post)
