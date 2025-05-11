from django.db import models
from django.utils import timezone

# Create your models here.
class chai(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    data_added = models.DateTimeField(default=timezone.now)

    CHAI_TYPE_CHOICE = [
        ('ML','MASALA'),
        ('PL','PLAIN'),
        ('GR','GINGER'),
        ('EL','ELACHI'),
        ('KL','KIWI')
    ]

    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)

    def __str__(self):
        return self.name
