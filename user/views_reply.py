from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.models import Publish
from user.forms import CommentForm

# Create your views here.
def test(request):
    return HttpResponse("回复需求的逻辑层")


def reply(request):
    return render(request, 'pub/reply.html')


# class AddCommentView():
#     def post(self, request):
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment_form.save()
#             return HttpResponse('{"status" : "success"}', content_type='application/json')
#         else:
#             return HttpResponse('{"status" : "fail"}', content_type='application/json')
#

def post_comment(request, publish_pk):
    # 获取需求内容
    publish = Publish.objects.get(Publish, pk=publish_pk)

    if request.method == 'POST':
        # 构造commentform表单
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            # 将回复和需求关联起来
            comment.publish = publish

            # 最终保存到数据库
            comment.save()

            return redirect('/pub/reply/')

        else:
            comment_list = publish.reply_set.all()
            context = {
                'publish' : publish,
                'form' : form,
                'comment_list' : comment_list
            }

            return render(request, 'pub/index.html', context=context)

    return redirect('/pub/reply/')