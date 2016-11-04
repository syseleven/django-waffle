from __future__ import unicode_literals

from django.contrib import admin

from waffle.models import Flag, Sample, Switch


class BaseAdmin(admin.ModelAdmin):
    def get_actions(self, request):
        actions = super(BaseAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


def enable_for_all(ma, request, qs):
    # Iterate over all objects to cause cache invalidation.
    for f in qs.all():
        f.everyone = True
        f.save()
enable_for_all.short_description = 'Enable selected flags for everyone.'


def disable_for_all(ma, request, qs):
    # Iterate over all objects to cause cache invalidation.
    for f in qs.all():
        f.everyone = False
        f.save()
disable_for_all.short_description = 'Disable selected flags for everyone.'


def delete_individually(ma, request, qs):
    # Iterate over all objects to cause cache invalidation.
    for f in qs.all():
        f.delete()
delete_individually.short_description = 'Delete selected.'


class FlagAdmin(BaseAdmin):
    actions = [enable_for_all, disable_for_all, delete_individually]
    list_display = ('name', 'note', 'everyone', 'percent', 'superusers',
                    'staff', 'authenticated', 'languages')
    list_filter = ('everyone', 'superusers', 'staff', 'authenticated', 'groups')
    ordering = ('-id',)


def enable_switches(ma, request, qs):
    for switch in qs:
        switch.active = True
        switch.save()
enable_switches.short_description = 'Enable the selected switches.'


def disable_switches(ma, request, qs):
    for switch in qs:
        switch.active = False
        switch.save()
disable_switches.short_description = 'Disable the selected switches.'


class SwitchAdmin(BaseAdmin):
    actions = [enable_switches, disable_switches, delete_individually]
    list_display = ('name', 'active', 'note', 'created', 'modified')
    list_filter = ('active',)
    ordering = ('-id',)


class SampleAdmin(BaseAdmin):
    actions = [delete_individually]
    list_display = ('name', 'percent', 'note', 'created', 'modified')
    ordering = ('-id',)


admin.site.register(Flag, FlagAdmin)
admin.site.register(Sample, SampleAdmin)
admin.site.register(Switch, SwitchAdmin)
