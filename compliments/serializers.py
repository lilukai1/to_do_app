from compliments.models import Compliments
from datetime import datetime
from rest_framework import serializers
from compliments.models import TIME_CHOICES, PERSON_CHOICES

class ComplimentSerializer(serializers.Serializer):
    category = serializers.ChoiceField(choices=TIME_CHOICES, default='anytime',)
    compliment = serializers.CharField(required=True, max_length=75)
    person = serializers.CharField(max_length=10)
    created = serializers.DateTimeField(default=datetime.now())
  
    def create(self, validated_data):
        return Compliments.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.compliment = validated_data.get('compliment', instance.compliment)
        instance.person = validated_data.get('person', instance.person)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
