from django.contrib import admin
from .models import User, Listing, Booking, Review
from .serializers import UserSerializer


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'Email')
    search_fields = ('first_name', 'last_name',  'Email', 'id',
                     'password')
    UserSerializer = UserSerializer()

    class Meta:
        model = User
        fields = ['first_name', 'last_name',  'Email', 'id',
                  'password']


admin.site.register(User, UserAdmin)
admin.site.register(Listing)
admin.site.register(Booking)
admin.site.register(Review)
