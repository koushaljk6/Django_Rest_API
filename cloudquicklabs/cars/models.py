import uuid
from django.db import models

class Cars(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    care_name = models.CharField(max_length=100)
    car_version = models.CharField(max_length=3)
    car_model = models.CharField(max_length=30)
