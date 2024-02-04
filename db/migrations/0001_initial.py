# Generated by Django 5.0.1 on 2024-02-04 21:27

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.category')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('checksum', models.CharField(max_length=32, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='db.category')),
                ('tags', models.ManyToManyField(to='db.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('explanation', models.TextField(null=True)),
                ('is_correct', models.BooleanField(default=False)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='db.question')),
            ],
        ),
    ]
