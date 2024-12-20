from django.contrib.auth.models import User
from rest_framework import serializers

class CreateUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def create(self, validated_data):
        password1 = validated_data.pop('password1')
        password2 = validated_data.pop('password2')
        
        if password1 != password2:
            raise serializers.ValidationError({"Password":"Password mismatch"})
        
        user = User(**validated_data)
        user.set_password(password1)
        user.save()
        
        return user
    
    def update(self, instance, validated_data):
        if 'username' in validated_data and instance.username != validated_data['username']:
            raise serializers.ValidationError({"Incorrect Username"})
        
        print(validated_data['email'])
        print(instance.email)
        
        instance.email = validated_data.get('email', instance.email)
        
        if 'password1' in validated_data and 'password2' in validated_data:
            password1 = validated_data.pop('password1')
            password2 = validated_data.pop('password2')
            if password1 != password2:
                raise serializers.ValidationError({"Password": "Password mismatch"})
            instance.set_password(password1)
    
        instance.save()
        
        return instance
        
        