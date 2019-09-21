from django.shortcuts import render, get_object_or_404
from .models import pcil_products,pcil_cities,product_requisition


def index(request):
    all_products = pcil_products.objects.all()
    # we dont write music/template/music/index.html because befault it searches in templates
    context = {'all_products':all_products}
    # return HttpResponse(template.render(context,request))
    # return HttpResponse("This is my music app homepage")
    # we need HttpResponse to render a template, but we can use render function directly as it has the HttpResponse built-in in it.
    return render(request,'product_request/index.html',context)


def details(request,product_id):
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exist")
    product = get_object_or_404(pcil_products,id=product_id)
    context = {'product':product}
    return render(request,'product_request/details.html',context)
    # +(album_id.title)+(album_id.artist)+(album_id.genre)+(album_id.logo)+


def favorite(request,product_id):
    # print("product_id",product_id)
    # product = get_object_or_404(pcil_products,id=product_id)
    # print("product",product)
    # try:
    # 	selected_product_requisition = product.product_requisition_set.get(id=request.POST['product_requisition'])
    # except (KeyError, product_requisition.DoesNotExist):
    # 	return render(request, 'product_request/details.html',{
    # 			'product':product,
    # 			'error_message': "Invalid sub product"
    # 		})
    # else:
    # 	selected_product_requisition.is_favorite = True
    # 	selected_product_requisition.save()
    # 	return render(request,'product_request/details.html',{'product':product})
    context = {}
    return render(request,'product_request/final.html',context)


# def index(request):
#     all_albums = Album.objects.all()
#     # we dont write music/template/music/index.html because befault it searches in templates
#     context = {
#     	'all_albums':all_albums,
#     }
#     # return HttpResponse(template.render(context,request))
#     # return HttpResponse("This is my music app homepage")
#     # we need HttpResponse to render a template, but we can use render function directly as it has the HttpResponse built-in in it.
#     return render(request,'music/index.html',context)


# def details(request,album_id):
#     # try:
#     #     album = Album.objects.get(pk=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Album does not exist")
#     album = get_object_or_404(Album,id=album_id)
#     context = {'album':album}
#     return render(request,'music/details.html',context)
#     # +(album_id.title)+(album_id.artist)+(album_id.genre)+(album_id.logo)+
