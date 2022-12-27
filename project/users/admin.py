from django.contrib import admin
from .models import userMessage, adminMessage

# Register your models here.
admin.site.register(userMessage)
admin.site.register(adminMessage)