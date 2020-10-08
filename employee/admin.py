from django.contrib import admin
from .models import Department, DmsUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm


# Register your models here.
admin.site.register(Department)


class DmsUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = DmsUser

class DmsUserAdmin(UserAdmin):
    form = DmsUserChangeForm
    filter_horizontal = ('department', 'groups', 'user_permissions')

    fieldsets = UserAdmin.fieldsets + (
            ('Departments & Roles', {'fields': ('department', 'reviewer', 'approver')}),
    )


admin.site.register(DmsUser, DmsUserAdmin)
