from django.db import models
from trainer.models import Trainer

# Create your models here.
class Module(models.Model):
    module_id = models.AutoField(primary_key=True)
    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE)   
    module_name = models.CharField(max_length=255)
    total_marks = models.IntegerField(null=True) 
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.module_name