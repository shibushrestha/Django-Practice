from django.db import models
from django.db.models.enums import Choices
from django.utils.translation import gettext_lazy as _
import datetime

# These are some examples of the choice field option
class Person(models.Model):
    SHIRT_SIZE = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
    ]
    name = models.CharField(max_length=15)
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZE)

# or you can do the above example like this
class Student(models.Model):
    Freshman = 'FR'
    Sophomore = 'SO'
    Junior = 'JR'
    Senior = 'SR'
    Graduate = 'GR'
    YEAR_IN_SCHOOL = [
        (Freshman, 'Freshman'),
        (Sophomore, 'Sophomore'),
        (Junior, 'Junior'),
        (Senior, 'Senior'),
        (Graduate, 'Graduate')
    ]
    student_name = models.CharField(max_length=15)
    year_in_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL, default=Freshman)

    def is_upperclass(self):
        return self.year_in_school in {self.Junior, self.Senior}


# You can also collect your choices in named group
class Media(models.Model):
    MEDIA_TYPE = [
        ('Audio',(
            ('Cd', 'Cd'),
            ('Cas', 'Cassette'),
            )
        ),

        ('Video',(
            ('VHS', 'VHS Tape'),
            ('DVD', 'DVD'),
            )
        ),

        ('Unknown', 'Unknown'),
    ]
    name = models.CharField(max_length=30)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE)

# In addition django also provide enumeration type that you can subclass to define choices in a concise way
class Movie(models.Model):
    class Genre(models.TextChoices):
        HORROR = 'H',_('Horror')
        FICTION = 'S',_('Science Fiction')
        ROMANCE = 'R',_('Romance')
        ACTION = 'A',_('Action')
        UNKNOWN = 'U',_('Unknown')
    movie_name = models.CharField(max_length=30)
    genre = models.CharField(max_length=1, choices=Genre.choices, blank=False, default=Genre.UNKNOWN)

    def __str__(self):
        return self.movie_name


# If you don't want to have the human-readable name translated you can do it like this
class Car(models.Model):
    class CarType(models.TextChoices):
        SEDAN = 'SD'
        SPORTS = 'SR'
        SUV = 'SUV'

    car_name = models.CharField(max_length=20)
    car_type = models.CharField(max_length=3, choices=CarType.choices, default='SD')

    # here you can get the human-readable by (CarType.SEDAN.labels) which will be Sedan

# Django also provides IntegerChoices
class Club(models.Model):
    class ClubRanking(models.IntegerChoices):
        FIRST = 1
        SECOND = 2
        THIRD = 3
        FOURTH = 4
    
    club_name = models.CharField(max_length=30)
    club_ranking = models.CharField(max_length=1, choices=ClubRanking.choices, default=4)


'''It is also possible to make use of the Enum Functional API with the caveat that 
labels are automatically generated as highlighted above:'''

# You can use concrete data types in the choices, like the example below which takes date as its choices
class MoonLanding(models.Model):
    class MoonLandingsChoices(datetime.date, models.Choices):
        APOLLO_11 = 1969, 7, 20, 'Apollo 11 (Eagle)'
        APOLLO_12 = 1969, 11, 19, 'Apollo 12 (Intrepid)'
        APOLLO_14 = 1971, 2, 5, 'Apollo 14 (Antares)'
        APOLLO_15 = 1971, 7, 30, 'Apollo 15 (Falcon)'
        APOLLO_16 = 1972, 4, 21, 'Apollo 16 (Orion)'
        APOLLO_17 = 1972, 12, 11, 'Apollo 17 (Challenger)'
    astranaut_name = models.CharField(max_length=100, blank=True)
    moon_landings = models.DateField(choices=MoonLandingsChoices.choices)

    def __str__(self):
        return ('%s %a') % (self.moon_landings, self.astranaut_name)