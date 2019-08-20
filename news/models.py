from django.db import models
from django.contrib.auth import get_user_model
import string
import random

from django.urls import reverse

User = get_user_model()


# Create your models here.

def generate_token():
    return "".join([random.choice(string.ascii_letters + string.digits) for _ in range(120)])


class Data(models.Model):
    data = models.TextField()

    def __str__(self):
        return f"{self.data}"


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=120, default=generate_token)

    expire = models.BooleanField(default=False)

    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.token}"

    def get_verify_url(self):
        return reverse("verify", kwargs={"token": self.token,
                                         "user_id": self.user_id})
