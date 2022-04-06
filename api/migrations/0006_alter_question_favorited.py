# Generated by Django 4.0.3 on 2022-04-06 17:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_question_answer_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='favorited',
            field=models.ManyToManyField(blank=True, related_name='favorite_question', to=settings.AUTH_USER_MODEL),
        ),
    ]
