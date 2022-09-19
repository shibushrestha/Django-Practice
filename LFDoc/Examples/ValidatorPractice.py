from django.db import models
from django.core.validators import (DecimalValidator, EmailValidator, 
    MaxLengthValidator, MinLengthValidator, MaxValueValidator, MinValueValidator, RegexValidator)

# Using some built-in validators
first_name = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabet are allowed.')
username = RegexValidator(regex=r'^[0-9a-zA-Z@!]*$', message='Only alphanumeric characters and @ ! are allowed.')
min_amount = MinValueValidator(limit_value=100, message='Your value should be greater than hundred')
max_amount = MaxValueValidator(limit_value=1000000, message="Your amount cannot be greater than ten lakhs")
min_length = MinLengthValidator(limit_value=4, message="Your code must be atleast 4 character long.")
max_length = MaxLengthValidator(limit_value=10, message="Your code cannot be longer than 10 character.")
#decimal_validator = DecimalValidator(max_digits=10, decimal_places=4)

# These are examples of some Model Field Types and how to uses built-in Validators
class ValidatorPracticeModel(models.Model):
    first_name = models.CharField(max_length=50, validators=[first_name])
    username = models.CharField(max_length=15, validators=[username])
    email = models.EmailField()
    amount = models.PositiveIntegerField(validators=[min_amount])
    max_amount = models.PositiveIntegerField(validators=[max_amount])
    code = models.CharField(max_length=10, validators=[min_length])
    price = models.DecimalField(max_digits=10, decimal_places=4)
    
    def __str__(self):
        return self.username



# BUILT-IN VALIDATORS

# RegexValidator
# MinValueValidator
# MaxValueValidator
# MinLengthValidator
# MaxLengthValidator
# EmailValidator
# validate_email
# URLValidator
# validate_slug
# validate_unicode_slug
# validate_ip4_address
# validate_ip6_address
# validate_ip46_address
# validate_comma_separated_integer_list
# int_list_validator
# DecimalValidator
# FileExtensionValidator
# validate_image_file_extension
# ProhibitNullCharactersValidator