from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Comment
from django.contrib.contenttypes.models import ContentType


# Create your views here.
def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    user = request.user
    if not user.is_authenticated:
        return render(request, 'error.html', {'message': '未登录','redirect_to':referer})
    text = request.POST.get('text', '').strip()
    if text == '':
        return render(request, 'error.html', {'message': '评论不能为空','redirect_to':referer})
    content_type = request.POST.get('content_type', '')
    object_id = int(request.POST.get('object_id', ''))
    model_class = ContentType.objects.get(model=content_type).model_class()
    model_obj = model_class.objects.get(pk=object_id)

    comment = Comment()
    comment.user = user
    comment.text = text
    comment.content_object = model_obj
    comment.save()
    return redirect(referer)
