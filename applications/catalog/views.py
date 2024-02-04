import hashlib
import json
from django.db import transaction
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from jsonschema.exceptions import ValidationError as OpenAPIValidationError
from applications.catalog.serializers import CategorySerializer, QuestionCreateSerializer, QuestionResponseSerializer, TagSerializer
from db.models.category import Category

from db.models.question import Answer, Question
from db.models.tag import Tag



class ModelMixin:
	response_serializer_class: serializers.Serializer = None

	def get_response_data(self, result):
		serialized_data = "Operation completed successfully"
		if result :
			serialized_data = self.response_serializer_class(result).data if self.response_serializer_class else self.get_serializer(result).data
		return serialized_data

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())

		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True) if not self.response_serializer_class else self.response_serializer_class(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(queryset, many=True) if not self.response_serializer_class else self.response_serializer_class(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.response_serializer_class(instance) if self.response_serializer_class else self.get_serializer(instance)
		return Response(serializer.data)

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		result = self.perform_create(serializer)
		return Response(data=self.get_response_data(result), status=status.HTTP_201_CREATED)

	def update(self, request, *args, **kwargs):
		partial = kwargs.pop('partial', False)
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data, partial=partial)
		serializer.is_valid(raise_exception=True)
		result = self.perform_update(serializer)

		if getattr(instance, '_prefetched_objects_cache', None):
			# If 'prefetch_related' has been applied to a queryset, we need to
			# forcibly invalidate the prefetch cache on the instance.
			instance._prefetched_objects_cache = {}

		return Response(data=self.get_response_data(result), status=status.HTTP_200_OK)


class QuestionView(ModelMixin, ListCreateAPIView):
	queryset = Question.objects.all()
	serializer_class = QuestionCreateSerializer
	response_serializer_class = QuestionResponseSerializer

	def perform_create(self, serializer: QuestionCreateSerializer):
		answers_data = serializer.validated_data.pop("answers")
		question_data = serializer.validated_data
		checksum = hashlib.md5(question_data["text"].lower().encode("utf-8")).hexdigest()

		with transaction.atomic():
			question = Question.objects.create(**question_data, checksum=checksum)
			answers = [Answer(
				text=answer_data["text"], 
				question=question, 
				is_correct=answer_data.get("is_correct", False), 
				explanation=answer_data.get("explanation")
			) for answer_data in answers_data]
			Answer.objects.bulk_create(answers
		)
		return question


class CategoryView(ModelMixin, ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

	def perform_create(self, serializer: CategorySerializer):
		return Category.objects.create(**serializer.validated_data)
	

class TagView(ModelMixin, ListCreateAPIView):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer

	def perform_create(self, serializer: CategorySerializer):
		return Tag.objects.create(**serializer.validated_data)
