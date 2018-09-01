from django.db import models

# Create your models here.
# 用户表，基本信息，登陆注册
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=64)
    tel = models.CharField(max_length=11)
    qq = models.CharField(max_length=11)
    wechat = models.CharField(max_length=20)
    gold = models.IntegerField()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'


#############################################################

# 用户个人信息页面，个人信息详情
class UserDetail(models.Model):
    company = models.CharField(max_length=32)
    brand = models.CharField(max_length=20)
    job = models.CharField(max_length=20)

    collect = models.CharField(max_length=64)

    user = models.OneToOneField("User", on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_info'


#############################################################

 #发布主页，回复主页

class Sort(models.Model):
    '''分类表'''
    pet = models.IntegerField(default=0)
    home = models.IntegerField(default=0)
    market = models.IntegerField(default=0)
    find = models.IntegerField(default=0)
    connect = models.IntegerField(default=0)
    area = models.IntegerField(default=0)

    class Meta:
        db_table = 'sort'


class Publish(models.Model):
    ''' 发布表 '''
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField()
    reward = models.IntegerField()

    title = models.CharField(max_length=32)
    detail = models.TextField()
    image = models.ImageField()
    tel = models.CharField(max_length=11)

    count = models.IntegerField(default=0)

    is_top = models.BooleanField(default=False)
    is_flush = models.BooleanField(default=False)

    sort = models.ForeignKey("Sort", on_delete=models.CASCADE)
    publisher = models.ForeignKey("User", on_delete=models.CASCADE)

    class Meta:
        db_table = 'publish'


class Reply(models.Model):
    ''' 回复表 '''
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)
    message = models.TextField()
    is_select = models.BooleanField(default=False)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    submit_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reply'
        ordering = ['-submit_date']


class Sure(models.Model):
    ''' 交易表 '''
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)
    reply = models.ForeignKey("Reply", on_delete=models.CASCADE)

    is_pub_sure = models.BooleanField(default=False)
    is_rep_sure = models.BooleanField(default=False)

    pub_comment = models.CharField(max_length=280)
    rep_comment = models.CharField(max_length=280)

    class Meta:
        db_table = 'sure'