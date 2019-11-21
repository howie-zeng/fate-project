from django.db import models

class submit(models.Model):
    age = models.CharField()
    gender = models.CharField()
    education = models.CharField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    ID = models.CharField()
