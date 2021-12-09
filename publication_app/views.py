from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def main_page(request):
    #mock_post = [{'title': random.randint(1, 100), 'text': 'dfsdfsfdsfddf'} for _ in range(1,100)]
    posts = Post.objects.filter(is_public = True).order_by('-create_date', '-id').all()
    context = {'title': 'hi', 'text': 'dfsdfsdfs'}
    return render(request, 'mainpage.html', context)