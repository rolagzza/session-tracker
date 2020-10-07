from django.contrib import admin

from .models import SessionAction, SessionActionDetails, SessionLocationDetails, Resolution

admin.autodiscover()


class ResolutionAdmin(admin.ModelAdmin):
    list_display = ('width', 'height')

    fieldsets = (
        (None, {'fields': ['width', 'height']}),
    )

class SessionActionAdmin(admin.ModelAdmin):
    list_display = ('ip', 'resolution')

    fieldsets = (
        (None, {'fields': ['ip', 'resolution']}),
    )


class SessionLocationDetailsAdmin(admin.ModelAdmin):
    list_display = ('longitude', 'latitude', 'city', 'region', 'country', 'country_iso2', 'continent')

    fieldsets = (
        (None, {'fields': ['longitude', 'latitude', 'city', 'region', 'country', 'country_iso2',
                           'continent']}),
    )


class SessionActionDetailsAdmin(admin.ModelAdmin):
    list_display = ('action', 'info', 'location', 'action_date')

    fieldsets = (
        (None, {'fields': ['action', 'info', 'location', 'action_date']}),
    )


admin.site.register(Resolution, ResolutionAdmin)
admin.site.register(SessionAction, SessionActionAdmin)
admin.site.register(SessionLocationDetails, SessionLocationDetailsAdmin)
admin.site.register(SessionActionDetails, SessionActionDetailsAdmin)
