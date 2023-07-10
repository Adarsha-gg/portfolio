from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.fname