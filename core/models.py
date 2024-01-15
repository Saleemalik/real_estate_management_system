from django.db import models

# Create your models here.





#Property Details: Create property profile with information like Property name and address, location, features. 
class Property(models.Model):
    name = models.CharField(max_length=25)
    address = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    property_view = models.ImageField(upload_to='images/', blank=True, null=True)



    def __str__(self) -> str:
        return f'{self.name}'



class Unit(models.Model):
    rent_cost = models.FloatField(blank=True, null=True)
    type_choices = (
        (1,'1BHK'),
        (2,'2BHK'),
        (3,'3BHK'),
        (4,'4BHK'),
    )
    unit_type = models.CharField(max_length=10, choices=type_choices, blank=True, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey('Tenant', on_delete=models.CASCADE, blank=True, null=True )
    unit_view = models.ImageField(upload_to='untits/', blank=True, null=True)
    monthly_rent_date = models.DateField(blank=True, null=True)
    agreement_end_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.property} with {self.unit_type}'



class Tenant(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    tenant_view = models.ImageField(upload_to='tenants/', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'



class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.file.name}'
    
