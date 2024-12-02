from rest_framework import serializers
from .models import Customer
from django.contrib.auth.hashers import make_password

class CustomerRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'village', 'district', 'state', 'country', 'pincode', 'role', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        customer = Customer.objects.create(**validated_data)
        return customer

class CustomerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=[('buyer', 'Buyer'), ('seller', 'Seller')])

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')

        if not email or not password:
            raise serializers.ValidationError("Email and Password are required.")
        return data