from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


admin.site.register(User, UserAdmin)


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'photo', 'date_birth')
#     list_display_links = ('id', 'username')
