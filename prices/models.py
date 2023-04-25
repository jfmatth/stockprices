from django.db import models

#===============================================================================
# Symbol - Stock Symbol
#===============================================================================
class Symbol(models.Model):
    name        = models.CharField(max_length=10, db_index=True, unique=True, blank=False, null=False)
    description = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.name} - {self.description}"
    
#===============================================================================
# Price - Stock price 1-N back to Symbol
#===============================================================================
class Price(models.Model):

    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE)

    date   = models.DateField(db_index=True, blank=False)
    high   = models.DecimalField(max_digits=12, decimal_places=3, blank=False)
    low    = models.DecimalField(max_digits=12, decimal_places=3, blank=False)
    close  = models.DecimalField(max_digits=12, decimal_places=3, blank=False)
    volume = models.IntegerField(blank=False)
    
    def __str__(self):
        return f"{self.symbol} - {self.date} - {self.close}"
        return "%s %s %s" % (self.symbol.name, self.date, self.close)

#----------------
# download - Which symbols to download each run
#----------------
class Download(models.Model):
    symbol = models.CharField(max_length=10, db_index=True, unique=True, blank=False, null=False)

    def __str__(self):
        return f"{self.symbol}"