from django.contrib import admin
from stocks.models import Stocks, DefinitionTerms
# Register your models here.

admin.site.register(Stocks)
admin.site.register(DefinitionTerms)
