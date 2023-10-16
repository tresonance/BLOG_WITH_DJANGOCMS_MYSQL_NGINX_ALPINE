# my_custom_plugin.py

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import MyArticlePlugin

# this script is to create plugin and link it to a model. It register the created blog

@plugin_pool.register_plugin
class MyArticlePluginRenderer(CMSPluginBase):
    model = MyArticlePlugin
    name = _("My Article Plugin")
    render_template = "base.html"  # Specify your template
    cache = False
    allow_children = True

    def render(self, context, instance, placeholder):
        # Add logic here to render your plugin's content
        # context['instance'] = instance
        context = super(MyArticlePluginRenderer, self).render(context, instance, placeholder)
        return context

#plugin_pool.register_plugin(MyArticlePluginRenderer)
