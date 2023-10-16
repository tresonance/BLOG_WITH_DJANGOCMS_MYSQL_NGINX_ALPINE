from django.apps import AppConfig

# Here we can set the name we want to give to our application inside admin panel
# So my application "blog" will be called IBRA_BLOG inside admin panl

class MyBlogAppConfig(AppConfig):
    #default_auto_field = 'django.db.models.BigAutoField'
    #name = 'my_blog_app'
    name = 'blog'
    verbose_name = "IBRA_BLOG"
