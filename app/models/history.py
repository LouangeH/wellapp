from django.db import models
from models.finance import Finance

class History_Finance(models.Model):
    finance = models.ForeignKey(Finance, on_delete=models.CASCADE)
    somme = models.FloatField()
    date_set = models.DateTimeField(auto_now_add=True)