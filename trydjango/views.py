"""
To render HTML web pages
"""

from django.http import HttpResponse
from django.shortcuts import render
import random

from articles.models import Article


def home_view(request, *args, **kwargs):
    """
    Take in a request (Djang sends request)
    Return HTML as a response (we pick to return the response)
    """
    
    random_id = random.randint(1, 12) # pseudo random
    
    # from the database
    article_obj = Article.objects.get(id=random_id)
    article_title = article_obj.title
    article_content = article_obj.content
    if article_obj.id == 1:
        article_obj.title = 'Title'
        article_obj.content = 'Content'

    query_set = Article.objects.all() #[102, 206, 345, 432, 529, 637]
    #print(query_set)
    
    context = {
        'object_list': query_set,
        'title': article_obj.title,
        'id': article_obj.id,
        'content': article_obj.content,
    }
    
    # Django Templates
    #HTML_STRING = """
    #<h1>{title} - with id = #{id}</h1>
    #<p>{content}</p>
    #""".format(**context)
    #return HttpResponse(HTML_STRING)
    
    return render(request, 'home-view.html', context)
    
    
    
    
    
    