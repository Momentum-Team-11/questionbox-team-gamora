# Generated by Django 4.0.3 on 2022-04-11 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_answer_favorited'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='accepted',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accepted', to='api.question'),
        ),
    ]
