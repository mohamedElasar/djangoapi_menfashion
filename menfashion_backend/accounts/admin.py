from django.contrib import admin
from accounts import models

# Register your models here.


# class UserInline(admin.TabularInline):
#     model = models.User
#     readonly_fields=('id',)


class UserAdmin(admin.ModelAdmin):
      readonly_fields = ('id',)
      admin.site.register(models.User)
