from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^questions/$', views.QuestionView.as_view(), name='list-or-create-question'),
    re_path(r'^category/$', views.CategoryView.as_view(), name='list-or-create-category'),
    re_path(r'^tags/$', views.TagView.as_view(), name='list-or-create-tag')
]