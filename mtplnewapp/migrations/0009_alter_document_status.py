# Generated by Django 5.0.3 on 2024-04-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtplnewapp', '0008_alter_document_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
