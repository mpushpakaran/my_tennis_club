from django.db import models

# Create your models here.
class member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    # firstname, is a Text field, and will contain the first name of the members. 255 chars
    # lastname, is also a Text field, with the member's last name. 255 chars
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

'''
As you can see, we want to add phone and joined_date to our Member Model.
This is a change in the Model's structure, and therefor we have to make a migration to tell Django that it has to update the database:
py manage.py makemigrations members
Which, in my case, will result in a prompt, because I try to add fields that are not allowed to be null, to a table that already contains records.

'''