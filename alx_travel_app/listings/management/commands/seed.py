import json
import uuid
from django.core.management.base import BaseCommand
from listings.serializers import UserSerializer
from django.conf import settings
import os


class Command(BaseCommand):
    help = "Load user data from JSON file"

    def handle(self, *args, **kwargs):
        json_path = os.path.join(settings.BASE_DIR, "userdata.json")
        with open(json_path, "r") as file:
            data = json.load(file)

        for item in data:
            user_data = {
                "id": str(uuid.uuid4()),
                "first_name": item["first_name"],
                "last_name": item["last_name"],
                "username": item["username"],
                "email": item["email"],
                "password": item["password"],
            }

            serializer = UserSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
            else:
                self.stdout.write(self.style.ERROR(f"Error: {serializer.errors}"))

        self.stdout.write(self.style.SUCCESS("Users imported successfully!"))
