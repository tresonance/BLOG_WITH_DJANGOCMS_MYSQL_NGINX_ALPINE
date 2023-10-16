from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

# this scrips include the blog application to cms , this is why w remove 
# th line re_path(r'^blog/', include('blog.urls', namespace='blog')) to the project urls.py

@apphook_pool.register  # register the application
class BlogApphook(CMSApp):
    app_name = "blog"
    name = "Blog Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["blog.urls"]