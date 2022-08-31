from django.contrib import admin
from shop.models import Order_update, Product,Contact,Orders

# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(Order_update)