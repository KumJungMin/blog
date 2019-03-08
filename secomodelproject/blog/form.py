#1. 앱안에 form.py를 만든다.
from django import forms
#-장고 안에 있는 forms기능을 import한다.
from .models import Blog
#-models.py에 블로그객체를 import한다. 

class BlogPost(forms.ModelForm):
#-models를 기반으로 하는 입력공간을 만든다.(forms.ModelForm)
#-만약 입력공간의 경우 forms.Form이라고 매개변수를 받는다.
    class Meta:
        #-내장클래스 만들기(mota)
        model = Blog
        #-모델은 어떤 모델을 기반으로 입력공간을 만들지.
        fields = ['title', 'body']
        #-어떤 항목을 입력받을지.
        # (타이틀과 바디를 입력받을 수 있는 공간을 만들겠다..)

# 2. view.py에 이것들을 언제 처리해줄 지 정의한다.
