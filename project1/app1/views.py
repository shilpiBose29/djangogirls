from django.shortcuts import render
from app1.models import Post 
from django.contrib.auth.models import User


# Create your views here.
def home(request):
	if request.method == "GET":
		return render(request, 'blog.html')
	else:
		post = publish(request)
		posts = grab_all_posts()
		context = dict()
		context['posts'] = posts
		return render(request, 'blogposts.html', context)

def posts(request):
	posts = grab_all_posts()
	context = dict()
	context['posts'] = posts
	return render(request, 'blogposts.html', context)


def publish(request):
	post = Post()
	post.author = User.objects.get(id=request.POST['author'])
	post.title = request.POST['title']
	post.text = request.POST['text']
	post.created_date = request.POST['created_date_0']
	post.published_date = request.POST['published_date_0']
	post.save()

	return post

def grab_all_posts():
	posts = Post.objects.all()
	return posts

def post_link(request, post_id):
	post = Post.objects.get(id=post_id)
	context = dict()
	context['post'] = post
	return render(request, 'posts.html', context)