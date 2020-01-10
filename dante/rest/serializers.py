from rest_framework import serializers
from dante.models import Hospital , Dept

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['Hospital_id', 'Hospital_name']
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dept
        fields = ['Uid','Type', 'Hospital_id'  ]