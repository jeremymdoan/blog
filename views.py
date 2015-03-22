# Create your views here.
from django.shortcuts import render, get_object_or_404
from blog.models import Post #, Category
 
def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)[:10]
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts})

def archive(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/archive.html', {'posts': posts})
 
def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})

#def view_category(request, slug):
#    category = get_object_or_404(Category, slug=slug)
#    posts = Post.objects.filter(category=category).filter(published=True)[:5]
#    return render(request, 'blog/category.html', {
#        'category': category,
#        'posts': posts
#    })
