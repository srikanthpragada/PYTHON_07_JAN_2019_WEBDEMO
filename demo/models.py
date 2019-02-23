from django.db import models


# Create your models here.

class Course:
    def __init__(self, name, fee, duration):
        self.name = name
        self.fee = fee
        self.duration = duration


class Title(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}, {self.title}, {self.author}, {self.price}"

