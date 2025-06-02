from django.shortcuts import render

def starting_page(request):
    return render(request, 'blog/index.html')

def posts(request):
    print('render all post page')
    return render(request, 'blog/all-posts.html')

def post_detail(request, slug):
    return render(request, 'blog/post-detail.html')
