from django.db import models

# Create your models here.
class Blog(models.Model):
    #어떤 변수에 어떤 타입의 데이터를 받을 지 써준다.
    title = models.CharField(max_length = 200)
    #타이틀변수에는, 모델안에 있는 문자로 된 데이터를 title이라는 변수로 처리한다.
    #처리하는 데이터의 최대 길이는 200을 제한한다.
    pub_date = models.DateTimeField('date published')
    #이 변수에는 날짜와 시간을 나타내는 데이터를 처리한다.
    body = models.TextField()
    #CharField보다 긴 문자열을 처리하는 건 textfield

    def __str__(self):
        return self.title 
        #타이틀에 게시물목록에 보이게 하려면 이렇게

#모델파일에 어떤 데이터를 처리할지 알려주는 걸 한다.
#명령어를 이용해서 데이터베이스에게 알려주고
#admin에 데이터를 집적 넣는 것까지 진행.

    def summary(self):
        return self.body[:100]

        