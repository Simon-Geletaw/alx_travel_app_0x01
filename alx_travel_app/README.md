# alx_travel_app 
## objective 
Define the database models, create serializers for API data representation, and implement a management command to seed the database.
## Models
- user
- - user_id  UUID primary key
- - user_name unique not null
- - email not null
- - password not null 
- - created_at
- Listings
- - listing_id 
- - user_id
- - Title
- - location
- - price
- - created_at
- - updated_at
- Booking
- - booking_id
- - listing_id(foriegn_key)
- - user_id(foriegn_key)
- - booking_date
- Review 
- - listing_id(forign_key)
- - user_id(foriegn-key)
- - rating
- - comment
- - created_at
## relation-ships
 relation between user and booking , listing i one to many one user might list,book(different time) properties