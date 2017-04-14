from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext,loader
from blog.models import Post



def MainPage(request):
    Post_list = Post.objects.order_by('date')
    template = loader.get_template('blog/main.html')
    context = RequestContext(request, {
            'Post_list':Post_list}
            )
    return HttpResponse(template.render(context))

def PostDetails(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'blog/details.html', {'post':post})

def LatestNews(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'blog/latestnews.html', {'post':post})
              
