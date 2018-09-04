from django import forms
from user.models import Reply

class CommentForm(forms.ModelForm):
    class Meta:
        # 表明这个表单对应的数据库模型是 Reply
        model = Reply
        fields = ['publish', 'message', 'user']