import json
from jsonschema import SchemaError

from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from db.models import Question
from db.models.category import Category
from db.models.question import Answer
from db.models.tag import Tag



class EmptySerializer(serializers.Serializer):
	pass



class AnswerCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ("text", "is_correct", "explanation")
	


class QuestionCreateSerializer(serializers.ModelSerializer):
	answers = AnswerCreateSerializer(many=True)

	class Meta:
		model = Question
		fields = ('answers', 'text', 'category')


class AnswerResponseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		exclude = ('question',)


class QuestionResponseSerializer(serializers.ModelSerializer):
	answers = AnswerResponseSerializer(many=True)

	class Meta:
		model = Question
		fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'
		read_only_fields = ('id', 'created_on',)


class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = '__all__'
		read_only_fields = ('id',)
