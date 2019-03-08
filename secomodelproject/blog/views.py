from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
#models에 있는 Blog함수를 가져온다.
# Create your views here.
from .form import BlogPost
#4.form->blogpost를 import해라

def home(request):
    blogs = Blog.objects #모델로부터 객체목록을 전달받을 수 있게 된다.
    #모델로부터 전달받은 객체목록을 '쿼리셋'이라고 한다.
    #->이 쿼리셋을 이용해서 기능을 만들거나 정렬할 때는 메소드를 이용한다.
    
    #model>Blog함수에 있는 객체를 담는 blogs변수
    return render(request, 'home.html', {'blogs' : blogs})
    #세번째 인자에는 키 값을 넣어준다.
    #사전형 객체, 키값을 blogs로 담아서 -> 키값을 template변수를 통해서 출력한다.
    #(home.html에서) -> 이렇게 하면 Blog.objects가 home.html에 떠야한다.

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id) 
    #이용자가 원한 id의 객체(블로그객체를 가져오는데, 블로그 아이디로 가져온다)
    return render(request, 'detail.html',{'blog': blog_detail})    

def new(request):
    return render(request, 'new.html')
# 경로를 new.html로 할 것.
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    #`request.GET['title']`은 new.html 파일에 form태그 안에 있는 녀석입니다.
    #코드를 확인해 보면 `name="title"`이라고 적혀있을텐데 그래서 `GET[]` 안에 'title'이 들어가는 겁니다. `blog.body`도 동일한 논리입니다.
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    #blog.pub_date` 의 경우는 입력한 시간이 자동으로 넘어가게끔 코드를 구성했습니다. 
    #이때 `timezone`이라는 패키지를 사용해야해서 두번째 줄에 보면 `import`를 해주는 겁니다.
    blog.save()
    return redirect('/blog/' + str(blog.id))    
    #redirect` 는 요청을 처리하고 보여주는 페이지 입니다. 
    #`render`가 '요청이 들어오면 이 html 파일을 보여줘 라는 녀석'이였다면, 
    # `redirect`는 '요청을 들어오면 저쪽 url로 보내버려' 하는 녀석입니다. 
 
def main(request):
    return render(request, 'main.html')


def blog(request):
    return render(request, 'blog.html')    

def port(request):
    return render(request, 'port.html')    

def blogpost(request):
    #request가 오면 실행되느 함
#->입력된 내용을 처리하는 기능 -> 메소드로 구분(post)
# 빈 페이지를 띄워주는 기능 -> get
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_vaild():
            post = form.save(commit = False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')

    else: #빈페이지 띄워주기
        form = BlogPost()
        #비어있는 form객체를 변수에 담기.
        return render(request, 'new.html',{'form':form })   