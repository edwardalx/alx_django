from rest_framework import serializers

from .models import Customer, Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player', 'balance']

class CustomerSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Customer
        fields = ['phoneNumber','first_name', 'last_name','password','full_name']
    def get_full_name(self,obj):
        return  obj.first_name +" "+ obj.last_name
    
    
    