from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Article, ArticleImage, ArticleAuthorImage, Comment, CommentorImage
from .forms import CommentForm, CommentorImageForm

# Vue pour afficher la liste des articles
def article_list(request):
    articles = Article.objects.all()
    articles_images = ArticleImage.objects.all()
    articles_comments = Comment.objects.all()

    # Combine articles and images into a list of dictionaries
    combined_data = [{'article': article, 'image': image} for article, image in zip(articles, articles_images)]

    #print("FROM VIEWS: ", articles)
    return render(request, 'base.html', {
        'combined_data': combined_data,
        'articles_comment_total': len(articles_comments)
        }
    )
   

def articles_with_chosen_category(request, chosen_category_name):
   
    chosen_articles = Article.objects.filter(ca_category__cc_name=chosen_category_name)
    chosen_articles_images = ArticleImage.objects.filter(article__in=chosen_articles)
    chosen_articles_comments = Comment.objects.filter(article__in=chosen_articles)

    print("\n=======> chosen_category_name: ", chosen_category_name)
    print("\n=======> chosen_articles: ", chosen_articles)
    print("\n=======> chosen_articles_images: ", chosen_articles_images)
    print("\n=======> chosen_articles_comments: ", chosen_articles_comments)
    # Combine articles and images into a list of dictionaries
    combined_data = []
    for article in chosen_articles:
        image = chosen_articles_images.filter(article=article).first()
        combined_data.append({'article': article, 'image': image})

    #print("FROM VIEWS: ", articles)
    return render(request, 'base.html', {
        'combined_data': combined_data,
        'articles_comment_total': len(chosen_articles_comments)
        }
    )




# Vue pour afficher un article individuel
def article_detail(request, article_id):

    categories = Category.objects.all()

    article = get_object_or_404(Article, pk=article_id)

    article_image = ArticleImage.objects.filter(article=article, pk=article_id)[0]
  
    article_author_images = ArticleAuthorImage.objects.filter(article=article)
  
    '''
    comments = Comment.objects.filter(article=article)
    print("comments:  ", comments)
    print("comments: ", comments)

    commentor_image = CommentorImage.objects.filter(comment=comments)
    print("commentor_image:  ", commentor_image)
    print("commentor_image: ", commentor_image)
    '''
    return render(request, 'sidebar.html', 
    {
        'article': article, 
        'blog_image': article_image.cai_article_image,
        'art_auth_image': article_author_images ,
        'categories': categories
        #'comments': comments, 
        #'commentor_image':commentor_image
    })
    #return render(request, 'article.html', {'article_id': article_id})


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
