from django.db import models


# Create your models here.

class Course:
    def __init__(self, name, fee, duration):
        self.name = name
        self.fee = fee
        self.duration = duration
