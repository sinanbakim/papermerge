# Generated by Django 3.0.10 on 2020-10-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_remove_document_file_orig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]