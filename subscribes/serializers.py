from rest_framework import serializers
from .models import Subscribe, SubscribeContract, SubscribeOrder
from rest_framework_recaptcha.fields import ReCaptchaField

class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'

class SubscribeContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribeContract
        fields = '__all__'


class SubscribeOrderSerializer(serializers.ModelSerializer):
    recaptcha = ReCaptchaField()
    class Meta:
        model = SubscribeOrder
        fields = '__all__'

