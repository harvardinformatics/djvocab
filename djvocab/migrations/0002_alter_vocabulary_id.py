# Generated by Django 3.2.18 on 2023-03-31 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djvocab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabulary',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
