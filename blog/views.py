from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST": # post인 경우
        form = PostForm(request.POST) #request인 Post를 받아서 폼을 만듦
        if form.is_valid():
            post = form.save(commit=False) # 포스트의 데이터 가지고 옴
            post.author = request.user # 유저정보를 갖고 있는 request.user를 가지고 옴
            post.published_date = timezone.now() # 현재 시간을 넣어줌
            post.save() # 다 만들었으면 세이브 호출
            return redirect('blog:post_detail', pk=post.pk)
            #return redirect('post_detail', pk=post.pk)
            #글을 추가하고 저장까지 끝났기에 디테일로 다시 연결, 지금 작성한 디테일 화면으로 넘어갈 수 있게 post.pk 연결
    else:
        form = PostForm() # 빈 폼을 출력
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) # 포스트폼에서 포스트에서 작성하는 것.
        if form.is_valid(): # 받아온 폼이 유효한가 체크
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            #return redirect('post_detail', pk=post.pk)
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
