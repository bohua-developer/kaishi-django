from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from article.models import LevelDirectory,SecondaryDirectory,AllContentList
# Create your views here.

def index(request):
    levelDirectory = LevelDirectory.objects.all()
    re_content = {"directory":levelDirectory,}
    return render_to_response("base.html",re_content)

def content_list(request,offset):
    # return HttpResponse(offset)
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    contentList = SecondaryDirectory.objects.all().filter(series=offset)
    re_content = {"contentlist":contentList,}
    return render_to_response("contentList.html",re_content)

def content_all_list(request):
    contentList = SecondaryDirectory.objects.all()
    re_content = {"contentlist": contentList,"all_One":True,}
    return render_to_response("contentList.html", re_content)

def the_content(request,offset1,offset2):
    try:
        offset1 = int(offset1)
        offset2 = int(offset2)
    except ValueError:
        raise Http404()
    content = AllContentList.objects.all().filter(series=offset1).filter(page=offset2)
    re_content = {"the_content":content}
    return render_to_response("content.html",re_content)