from rest_framework import serializers
from.models import KapitalBank

class KapitalBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = KapitalBank
        fields = '__all__'
        
        