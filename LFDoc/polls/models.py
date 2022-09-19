from django.db import models
from django.utils import timezone
from django.urls import reverse

class Question(models.Model):
	question_text = models.CharField(max_length=100)
	pub_date = models.DateTimeField('Date published', auto_now_add=True)

	def __str__(self):
		return self.question_text

	def get_absolute_url(self):
		return reverse("polls:result", kwargs={"question_id": self.id})
	

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=20)
	votes = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return self.choice_text