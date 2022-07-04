
from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        rating = Rating.objects.create(**validated_data)
        return rating

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['movie'] = str(instance)
        return rep
