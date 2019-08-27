from django.db import models

class Callback(models.Model):
  device = models.CharField(max_length=100)
  snr = models.DecimalField(max_digits=6, decimal_places=4)
  data = models.CharField(max_length=150)
  time = models.CharField(max_length=100)

  def __str__(self):
    return self.name