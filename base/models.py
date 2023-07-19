from django.db import models

# Create your models here.

class Data(models.Model):
    age=models.PositiveIntegerField(null=True)
    blood_pressure=models.PositiveIntegerField()
    specific_gravity=models.FloatField()
    albumin=models.FloatField()
    sugar=models.PositiveIntegerField()
    rbc=models.PositiveIntegerField()
    pus=models.PositiveIntegerField()
    pus_clumps=models.PositiveIntegerField()
    bacteria=models.PositiveIntegerField()
    blood_glucose=models.PositiveIntegerField()
    blood_urea=models.FloatField()
    serum_creatinine=models.FloatField()
    sodium=models.FloatField()
    potassium=models.FloatField()
    haemoglobin=models.FloatField()
    packed_cell_volume=models.PositiveIntegerField()
    wbc_count=models.PositiveIntegerField()
    rbc_count=models.PositiveIntegerField()
    hypertension=models.PositiveIntegerField()
    diabetes_mellitus=models.PositiveIntegerField()
    coronary_artery_disease=models.PositiveIntegerField()
    appetite=models.PositiveIntegerField()
    peda_edema=models.PositiveIntegerField()
    anemia=models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
    
    
