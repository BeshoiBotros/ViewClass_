from django.db import models
from users.models import CustomUser

class Subscribe(models.Model):
    name = models.CharField(max_length=255)
    numsOfSubscribers = models.BigIntegerField()
    startDuration = models.DateField(null=True, blank=True)
    endDuration = models.DateField(null=True, blank=True)
    isFree = models.BooleanField(default=False)
    price = models.FloatField(null=True, blank=True)
    active = models.BooleanField(default=True)
    discription = models.TextField(null=True, blank=True)
    subscribeType = models.TextField(null=True, blank=True)

class SubscribeOrder(models.Model):
    requestStatusChoices = (('underProcess', 'تحت الاجراء'), ('accepted', 'مقبول'), ('rejected', 'مرفوض'), ('canceled', 'ملغي'), ('other', 'اخرى'))
    subscribe = models.ForeignKey(Subscribe, on_delete=models.CASCADE)
    companyuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)
    companyName = models.CharField(max_length=255)
    companyAddres = models.TextField(null=False, blank=False)
    companyNo = models.CharField(max_length=200, blank=True,default='')
    companyID = models.FileField(upload_to='companyID/')
    companyURL = models.URLField(null=True, blank=True)
    companyEmail = models.EmailField(null=True, blank=True)
    responsibleName = models.CharField(max_length=255)
    responsiblePhone = models.CharField(max_length=15)
    responsibleEmail = models.EmailField(null=True, blank=True)
    requestStatus = models.CharField(choices=requestStatusChoices, max_length=30, default='تحت الاجراء')
    statusDiscription = models.TextField(null=True, blank=True)

class SubscribeContract(models.Model):
    subscribeOrder = models.ForeignKey(SubscribeOrder, models.CASCADE)
    subscribeContractStatusChoices = (('underProcess', 'جاري التعاقد'), ('paied', 'مدفوع'), ('unpaied', 'غير مدفوع'), ('canceled', 'ملغي'), ('rejected', 'مرفوض'), ('other', 'اخرى'))
    statusDiscription = models.TextField(null=True, blank=True)
    subscribeContractStatus = models.CharField(choices=subscribeContractStatusChoices, max_length=30)
    numsOfOrganization = models.IntegerField()
    numsOfUsers  = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    paiedAmount = models.FloatField()
    recieptFile = models.FileField(upload_to='recieptFile/')
    contractFile = models.FileField(upload_to='contractDiscription/')
    contractDiscription = models.TextField(null=True, blank=True)
    contractAproval = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)

