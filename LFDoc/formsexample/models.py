from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError

# A Simple name validator that only accepts alphabets
name_validator = RegexValidator(r'^[a-zA-Z]*$', message='Only alphabet are allowed.', code='invalid')

# But the preffered way to add method to class is through manager
class PersonManager(models.Manager):
    def create_person(self, username, first_name, last_name, date_of_birth, email, comments):
        person = self.create(username=username, 
            first_name=first_name, 
            last_name=last_name, 
            date_of_birth=date_of_birth, 
            email=email, 
            comments=comments)

        return person

# A model to practice ModelForm
class Person(models.Model):
    username = models.CharField(max_length=100, unique=True, 
        error_messages={'unique':'Username already taken.',}
        )
    first_name = models.CharField(max_length=100, validators=[name_validator],)
    last_name = models.CharField(max_length=100, validators=[name_validator])
    date_of_birth = models.DateField()
    email = models.CharField(max_length=100,
        validators=[EmailValidator(message='Please enter a valid email address', code='invalid')]
        )
    comments = models.TextField(max_length=1000)

    objects = PersonManager()


    def __str__(self):
        return self.username
    
    '''
    def clean(self):
        if self.email == "shibushrestha12@gmail.com":
            raise ValidationError({'email':'Email already in use.'})
        return self.email
    '''




    


