from django.db import models



# Example of Abstract base class
class CommonInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField()

    class Meta:
        abstract = True
    
class Student(CommonInfo):
    YEAR_IN_SCHOOL = [
        ('FRESHMAN', 'Freshman'),
        ('SOPHOMORE', 'Sophpmore'),
        ('GRADUATE', 'Graduate'),
        ('SENIOR', 'Senior'),
        ('JUNIOR', 'Junior'),
    ]
    FACULTY = [
        ('S', 'Science'),
        ('C', 'Commerce'),
        ('H', 'Humainity'),
    ]
    year_in_school = models.CharField(max_length=9, choices=YEAR_IN_SCHOOL,)
    faculty = models.CharField(max_length=1, choices=FACULTY,)


# PROXY MODEL
'''Proxy model is used when you just want to change the 
python-level behaviour of the model or want to add extra methods on the model.'''

class MyStudent(Student):
    class Meta():
        proxy = True
        ordering = ['first_name']

    def __str__(self):
        return self.first_name

    @property    
    def get_fullname(self):
        return '%s %s' %(self.first_name, self.last_name) 
    
    
    
# MULTI-TABLE INGERITANCE
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=20)

# All the fields in the Company model will be available here.
class CompanyProfile(Company):
    established = models.DateField(blank=True)


