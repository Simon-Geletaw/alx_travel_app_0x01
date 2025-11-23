from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    user_name = models.CharField(max_length=10, unique=True, db_index=True,
                                 null=False)
    Email = models.EmailField(max_length=254, unique=True, db_index=True,
                              null=False)


class Listing(models.Model):
    user_id = models.ForeignKey(User,  on_delete=models.CASCADE)
    Listing_id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=10)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class Booking(models.Model):
    guest_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    booking_id = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    rate_id = models.UUIDField(primary_key=True)
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    Rating = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(Rating__range=(0, 5)),
                name='rate_between_0_and_5'
            )
        ]
