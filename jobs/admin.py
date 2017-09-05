from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
# Register your models here.
from jobs.models import Job


def make_published(modeladmin, request, queryset):
    queryset.update(published=True)
make_published.short_description = _("设为已发布")


def make_unpublished(modeladmin, request, queryset):
    queryset.update(published=False)
make_unpublished.short_description = _("设为未发布")


class JobAdmin(admin.ModelAdmin):
    list_display = ['company', 'published', 'job_position', 'location', 'department', 'date_published']
    ordering = ['-date_published']
    actions = [make_published, make_unpublished]


admin.site.register(Job, JobAdmin)
