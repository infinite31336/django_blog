from datetime import date

from django.shortcuts import render

all_posts = [
    {
        'slug': 'Heiwajima-hot-spring',
        'image': 'Heiwajima.jpg',
        'author': 'Tony',
        'date': date(2025, 6, 2),
        'title': 'Heiwajima Hot Spring',
        'excerpt': 'There is nothing more relaxing than visiting Japan and soaking in hot springs.',
        'content': '''
            Soak in Heiwajima hot springs
        '''
    },
    {
        'slug': 'stay-in-omo3-hotel',
        'image': 'omo3.jpg',
        'author': 'Tony',
        'date': date(2025, 6, 3),
        'title': 'OMO3 Hotel',
        'excerpt': 'OMO3 hotel is an affordable and comfortable place to stay.',
        'content': '''
            Stay in OMO3 Hotel
        '''
    }
]

def get_date(post):
    return post.get('date')

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    lastest_posts = sorted_posts[-2:]
    return render(request, 'blog/index.html', {
        'posts': lastest_posts
    })

def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts,
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': identified_post,
    })
