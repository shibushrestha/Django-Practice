from django.db import models

# This is a simple example of many-to-one relationship
class Manufacturer(models.Model):
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

def get_default_manufacturer():
	return Manufacturer.objects.get_or_create(name='Unknown')[0]

class Product(models.Model):
	manufacturer = models.ForeignKey(Manufacturer, models.SET_DEFAULT, default=get_default_manufacturer)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Car(models.Model):
	Manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


# This model is from the document, we will practice some queryset with this model
class Blog(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()

	def __str__(self):
		return self.name


class Author(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()

	def __str__(self):
		return self.name


class Entry(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='entries', related_query_name='all_entries',)
	headline = models.CharField(max_length=255)
	body_text = models.TextField()
	pub_date = models.DateField()
	mod_date = models.DateField()
	author = models.ManyToManyField(Author)
	number_of_comments = models.IntegerField(default=0)
	number_of_pingbacks = models.IntegerField(default=0)
	rating = models.IntegerField(default=0)
	
	class Meta:
		verbose_name_plural = 'Entries'
	
	def __str__(self):
		return self.headline