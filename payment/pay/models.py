from django.db import models

# Create your models here.

class Payment(models.Model):
    operation_id = models.CharField(primary_key=True, max_length=200)
    amount = models.IntegerField()
    payer_inn = models.CharField(max_length=200)
    document_number = models.CharField(max_length=200)
    document_date = models.DateTimeField()

class BalanceOrganizations(models.Model):
    inn = models.CharField(max_length=200)
    balance = models.IntegerField()
