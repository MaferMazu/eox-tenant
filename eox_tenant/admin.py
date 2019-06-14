"""
Django admin page for microsite model
"""
from django.contrib import admin

from eox_tenant.models import Redirection, Microsite, TenantConfig


class MicrositeAdmin(admin.ModelAdmin):
    """
    TODO: add me
    """
    list_display = [
        'key',
        'subdomain',
        'sitename',
        'template_dir',
        'course_org_filter',
        'ednx_signal',
    ]
    readonly_fields = (
        'sitename',
        'template_dir',
        'course_org_filter',
        'ednx_signal',
    )
    search_fields = ('key', 'subdomain', 'values', )

    def sitename(self, microsite):
        """
        TODO: add me
        """
        # pylint: disable=broad-except
        try:
            return microsite.values.get('SITE_NAME', "NOT CONFIGURED")
        except Exception as error:
            return str(error)

    def template_dir(self, microsite):
        """
        TODO: add me
        """
        # pylint: disable=broad-except
        try:
            return microsite.values.get('template_dir', "NOT CONFIGURED")
        except Exception as error:
            return str(error)

    def course_org_filter(self, microsite):
        """
        TODO: add me
        """
        # pylint: disable=broad-except
        try:
            return microsite.values.get('course_org_filter', "NOT CONFIGURED")
        except Exception as error:
            return str(error)

    def ednx_signal(self, microsite):
        """
        Read only method to see if the site has activated the usage of signals
        """
        # pylint: disable=broad-except
        try:
            return microsite.values.get('EDNX_USE_SIGNAL', "EMPTY")
        except Exception as error:
            return str(error)


class TenantConfigAdmin(admin.ModelAdmin):
    """
    Tenant config model admin
    """
    list_display = [
        'external_key',
        'domain',
        'sitename',
        'template_dir',
        'course_org_filter',
        'ednx_signal',
    ]
    readonly_fields = (
        'sitename',
        'template_dir',
        'course_org_filter',
        'ednx_signal',
    )
    search_fields = ('key', 'route__domain', 'lms_configs', )

    def sitename(self, tenant_config):
        """
        Read only method to calculate sitename attribute from config model.
        """
        # pylint: disable=broad-except
        try:
            return tenant_config.lms_configs.get('SITE_NAME', "NOT CONFIGURED")
        except Exception as error:
            return str(error)

    def template_dir(self, tenant_config):
        """
        Read only method to calculate template dir attribute from config model.
        """
        # pylint: disable=broad-except
        try:
            return tenant_config.lms_configs.get('template_dir', "NOT CONFIGURED")
        except Exception as error:
            return str(error)

    def course_org_filter(self, tenant_config):
        """
        Read only method to calculate course org filter attribute from config model.
        """
        # pylint: disable=broad-except
        try:
            return tenant_config.lms_configs.get('course_org_filter', "NOT CONFIGURED")
        except Exception as error:
            return str(error)

    def ednx_signal(self, tenant_config):
        """
        Read only method to see if the site has activated the usage of signals.
        """
        # pylint: disable=broad-except
        try:
            return tenant_config.lms_configs.get('EDNX_USE_SIGNAL', "EMPTY")
        except Exception as error:
            return str(error)

    def domain(self, tenant_config):
        """
        Read only method to calculate the domain.
        """
        # pylint: disable=broad-except
        try:
            domains = [route.domain for route in tenant_config.route_set.all()]
            separator = '\n'
            return separator.join(domains)
        except Exception as error:
            return str(error)


class RedirectionAdmin(admin.ModelAdmin):
    """
    Admin view to see and edit edunext redirection objects.
    """
    list_display = [
        'target',
        'domain',
        'scheme',
    ]
    search_fields = ('target', 'domain',)


admin.site.register(Microsite, MicrositeAdmin)
admin.site.register(TenantConfig, TenantConfigAdmin)
admin.site.register(Redirection, RedirectionAdmin)
