from django.db import models


# Create your models here.

class Trip(models.Model):
    station_name = models.CharField('车站名称', max_length=20, db_index=True)
    station_code = models.CharField('车站名称', max_length=20, db_index=True)

    def __str__(self):
        return f'车站名称:{self.station_name},车站代码:{self.station_code}'
   