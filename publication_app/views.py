from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from hashtag_app.models import Hashtag
from .forms.create_post_form import CreatePostForm
from .models import Post



class PostListView(ListView):
    queryset = Post.objects.filter(is_public = True).all()
    template_name = 'mainpage.html'
    context_object_name = 'posts'
    ordering = ['-create_date']

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return self.queryset.all()
    #     return self.queryset.filter(is_public = True).all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['title'] = "Publications"
        context['user'] = self.request.user
        return context

    def get(self, request, *args, **kwargs):
        result = super(PostListView, self).get( request, *args, **kwargs)
        return result


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'title', 'text']
    template_name = 'create_post_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            user=self.request.user,
        )

    def get_success_url(self):
        return reverse('home')


#
# def main_page(request):
#     posts = Post.objects.filter(is_public = True).order_by('-create_date', '-id').all()
#     context = {
#                 'title': 'Insta Django',
#                 'posts': posts
#                }
#     return render(request, 'mainpage.html', context)


# @login_required
# def create_post_page(request):
#     if request.method == 'POST':
#         publication_form = CreatePostForm(request.POST,request.FILES)
#         if publication_form.is_valid():
#             publication_form.instance.user = request.user
#             publication_form.save()
#
#             hashtags = Hashtag.get_or_create(request = request , title_form_field = 'text')
#             publication_form.instance.hashtags.add(*hashtags)
#             return redirect(to='/')
#     else:
#         publication_form = CreatePostForm()
#
#     return render(request, 'create_post_form.html', {'publication_form': publication_form})

