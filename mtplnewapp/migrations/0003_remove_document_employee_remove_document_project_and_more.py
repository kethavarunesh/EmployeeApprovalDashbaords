# Generated by Django 5.0.3 on 2024-04-21 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtplnewapp', '0002_document_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='document',
            name='project',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
