

from ..models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    id          = serializers.IntegerField(required=False, read_only=True)
    firstName   = serializers.CharField(max_length=20)
    lastName    = serializers.CharField(max_length=20)
    emailId     = serializers.EmailField()
    number      = serializers.CharField(max_length=10)

    def validate_emailId(self, value):
        if self.context['request'].method == 'POST':
            if User.objects.filter(emailId=value).exists():
                raise serializers.ValidationError('Email Id already Exists.')
            return value
        else:
            return value

    class Meta:
        model   = User
        fields  = ['id','firstName', 'lastName', 'emailId', 'number']
