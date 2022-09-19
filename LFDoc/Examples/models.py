from django.db import models
from datetime import date, timedelta
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# These are examples of the all Field Types Django provides. You can also write your custom field.
class ModelFieldType(models.Model):
	#AutoField
	#BigAutoField
	big_integer = models.BigIntegerField()
	boolean = models.BooleanField(default=True)
	binary = models.BinaryField()
	full_name = models.CharField(_("Full Name"), max_length=50)
	username = models.CharField(max_length=50, error_messages={"blank":"Enter a username"},)
	address = models.CharField(max_length=200)
	date = models.DateField(auto_now=False, auto_now_add=False)
	datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
	decimal = models.DecimalField(max_digits=5, decimal_places=2)
	duration = models.DurationField()
	email = models.EmailField(max_length=254, blank=True)
	num = models.FloatField()
	upload_file = models.FileField(upload_to=None, max_length=100)
	#FilePathField
	#generic_ipaddress = models.GenericIPAddressField(protocol="both", unpack_ipv4=False)
	#json = models.JSONField(encoder=, decoder=)
	image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
	integer = models.IntegerField()
	positive_integer = models.PositiveIntegerField()
	positive_big_integer = models.PositiveBigIntegerField()
	positive_small_integer = models.PositiveSmallIntegerField()
	slug = models.SlugField()
	small_integer = models.SmallIntegerField()
	#SmallAutoField
	text = models.TextField()
	time = models.TimeField(auto_now=False, auto_now_add=False)
	url = models.URLField(max_length=200)
	uuid = models.UUIDField()
	
	class Meta():
		# abstract = True
		# app_label = 
		# base_manager_name = 
		# db_table =
		# db_tablespace = 
		# default_manager_name = 
		# default_related_name = 
		# get_latest_by =
		# managed = 
		# order_with_respect_to =
		ordering = ['date']
		# permissions = 
		# default_permissions =
		# proxy =
		# required_db_features = 
		# required_db_vendors =
		# select_on_save =
		# indexes =
		# unique_together = 
		# index_together =
		# constraints = 
		# verbose_name =
		# verbose_name_plural =


