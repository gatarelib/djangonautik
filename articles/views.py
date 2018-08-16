from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles':articles})

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

class HellloApiView(APIView):
    """Test API View """

    def get(self,request,format=None):
        """Returns a list of APIView features. """

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)'
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})