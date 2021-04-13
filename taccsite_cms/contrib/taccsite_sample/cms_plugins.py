from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_text

from .models import TaccsiteSample

from .defaults import name as default_name

@plugin_pool.register_plugin
class TaccsiteSamplePlugin(CMSPluginBase):
    """
    Components > "Sample (Greet User)" Plugin
    https://url.to/docs/components/sample/
    """
    module = 'TACC Site'
    model = TaccsiteSample
    name = _('Sample (Greet User)')
    render_template = 'sample.html'

    cache = False
    text_enabled = True

    # FAQ: Sets tooltip of preview of this plugin within a Text plugin
    def icon_alt(self, instance):
        super_value = force_text(super().icon_alt(instance))
        name = self.get_name(instance)
        return f'Hello, {{{name}}} [{super_value}]'

    # Helpers

    def get_name(self, instance, user=None):
        """Get name of authenticated user or the name for any guest."""

        if user and user.is_authenticated:
            name = user.first_name + ' ' + user.last_name
        elif bool(instance.guest_name):
            name = instance.guest_name
        else:
            name = default_name

        return name

    # Render

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        context.update({
            'user_name': self.get_name(instance, request.user)
        })
        return context
