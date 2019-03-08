from django.contrib import admin
from .models import Blog
#같은 폴더에 있는 model에 있는 Blog객체를 불러와라!
# Register your models here.


admin.site.register(Blog)
#admin사이트에 Blog객체를 등록해라~