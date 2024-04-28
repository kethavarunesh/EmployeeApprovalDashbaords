
from django.db import models
from datetime import datetime
class Mtplnew_dataentry(models.Model):
    NC_CHOICES=[
        ('yes','yes'),
        ('no','no')
    ]
    empcode = models.CharField(max_length=20)
    project_name = models.CharField(max_length=100)
    date = models.DateField(default=datetime.now)
    document_no = models.CharField(max_length=50)
    order_serial_no = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    material_code = models.CharField(max_length=50)
    material_description = models.TextField()
    supplier_name = models.CharField(max_length=100)
    qty = models.CharField(max_length=1000)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    rejection_reason = models.CharField(max_length=50)
    reason_for_rejection = models.TextField()
    file_upload = models.FileField(upload_to='uploads/')
    man_hours_wasted = models.DecimalField(max_digits=5, decimal_places=5)
    machine_hours_wasted = models.DecimalField(max_digits=5, decimal_places=5)
    information_to_buyer = models.CharField(max_length=100)
    status = models.IntegerField(default=0)  
    approval_comment = models.CharField(max_length=100)
    ncraised = models.CharField(max_length=10, choices=NC_CHOICES)
    purchase_remarks=models.CharField(max_length=100)
    planthod_remarks=models.CharField(max_length=100)
    def __str__(self):
        return self.document_no

 
