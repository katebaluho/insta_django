from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from hashtag_app.models import Hashtag
from .forms.create_post_form import CreatePostForm
from .models import Post
# Create your views here.

def main_page(request):
    #mock_post = [{'title': random.randint(1, 100), 'text': 'dfsdfsfdsfddf'} for _ in range(1,100)]
    posts = Post.objects.filter(is_public = True).order_by('-create_date', '-id').all()
    context = {'title': 'Insta Django', 'posts': posts}
    return render(request, 'mainpage.html', context)

@login_required
def create_post_page(request):
    if request.method == 'POST':
        publication_form = CreatePostForm(request.POST,request.FILES)
        if publication_form.is_valid():
            publication_form.instance.author = request.user
            publication_form.save()

            hashtags = Hashtag.get_or_create(request = request , title_form_field = 'text')
            publication_form.instance.hashtags.add(*hashtags)
            return redirect(to='/')
    else:
        publication_form = CreatePostForm()

    return render(request, 'create_post_form.html', {'publication_form': publication_form})
