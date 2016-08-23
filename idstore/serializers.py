from rest_framework import serializers
from .models import IdPair


class IdPairSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = IdPair
        fields = ('udn_id', 'external_id')

    def create(self, validated_data):
        return IdPair.objects.create(**validated_data)
