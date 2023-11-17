from django.contrib import admin
from .models import Subscribe, SubscribeContract, SubscribeOrder
from django.contrib.auth.models import Permission
# Register your models here.

admin.site.register(SubscribeOrder)
admin.site.register(Subscribe)
admin.site.register(SubscribeContract)
admin.site.register(Permission)