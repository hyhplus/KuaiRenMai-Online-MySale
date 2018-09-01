from django.contrib import admin

# Register your models here.
from user.models import User,UserDetail,Sort,Reply,Sure,Publish

admin.site.register(User)
admin.site.register(UserDetail)
admin.site.register(Sort)
admin.site.register(Publish)
admin.site.register(Reply)
admin.site.register(Sure)