
from rest_framework import serializers
from .models import Pereval_added

class Pereval_addedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval_added
        fields = '__all__'


