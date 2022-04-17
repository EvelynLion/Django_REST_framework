from django.db import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class HotelInfo(models.Model):
    hotel_id = models.CharField(max_length=50, verbose_name='Hotel ID', primary_key=True)
    hotel_name = models.CharField(max_length=200, verbose_name='Hotel Name')
    price = models.FloatField(verbose_name='Price')
    is_delete = models.BooleanField(default=False, verbose_name='Logical Delete')

    class Meta:
        db_table = 'tb_hotel'
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'

    def __str__(self):
        return self.hotel_name
