from django.db import models

# Create your models here.

class Categorie(models.Model):
    categorie = models.CharField(max_length=50)
    essential = models.BooleanField(default=False)
    planning_value = models.FloatField(default=0)

    def __str__(self):
        return self.categorie

class Wallet(models.Model):
    bank_choices = (
        ('NU', 'Nubank'),
        ('BB', 'Banco do Brasil'),
    )

    type_choices = (
        ('P', 'Personal'),
        ('C', 'Company'),
    )

    name = models.CharField(max_length=50)
    bank = models.CharField(max_length=2, choices=bank_choices)
    wallet_type = models.CharField(max_length=2, choices=type_choices)
    value = models.FloatField()

    def __str__(self):
        return self.name
