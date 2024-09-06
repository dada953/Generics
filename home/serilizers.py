from rest_framework import serializers
from home.models import CustomUser
class RegisterUser(serializers.ModelSerializer):
    confirm_password = serializers.CharField(min_length=6, max_length=20, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'address', 'password', 'confirm_password']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self, validated_data):
        user = CustomUser(
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
               # username=validated_data['username'],
                email=validated_data['email'],
                #mobileno=validated_data['mobileno'],
                address=validated_data['address'],
              #  gender=validated_data['gender'],
            )
                