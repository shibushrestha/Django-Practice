from django.contrib import admin

from .models import ModelFieldType
from .ValidatorPractice import ValidatorPracticeModel
from Examples.ChoicePractice import Person, Student, Media, Movie, Car, Club, MoonLanding
from Examples.Model_Instances import Restaurant, School

# for models.py
admin.site.register(ModelFieldType)

# For ValidatorPractice.py
admin.site.register(ValidatorPracticeModel)

# For ChoicePractice.py
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Media)
admin.site.register(Movie)
admin.site.register(Car)
admin.site.register(Club)
admin.site.register(MoonLanding)

# For Model_Instances.
admin.site.register(Restaurant)
admin.site.register(School)


