from rest_framework import serializers
from .models import Account
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import  get_adapter

class AccountSerializer(serializers.Serializer):

    class Meta:
        model=Account
        fields=('email','name',)
        read_only_fields=('email','name',)

class CustomRegisterSerializer(RegisterSerializer):
    email=serializers.EmailField(required=True)
    name=serializers.CharField(required=True)
    password1=serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer,self).get_cleaned_data()
        return {
            'password1':self.validated_data.get('password1',''),
            'email':self.validated_data.get('email',''),
            'name':self.validated_data.get('name','')
        }
    def save(self, request):
        adapter=get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data=self.get_cleaned_data()
        adapter.save_user(request,user,self)
        user.name=self.cleaned_data.get('name')
        user.save()
        return user