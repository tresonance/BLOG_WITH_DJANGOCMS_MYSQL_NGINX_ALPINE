from django.db import models
from django.contrib.auth.models import User  # Pour les utilisateurs (personnel)

class Article(models.Model):
    title = models.CharField(max_length=200, default='Mon titre par défaut')
    content = models.TextField( default='Contenu par défaut ici.\nContenu par défaut ici\nContenu par défaut ici' )
    edit_time = models.DateTimeField(auto_now=True)  # Heure d'édition automatique
    # Autres champs relatifs aux articles
  

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image_article = models.ImageField(
        upload_to='images/articles/posts',
        default='images/articles/posts/img1.jpg'  # Spécifiez le chemin de votre image par défaut
    )

class ArticleAuthorImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image_article_author = models.ImageField(
        upload_to='images/articles/authors',
        default='images/articles/authors/face1.jpg'  # Spécifiez le chemin de votre image par défaut
    )


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilisateur (personnel)
    text = models.TextField( default="Ceci est un commentaire par defaut. Merci vous etes un gros ravailleur. Bon courag." )
    date = models.DateTimeField(auto_now_add=True)  # Date de création automatique
    # Autres champs relatifs aux commentaires

class CommentorImage(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilisateur (personnel)
    image_commentor = models.ImageField(upload_to='images/commentators')  # Champ pour les photos des commentaires
    image_commentor = models.ImageField(
        upload_to='images/commentators',
        default='images/commentators/face3.jpg'  # Spécifiez le chemin de votre image par défaut
    )

