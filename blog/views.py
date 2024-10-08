from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404


# Create your views here.
def post_list(request):
    # Extract published posts from the custom manager
    posts = Post.published.all()

    return render(
        request,
        "blog/post/blog-list.html",
        {"posts": posts}
    )


def post_detail(request, year, month, day, post):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No post found")

    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,

    )

    return render(
        request,
        "blog/post/blog-detail.html",
        {"post": post}
    )
