from django.db import models


class Hospital(models.Model):
    Hospital_id = models.IntegerField(
    primary_key=True, unique=True, null=False, blank=False)
    Hospital_name = models.CharField(max_length=100, default='')

    def __str__(self):
        x = str(self.Hospital_id)
        return x 


class Dept(models.Model):
    class Meta:
        unique_together = (('Uid', 'Hospital_id'),)

    Uid = models.IntegerField()
    Type = models.CharField(max_length=20, default='')
    Hospital_id = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, default='null')

    def __str__(self):
        return self.Type