import uuid
from django.db import models


class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True)
	description = models.TextField(null=True)
