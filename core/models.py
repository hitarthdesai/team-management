from django.db import models


class Member(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName

    def __str__(self):
        return self.lastName
