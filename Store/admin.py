from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Size_categorie)
admin.site.register(Size)
admin.site.register(Sale)
# admin.site.register(Cart)