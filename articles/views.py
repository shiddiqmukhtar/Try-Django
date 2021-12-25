from django.shortcuts import render, redirect

from .models import Article

# Create your views here.

def article_search_view(request):

    #print(request.GET)
    query_dict = request.GET
    #query = query_dict.get('q')
    
    try:
        query = int(query_dict.get('q'))
    except:
        query = None

    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        'object': article_obj,
    }
    
    return render(request, 'articles/search.html', context)
    
    
def article_create_view(request):
    #print(request.POST)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(title, content)
        Article.objects.create(title=title, content=content)
        return redirect('/')
    context = {}
    
    return render(request, 'articles/create.html', context)
    

def article_detail_view(request, id=None):

    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    
    context = {
        'object': article_obj,
    }
    
    return render(request, 'articles/detail.html', context)












