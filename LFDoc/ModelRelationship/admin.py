from django.contrib import admin

from ModelRelationship.RelationExample import Manufacturer, Product, Blog, Author, Entry, Car
from ModelRelationship.ManyToManyField import Publication, Article, Person, Group, Membership
from ModelRelationship.Modelinheritance import Student, MyStudent, Company, CompanyProfile


# For RelationExample.py
admin.site.register(Manufacturer)
admin.site.register(Product)

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(Car)

# For ManyToManyField.py
admin.site.register(Publication)
admin.site.register(Article)

admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)

# For Modelinheritance.py
admin.site.register(Student)
admin.site.register(MyStudent)

admin.site.register(Company)
admin.site.register(CompanyProfile)