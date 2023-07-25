# Django
from django.contrib import admin
from apps.usuarios.models import Usuario


from apps.usuarios.models import AdminProfile


@admin.register(AdminProfile)


class AdminProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'user', 'photo')
    list_display_links = ('pk', 'user',)
    list_editable = ('photo',)

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'user__is_superuser',
        'date_modified',
    )

    fieldsets = (
        ('AdminProfile', {
            'fields': (('user', 'photo'),),
        }),
        ('Extra info', {
            'fields': (('date_modified'),),
        })
    )

    readonly_fields = ('date_modified',)


class ProfileInline(admin.StackedInline):

    model = AdminProfile
    can_delete = False
    verbose_name_plural = 'administradores'

