import hashlib
import uuid
from django.db import models

from db.models import Category
from db.models import Tag


class Question(models.Model):
	id = models.UUIDField(default=uuid.uuid1, primary_key=True)

	text = models.TextField(null=False)
	checksum = models.CharField(max_length=32, unique=True)

	category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="questions")
	created_on = models.DateTimeField(auto_now_add=True)

	tags = models.ManyToManyField(Tag)


class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")

	text = models.TextField(null=False)
	explanation = models.TextField(null=True)
	is_correct = models.BooleanField(default=False) 						# Cannot be unique per question
	
	updated_on = models.DateTimeField(auto_now=True)
