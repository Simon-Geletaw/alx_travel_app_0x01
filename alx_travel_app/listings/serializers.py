from rest_framework import serializers
from listings.models import User, Listing, Review, Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ListingSerializer(serializers.Serializer):
    UserSerializer = UserSerializer()

    class Meta:
        model = Listing
        fields = ['UserSerializer']
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    UserSerializer = UserSerializer()
    ListingSerializer = ListingSerializer()

    class Meta:
        model = Booking
        fields = ['UserSerializer', 'ListingSerializer']
        fields = '__all__'


class review(serializers.ModelSerializer):
    UserSerializer = UserSerializer()
    ListingSerializer = ListingSerializer()

    class Meta:
        model = Review
        fields = ['UserSerializer', 'ListingSerializer']
        fields = '__all__'
