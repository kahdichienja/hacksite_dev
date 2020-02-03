from django.db import models

# Create your models here.

class Autogen(models.Model):
    student_full_name = models.CharField(max_length = 191)
    adm_number = models.CharField(max_length = 191)
    exam_card_number = models.CharField(max_length = 6)
    fee = models.BooleanField(default = True, null=True)    
    def __str__(self):
        return f'{self.student_full_name}:{self.adm_number}'