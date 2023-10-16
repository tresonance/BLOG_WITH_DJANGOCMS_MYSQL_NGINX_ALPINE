from django.db import models
from django.contrib.auth.models import User  # Pour les utilisateurs (personnel)
from aldryn_categories.fields import CategoryManyToManyField
from cms.models import CMSPlugin
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    cc_name = models.CharField(max_length=200)
    def __str__(self):
        return self.cc_name

class Article(models.Model):
    ca_title = models.CharField(max_length=200, default='Mon titre par défaut')
    # content = models.TextField( default='Contenu par défaut ici.\nContenu par défaut ici\nContenu par défaut ici' )
    # content = RichTextField()
    ca_content = RichTextUploadingField()
    ca_edit_time = models.DateTimeField(auto_now=True)  # Heure d'édition automatique
    # Autres champs relatifs aux articles
    ca_category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Add this field for categories
  

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    cai_article_image = models.ImageField(
        upload_to='images/articles/posts',
        default='images/articles/posts/img1.jpg'  # Spécifiez le chemin de votre image par défaut
    )

class ArticleAuthorImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    caui_author = models.CharField(max_length=200)
    caui_image = models.ImageField(
        upload_to='images/articles/authors',
        default='images/articles/authors/face1.jpg'  # Spécifiez le chemin de votre image par défaut
    )


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilisateur (personnel)
    text = models.TextField( default="Ceci est un commentaire par defaut. Merci vous etes un gros ravailleur. Bon courag." )
    date = models.DateTimeField(auto_now_add=True)  # Date de création automatique
    # Autres champs relatifs aux commentaires

class CommentorImage(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilisateur (personnel)
    image_commentor = models.ImageField(upload_to='images/commentators')  # Champ pour les photos des commentaires
    image_commentor = models.ImageField(
        upload_to='images/commentators',
        default='images/commentators/face3.jpg'  # Spécifiez le chemin de votre image par défaut
    )

# -----------------------------------------------------------------------------
#   CREATE PLUGIN
# ------------------------------------------------------------------------------
# To create a custom plugin , you need class  as below 
# After that, go to my_custom_plugins.py and instanciat it interface there
# Do not forget to fill his tmplate (example templates/blog_plugins/article.html)
class MyArticlePlugin(CMSPlugin):
    article = models.ForeignKey('blog.Article', on_delete=models.CASCADE)
