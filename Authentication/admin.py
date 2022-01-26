from django.contrib import admin
from Authentication.models import user_detail,providerdetail

# Register your models here.

admin.site.register(user_detail)
admin.site.register(providerdetail)

