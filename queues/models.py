from django.db import models
class QueueEntery(models.Model):
    STATUS_CHOICES= [
        ('Waiting','Waiting'),
        ('Serving','Serving'),
        ('Completed','Completed'),
    ]
    customer_name= models.CharField(max_length=100)
    service_types= models.CharField(max_length=100)
    status= models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Waiting'
    )
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.customer_name