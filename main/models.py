from django.db import models

# Create your models here.

class Sector(models.Model):
    sectorName = models.CharField(max_length=50)
    description = models.TextField()


    def __str__(self):
        return self.sectorName

    class Meta:
        verbose_name = 'sector'
        verbose_name_plural = 'sectors'

class Service(models.Model):
    serviceName = models.CharField(max_length=50)
    sector = models.ForeignKey("Sector", on_delete=models.CASCADE)

    def __str__(self):
        return self.serviceName

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
