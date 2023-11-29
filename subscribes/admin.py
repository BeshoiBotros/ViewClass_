from django.contrib import admin
from .models import Subscribe, SubscribeContract, SubscribeOrder
from users.models import CustomUser
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin

# Register your custom user model with the admin
admin.site.register(CustomUser, UserAdmin)

# Register your models here.
admin.site.register(SubscribeOrder)
admin.site.register(Subscribe)
admin.site.register(SubscribeContract)
admin.site.register(Permission)
