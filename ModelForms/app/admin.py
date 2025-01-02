from django.contrib import admin
from .models import user, blog

# Register the user model
admin.site.register(user)
admin.site.register(blog)