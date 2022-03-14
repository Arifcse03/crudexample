
from django.db import models


class Khawadawa(models.Model):
    id = models.FloatField(primary_key=True)
    item_name = models.CharField(max_length=1000, blank=True, null=True)
    person_will_feed = models.CharField(max_length=100, blank=True, null=True)
    program_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KhawaDawa'