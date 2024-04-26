# Generated by Django 5.0.3 on 2024-04-25 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mtplnewapp', '0022_delete_mtplnew_dataentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mtplnew_dataentry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empcode', models.CharField(max_length=20)),
                ('project_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('document_no', models.CharField(max_length=50, unique=True)),
                ('order_serial_no', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=100)),
                ('material_code', models.CharField(max_length=50)),
                ('material_description', models.TextField()),
                ('supplier_name', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rejection_reason', models.CharField(max_length=50)),
                ('reason_for_rejection', models.TextField()),
                ('file_upload', models.FileField(upload_to='uploads/')),
                ('man_hours_wasted', models.DecimalField(decimal_places=5, max_digits=5)),
                ('machine_hours_wasted', models.DecimalField(decimal_places=5, max_digits=5)),
                ('information_to_buyer', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=0)),
                ('approval_comment', models.CharField(max_length=100)),
                ('nc_raised', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('remarks', models.CharField(max_length=100)),
            ],
        ),
    ]
