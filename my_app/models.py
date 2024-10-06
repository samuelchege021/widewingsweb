from django.db import models

from django .contrib.auth.models import User
# Create your models here.





from django.db import models

class Plumbing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='plumbing_images/', blank=True, null=True)
    pub_date = models.DateField()

    def __str__(self):
        return self.name

class Biodigester(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='biodigester_images/', blank=True, null=True)
    pub_date = models.DateField()

    def __str__(self):
        return self.name

class WaterTreatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='water_treatment_images/', blank=True, null=True)
    pub_date = models.DateField()

    def __str__(self):
        return self.name

class SolarInstallation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='solar_installation_images/', blank=True, null=True)
    pub_date = models.DateField()

    def __str__(self):
        return self.name
    
    
    
    from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email}) on {self.date_sent}"

