from phonenumber_field import serializerfields
from rest_framework import serializers
from ads.models import Advertisement
from users.models import User


class AdvertisementViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = ["pk", "image", "title", "price", "description"]


class AdvertisementDetailSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),
                                                   many=False)
    phone = serializerfields.PhoneNumberField(source="author.phone", read_only=True)
    author_first_name = serializers.CharField(max_length=20, source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(max_length=30, source="author.last_name", read_only=True)

    class Meta:
        model = Advertisement
        fields = ["pk", "image", "title",
              "price", "phone", "description",
              "author_first_name", "author_last_name", "author_id", ]
