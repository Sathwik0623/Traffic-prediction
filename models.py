from django.db import models

# Create your models here.
class storetrafficdata(models.Model):
    Date=models.CharField(max_length=150)
    Day=models.CharField(max_length=100)
    CodedDay=models.CharField(max_length=100)
    Zone=models.CharField(max_length=100)
    Weather=models.CharField(max_length=100)
    Temperature=models.CharField(max_length=100)
    Traffic=models.CharField(max_length=100)

    def __str__(self):
        return self.Date, self.Day, self.CodedDay, self.Zone, self.Weather, self.Temperature, self.Traffic

    class Meta:
        db_table = 'storetrafficdata'

class userModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=40)
    cwpasswd = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=50, default="", editable=True)
    status = models.CharField(max_length=40, default="", editable=True)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='userregister'

