from rest_framework.serializers import ModelSerializer
from card.models import Card

class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")