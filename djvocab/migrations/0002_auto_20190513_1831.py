# Generated by Django 2.1.7 on 2019-05-13 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djvocab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabulary',
            name='value',
            field=models.CharField(max_length=200),
        ),
    ]
