from django.db import models
from django.utils import timezone

class Expense(models.Model):
    image = models.ImageField(default='No Image',upload_to='image/', blank=False, null=True)
    upload_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(default='food',max_length=255)  #花費項目
    price = models.IntegerField(default='1') #金額
    
    def __str__(self):
        return f"{self.name}"