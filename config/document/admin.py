from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.unregister(Group)

# Foydalanuvchilar
class MainUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']
admin.site.register(MainUser, MainUserAdmin)

# fanlar
class FanlarAdmin(admin.ModelAdmin):
    list_display = ['name', 'pk']
admin.site.register(Fanlar, FanlarAdmin)

# Kategoriyalar
class KategoriyaAdmin(admin.ModelAdmin):
    list_display = ['name', 'pk']
admin.site.register(Kategoriya, KategoriyaAdmin)

# Yuklanmalar
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'file', 'fan', 'category', 'pk']
admin.site.register(DocumentFile, DocumentAdmin)


