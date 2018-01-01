from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
	list_display = ['user', 'id', 'drop_out', 'paid', 'delivered_on','if_return', 'if_exchange', 'cashback', 'exchanged']
	list_filter = ['paid', 'if_return', 'if_exchange', 'created', 'updated']
	list_editable = ['paid', 'delivered_on', 'cashback', 'exchanged']
	search_fields = ('id', 'user__username')
admin.site.register(Order, OrderAdmin)