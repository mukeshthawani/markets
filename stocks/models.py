from django.db import models


class Stocks(models.Model):
    symbol = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.symbol


class DefinitionTerms(models.Model):
    terms = models.CharField(max_length=50, unique=True)
    full_terms = models.CharField(max_length=50)

    def __unicode__(self):
        return self.terms

