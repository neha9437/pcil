from django.contrib import admin
from .models import pcil_products,pcil_cities,product_requisition

admin.site.register(pcil_products)
admin.site.register(pcil_cities)
admin.site.register(product_requisition)