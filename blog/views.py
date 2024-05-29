from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog,Comment
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib import messages


def blog_list(request):
    query = request.GET.get('search')
    if query:
        blog_list = Blog.objects.filter(tags__name__icontains=query)
    else:
        blog_list = Blog.objects.all()

    paginator = Paginator(blog_list, 4)  # Show 4 blogs per page
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        commenter = request.user
        Comment.objects.create(blog=blog, commenter=commenter, content=content)
        return redirect('blog_detail', blog_id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})


def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.likes += 1  # Increment the like count
    blog.save()
    return redirect('blog_detail', blog_id=blog_id)


def add_comment(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        commenter = request.user
        Comment.objects.create(blog=blog, commenter=commenter, content=content)
        messages.success(request, 'Comment added successfully!')
        return redirect('blog_detail', blog_id=blog_id)
    # Redirect back to the blog detail page after adding comment
    return redirect('blog_detail', blog_id=blog_id)