from django.contrib import admin
from .models import Stock, StockData


class StockAdmin(admin.ModelAdmin):

    search_fields = ["id", "name", "symbol"]


class StockDataAdmin(admin.ModelAdmin):
    
    readonly_fields = ['last_updated_at']

admin.site.register(Stock, StockAdmin)
admin.site.register(StockData, StockDataAdmin)
