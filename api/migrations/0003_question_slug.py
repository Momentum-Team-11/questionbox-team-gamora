# Generated by Django 4.0.3 on 2022-04-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_answer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(blank=True, max_length=75, unique=True),
        ),
    ]
