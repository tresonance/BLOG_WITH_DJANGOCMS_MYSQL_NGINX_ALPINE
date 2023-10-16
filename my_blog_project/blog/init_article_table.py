import os
import django

# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_blog_project.settings")
django.setup()

# We impor cms category table 
#from aldryn_categories.models import Category

# We import our custom table
from blog.models import Article, ArticleImage, ArticleAuthorImage, Comment, CommentorImage, Category
from datetime import datetime


# Create top-level categories
'''
category1 = Category.objects.create(name='Maths', slug='maths')
category2 = Category.objects.create(name='Physics', slug='physics')
category3 = Category.objects.create(name='C-Language', slug='c-language')
category4 = Category.objects.create(name='Big Data', slug='big-data')

# Create subcategories with a parent
subcategory1 = Category.objects.create(name='Algèbre', slug='algebre', parent=category1)
subcategory2 = Category.objects.create(name='Geometrie', slug='geometrie', parent=category1)
subcategory3 = Category.objects.create(name='Analyse', slug='analyse', parent=category1)
subcategory3 = Category.objects.create(name='Probabilités et Statistiques', slug='probabilite-stat', parent=category1)
'''

# category 
category_data = [
    {
        "name": "Maths",
    },
    {
        "name": "Physique",
    },
    {
        "name": "Big-Data",
    },
    {
        "name": "C-Language",
    },
]
# Insert category
for data in category_data:
    Category.objects.create(
        cc_name=data["name"]
    )

# Les données pour les articles
article_data = [
    {
        "title": "Titre de l'article 1 - whodunit tooltip",
        "content": "Contenu long de l'article 1...\nPlus de texte...",
        "edit_time": datetime.now(),
        "category_instance" : Category.objects.get(pk=1),
        #"categories": [category1, subcategory1]
    },
    {
        "title": "Titre de l'article 2 - whodunit tooltip",
        "content": "Contenu long de l'article 2...\nPlus de texte...",
        "edit_time": datetime.now(),
        "category_instance" : Category.objects.get(pk=2),
        #"categories": [category1, subcategory1]
    },
    {
        "title": "Titre de l'article 3 - whodunit tooltip",
        "content": "Contenu long de l'article 3...\nPlus de texte...",
        "edit_time": datetime.now(),
        "category_instance" : Category.objects.get(pk=3),
        #"categories": [category1, subcategory1]
    },
    {
        "title": "Titre de l'article 4 - whodunit tooltip",
        "content": "Contenu long de l'article 4...\nPlus de texte...",
        "edit_time": datetime.now(),
        "category_instance" : Category.objects.get(pk=4),
        #"categories": [category1, subcategory1]
    },
    {
        "title": "Titre de l'article 5 - whodunit tooltip",
        "content": "Contenu long de l'article 5...\nPlus de texte...",
        "edit_time": datetime.now(),
        "category_instance" : Category.objects.get(pk=1),
        #"categories": [category1, subcategory1]
    },
    {
        "title": "Titre de l'article 6 - whodunit tooltip",
        "content": "Contenu long de l'article 6...\nPlus de texte...",
        "edit_time": datetime.now(),
        "category_instance" : Category.objects.get(pk=2),
        #"categories": [category1, subcategory1]
    },
    {
        "title": "Titre de l'article 7 - whodunit tooltip",
        "content": "Contenu long de l'article 7...\nPlus de texte...",
        "edit_time": datetime.now(),
        "category_instance" : Category.objects.get(pk=3),
        #"categories": [category1, subcategory1]
    },
    {
        "title": "Titre de l'article 8 - whodunit tooltip",
        "content": "Contenu long de l'article 8...\nPlus de texte...",
        "edit_time": datetime.now(),
        "category_instance" : Category.objects.get(pk=4),
        #"categories": [category1, subcategory1]
    },
    {
        "title": "Titre de l'article 9 - whodunit tooltip",
        "content": "Contenu long de l'article 9...\nPlus de texte...",
        "edit_time": datetime.now(),
        "category_instance" : Category.objects.get(pk=1),
        #"categories": [category1, subcategory1]
    },
]

# Insérer les données dans la table Article
for data in article_data:
    Article.objects.create(
        ca_title=data["title"],
        ca_content=data["content"],
        ca_edit_time=data["edit_time"],
        ca_category=data["category_instance"],
        #categories=data["categories"],
    )


article_images_data = [
    {
        "article_instance" : Article.objects.get(pk=1),
        "image_article": "images/articles/posts/img1.jpg",
    },

    {
        "article_instance" : Article.objects.get(pk=2),
        "image_article": "images/articles/posts/img2.jpg",
    },

    {
        "article_instance" : Article.objects.get(pk=3),
        "image_article": "images/articles/posts/img3.jpg",
    },

    {
        "article_instance" : Article.objects.get(pk=4),
        "image_article": "images/articles/posts/img4.jpg",
    },

    {
         "article_instance" : Article.objects.get(pk=5),
        "image_article": "images/articles/posts/img5.jpg",
    },

    {
        "article_instance" : Article.objects.get(pk=6),
        "image_article": "images/articles/posts/img6.jpg",
    },

    {
        "article_instance" : Article.objects.get(pk=7),
        "image_article": "images/articles/posts/img7.jpg",
    },

    {
        "article_instance" : Article.objects.get(pk=8),
        "image_article": "images/articles/posts/img8.jpg",
    },

    {
         "article_instance" : Article.objects.get(pk=9),
        "image_article": "images/articles/posts/img9.jpg",
    },
]

# Insérer les données dans la table ArticleImage
for data in article_images_data:
    ArticleImage.objects.create(
        article=data["article_instance"],
        cai_article_image=data["image_article"],
    )


article_author_images_data = [
    {
        "article_instance" : Article.objects.get(pk=1),
        "image_article_author": "images/articles/authors/face1.jpg",
        "author": "Ibrahimadev"
    },

     {
         "article_instance" : Article.objects.get(pk=2),
        "image_article_author": "images/articles/authors/face2.jpg",
         "author": "Ibrahimadev"
    },

     {
        "article_instance" : Article.objects.get(pk=3),
        "image_article_author": "images/articles/authors/face3.jpg",
        "author": "Ibrahimadev"
    },

     {
        "article_instance" : Article.objects.get(pk=1),
        "image_article_author": "images/articles/authors/face1.jpg",
        "author": "Ibrahimadev"
    },

     {
        "article_instance" : Article.objects.get(pk=2),
        "image_article_author": "images/articles/authors/face2.jpg",
        "author": "Ibrahimadev"
    },

     {
        "article_instance" : Article.objects.get(pk=3),
        "image_article_author": "images/articles/authors/face3.jpg",
        "author": "Ibrahimadev"
    },

     {
        "article_instance" : Article.objects.get(pk=1),
        "image_article_author": "images/articles/authors/face1.jpg",
        "author": "Ibrahimadev"
    },

     {
        "article_instance" : Article.objects.get(pk=2),
        "image_article_author": "images/articles/authors/face2.jpg",
        "author": "Ibrahimadev"
    },

     {
        "article_instance" : Article.objects.get(pk=3),
        "image_article_author": "images/articles/authors/face3.jpg",
        "author": "Ibrahimadev"
    },
]


# Insérer les données dans la table ArticleImage
for data in article_author_images_data:
    ArticleAuthorImage.objects.create(
        article=data["article_instance"],
        caui_image=data["image_article_author"],
        caui_author=data["author"]
    )



Comment_data = [

    {
        "article_instance" : Article.objects.get(pk=3),
        "text" : Article.objects.get(pk=1),
        "date": "images/articles/authors/face1.jpg",
    },

]

print("Données insérées avec succès dans la table Article.")