from rest_framework import serializers
from .models import Card,HUMO,UZCARD,VISA


class CardSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    card_type = serializers.CharField(required=False)
    user = serializers.IntegerField(required=False)
    card_number = serializers.CharField(max_length=16,min_length=16)
    valid_time = serializers.CharField(max_length=4,min_length=4)


    class Meta:
        model=Card
        fields = ('id', 'card_number', 'valid_time', 'card_type', 'bank_name', 'name', 'user')



    def validate(self, attrs):
        card_number = attrs['card_number']

        if card_number.startswith('8600'):
            attrs['card_type'] = 'UZCARD'
        elif card_number.startswith('9860'):
           attrs['card_type'] = 'HUMO'
        else:
           attrs['card_type'] ='VISA'

        attrs['user']=1

        return attrs


    def create(self, validated_data):
        card = Card(
            card_number=validated_data['card_number'],
            valid_time=validated_data['valid_time'],
            card_type=validated_data['card_type'],
            bank_name=validated_data['bank_name'],
            name=validated_data['name'],
            user_id=validated_data['user'],
        )
        card.save()

        return card