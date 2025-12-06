from rest_framework import serializers
from listings.models import User, Listing, Review, Booking
import uuid
from rest_framework import status

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def create(self, validated_data):
        validated_data['id'] = str(uuid.uuid4())
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        
    def getdata(self, instance):
        users = User.objects.values('first_name', 'last_name', 'user_name', 
                                    'Email')
        self.authenticate()
    
    def authenticate(self, username, password):
        try:
            user = User.objects.get(user_name=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return status.HTTP_401_UNAUTHORIZED
       
     
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
        