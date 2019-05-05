from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from shop.models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
def shopindex(request):
	text_var = 'This is my first django app web page.'
	return HttpResponse(text_var)

# def allProdCat(request, c_slug=None):
# 	c_page = None
# 	products = None
# 	if c_slug!=None:
# 		c_page = get_object_or_404(Category,slug=c_slug)
# 		products = Product.objects.filter(category=c_page,available=True)
# 	else:
# 		products = Product.objects.all().filter(available=True)
# 	return render(request,'shop/shopcategory.html',{'category':c_page,'products':products})
def allProdCat(request, c_slug=None):
	c_page = None
	products_list = None
	if c_slug!=None:
		c_page = get_object_or_404(Category,slug=c_slug)
		products_list = Product.objects.filter(category=c_page,available=True)
	else:
		products_list = Product.objects.all().filter(available=True)
	'''Pagination code'''
	paginator = Paginator(products_list, 6)
	try:
		page = int(request.GET.get('page','1'))
	except:
		page = 1
	try:
		products = paginator.page(page)
	except (EmptyPage,InvalidPage):
		products = paginator.page(paginator.num_pages)
	return render(request,'shop/shopcategory.html',{'category':c_page,'products':products})

def ProdCatDetail(request,c_slug, product_slug):
	try:
		product = Product.objects.get(category__slug=c_slug,slug=product_slug)
	except Exception as e:
		raise e
	return render(request,'shop/shopproduct.html', {'product':product})
