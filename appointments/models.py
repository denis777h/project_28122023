from django.db import models
from datetime import datetime
# Create your models here.


class Appointment(models.Model):
    date = models.DateField(
        default=datetime.utcnow,
    )
    client_name = models.CharField(max_length=200)

    messsage = models.TextField()


    def __str__(self):
        return f'{self.client_name}: {self.messsage}'
