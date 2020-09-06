from django.db import models
class user(models.Model):
    email_id = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
