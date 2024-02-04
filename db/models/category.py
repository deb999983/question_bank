import uuid
from django.db import models



class Category(models.Model):
	id = models.UUIDField(default=uuid.uuid1, primary_key=True)
	name = models.CharField(max_length=50, unique=True)
	parent = models.ForeignKey("self", null=True, on_delete=models.CASCADE)
	description = models.TextField(null=True)
	created_on = models.DateTimeField(auto_now_add=True)
