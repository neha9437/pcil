from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404


def home(request):
    # all_albums = Album.objects.all()
    # we dont write music/template/music/index.html because befault it searches in templates
    context = {}
    # return HttpResponse(template.render(context,request))
    return HttpResponse("Welcome to Pest Control India")
    # we need HttpResponse to render a template, but we can use render function directly as it has the HttpResponse built-in in it.
    # return render(request,'product_request/index.html',context)