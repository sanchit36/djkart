from django.db import models


class Currency(models.Model):
    symbol = models.CharField(max_length=5)
    code = models.CharField(max_length=5)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.symbol
