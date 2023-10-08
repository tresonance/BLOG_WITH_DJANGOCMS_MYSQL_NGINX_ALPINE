from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, ArticleImage, ArticleAuthorImage, Comment, CommentorImage
from .forms import CommentForm, CommentorImageForm

# Vue pour afficher la liste des articles
def article_list(request):
    #articles = Article.objects.all()
    #print("FROM VIEWS: ", articles)
    #return render(request, 'blogpage.html', {'articles': articles})
    template_name = 'my_blog_app/templates/blogpage.html'
    context_object_name = 'latest_blog_list'

    def get_queryset(self):
        return Article.objects.all()

# Vue pour afficher un article individuel
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    images = ArticleImage.objects.filter(article=article)
    author_images = ArticleAuthorImage.objects.filter(article=article)
    comments = Comment.objects.filter(article=article)
    return render(request, 'article_detail.html', {'article': article, 'images': images, 'author_images': author_images, 'comments': comments})

# Vue pour ajouter un commentaire à un article
def add_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user  # Utilisateur actuel
            comment.save()
            return redirect('article_detail', article_id=article_id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'article': article})

# Vue pour ajouter une image à un commentaire
def add_commentor_image(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = CommentorImageForm(request.POST, request.FILES)
        if form.is_valid():
            commentor_image = form.save(commit=False)
            commentor_image.comment = comment
            commentor_image.user = request.user  # Utilisateur actuel
            commentor_image.save()
            return redirect('article_detail', article_id=comment.article.id)
    else:
        form = CommentorImageForm()
    return render(request, 'add_commentor_image.html', {'form': form, 'comment': comment})
