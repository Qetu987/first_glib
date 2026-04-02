from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from client.models import User, Task


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'phone', 'birth_date', 'is_staff', 'is_active', 'date_joined',)
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'groups', 'date_joined')
    list_editable = ('is_active', 'is_staff')
    ordering = ('-date_joined',)
    list_per_page = 25

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'bio',
                'phone',
                'birth_date',
            )
        }),
        ('Access rights', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'phone',
            ),
        }),
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'due_date', 'completed_at', 'created_at', 'updated_at')
    search_fields = ('id', 'title')
    list_filter = ('due_date', 'completed_at', 'created_at', 'updated_at')
    ordering = ('-due_date',)
