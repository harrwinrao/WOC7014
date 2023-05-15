from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'developer', 'platform']

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.developer = validated_data.get('developer', instance.developer)
        instance.platform = validated_data.get('platform', instance.platform)
        instance.save()
        return instance
