from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class SwitchBoard (models.Model):
    models.CharField(max_length=20)


class Material (models.Model):
    material_name = models.CharField(
        max_length=100, verbose_name="Material Name")
    # material_code = models.IntegerField(verbose_name="Material Code")
    part_number = models.CharField(max_length=100, verbose_name="Part No.")
    unit_of_measure = models.CharField(max_length=10, verbose_name="UoM")
    date_created = models.DateTimeField(default=timezone.now)
    last_edited_by = models.CharField(
        max_length=100, verbose_name="Edited By", blank=True)
    author = models.ForeignKey(
        User, default=1, on_delete=models.CASCADE, verbose_name="Created By")
    
    def __str__(self):
        return self.material_name

    def get_absolute_url(self):
        return reverse('materials-detail', kwargs={'pk': self.pk})

class Issues (model.Models):
    quantity = models.IntegerField()
    issue_date = models.DateTimeField(default=timezone.now)
    requisition_number = models.CharField(max_length=100, verbose_name="Req. No.")
    FK_material = models.ForeignKey(
        Material, default=1, on_delete=models.CASCADE, verbose_name="Material Reference")


class Receipts (model.Models):
    receive_quantity = models.IntegerField()
    issue_date = models.DateTimeField(default=timezone.now)
    PO_number = models.CharField(max_length=100, verbose_name="Receiving Doc. No.")
    FK_material = models.ForeignKey(
        Material, default=1, on_delete=models.CASCADE, verbose_name="Material Reference")



class Stock(models.Model):
    FK_material = models.ForeignKey(
        Material, default=1, on_delete=models.SET_DEFAULT)
    date_updated = models.DateTimeField()
    quantity = models.IntegerField()