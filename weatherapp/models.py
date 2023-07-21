from django.db import models

class Forecast(models.Model):
    date = models.CharField(max_length=255)
    condition = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.date + ' | ' + self.condition + ' | ' + self.state + ' | ' + str(self.city)
    
    
