from django.db import models
from hashlib import md5

# Create your models here.
# 用户表，基本信息，登陆注册
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=64)
    tel = models.CharField(max_length=11, default='110')
    qq = models.CharField(max_length=11, default='110')
    wechat = models.CharField(max_length=20, default='110')
    gold = models.IntegerField(default=0)
#下面的是后端表
    top1=models.CharField(max_length=200)
    top2=models.CharField(max_length=200)
    qqname=models.CharField(max_length=20)
    logopic=models.ImageField()
    lunpic1=models.ImageField()
    lunpic2=models.ImageField()
    lastpic=models.ImageField()


#到这里为止
    def create(self, username, password):
        self.username = username
        self.password = password
        self.save()

    @classmethod
    def findName(cls, username, password=''):
        names = User.objects.filter(username = username)
        if password != '':
            if len(names) >= 1:
                pwd = names[0].password
                md = md5()
                md.update(password.encode())
                if md.hexdigest() == pwd:
                    return True
            return False
        elif len(names) >= 1:
            return False
        else:
            return True

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'


#############################################################

# 用户个人信息页面，个人信息详情
class UserDetail(models.Model):
    company = models.CharField(max_length=32, default='')
    brand = models.CharField(max_length=20, default='')
    job = models.CharField(max_length=20, default='')

    collect = models.CharField(max_length=64, default='')

    # user = models.OneToOneField("User", on_delete=models.CASCADE)

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
    live = models.IntegerField(default=0)


    class Meta:
        db_table = 'sort'


class Publish(models.Model):
    ''' 发布表 '''
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateField()
    reward = models.IntegerField()

    title = models.CharField(max_length=100)
    detail = models.TextField(default='null')
    image = models.ImageField()
    tel = models.CharField(max_length=11)
    qq = models.CharField(max_length=12,default='null')
    wechat = models.CharField(max_length=15,default='null')
    area = models.IntegerField(default=0)


    count = models.IntegerField(default=0)

    is_top = models.BooleanField(default=False)
    is_flush = models.BooleanField(default=False)

    #sort = models.ForeignKey("Sort", on_delete=models.CASCADE)
    #publisher = models.ForeignKey("User", on_delete=models.CASCADE)

    class Meta:
        db_table = 'publish'


class Reply(models.Model):
    ''' 回复表 '''
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)
    message = models.TextField()
    is_select = models.BooleanField(default=False)
    # user = models.ForeignKey("User", on_delete=models.CASCADE)
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