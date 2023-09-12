from django.db import models

class ContactMe(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 150)
    subject = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
