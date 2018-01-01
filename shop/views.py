from django.shortcuts import render, get_object_or_404
from .models import Category, SubCategory, Item, ItemColour, ItemImage, Detail, Promo
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .items_viewed import ItemsViewed
from common.decorators import ajax_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from account.models import WishList

@ensure_csrf_cookie
def index(request):
	items = Item.objects.filter(available=True).order_by('-popularity')[:12]
	promos = Promo.objects.all()
	return render(request, 'shop/index.html', {'items' : items, 'promos' : promos, 'section' : 'shop'})

def product_list(request, sub_category_slug=None, category_slug=None, sort_type=None, trending=None):
	category = None
	sub_category = None
	if trending:
		items = Item.objects.filter(available=True).order_by('-popularity')
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		items = Item.objects.filter(category=category).order_by('-popularity')
	if sub_category_slug:
		sub_category = get_object_or_404(SubCategory, slug=sub_category_slug)
		items = Item.objects.filter(sub_category=sub_category).order_by('-popularity')
	if sort_type:
		if sort_type == "1":
			items = items.order_by('-popularity')
		elif sort_type == "2":
			items = items.order_by('price')
		elif sort_type == "3":
			items = items.order_by('-price')
		elif sort_type == "4":
			items = items.order_by('-created')
	total = items.count()
	paginator = Paginator(items, 8)
	page = request.GET.get('page')
	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		if request.is_ajax():
			return HttpResponse('')
		items = paginator.page(paginator.num_pages)
	if request.is_ajax():
		return render(request, 'shop/items/list_ajax.html', {'section' : 'shop', 'items' : items})
	return render(request, 'shop/items/list.html', {'section' : 'shop', 'items' : items, 'category' : category, 'sub_category' : sub_category, 'trending' : trending, 'total' : total})

def product_detail(request, item_slug, colour_id=None):
	item = get_object_or_404(Item, slug=item_slug)
	items_viewed = ItemsViewed(request)
	items_viewed.add(item)
	item_details = Detail.objects.filter(item=item)
	item_colours = ItemColour.objects.filter(item=item)
	colour_index = item_colours[0]
	colour_images = ItemImage.objects.filter(item_colour=colour_index)
	similar_items = Item.objects.filter(sub_category=item.sub_category)[:4]
	if colour_id:
		colour_index = ItemColour.objects.get(id=colour_id)
		colour_images = ItemImage.objects.filter(item_colour=colour_index)
	return render(request, 'shop/items/detail.html', {'section' : 'shop', 'item' : item, 'item_details' : item_details, 'item_colours' : item_colours, 'colour_images' : colour_images, 'similar_items' : similar_items, 'colour_index' : colour_index})

@ajax_required
@require_POST
def item_class_search_ajax(request):
	search_text = request.POST.get("text")
	json_data = {}
	if search_text:
		item_classes = SubCategory.objects.filter(name__icontains=search_text)[:4]
	if item_classes:
		for item_class in item_classes:
			append_json = {}
			url = item_class.get_absolute_url()
			name = item_class.name.encode("utf-8")
			cat = item_class.category.name.encode("utf-8")
			cat_url = item_class.category.get_absolute_url()
			append_json["name"] = name
			append_json["cat"] = cat
			append_json["url"] = str(url)
			append_json["cat_url"] = str(cat_url)
			json_data["{}".format(str(item_class.id))] = append_json
	return JsonResponse(json_data)

@ajax_required
@require_POST
@login_required
def item_wished(request):
	item_id = request.POST.get('id')
	action = request.POST.get('action')
	if item_id and action:
		try:
			item = Item.objects.get(id=int(item_id))
			if action == 'wish':
				item.wished.add(request.user)
				WishList.objects.create(user=request.user, item=item)
			else:
				item.wished.remove(request.user)
				WishList.objects.get(user=request.user, item=item).delete()
			return JsonResponse({'status' : 'ok'})
		except:
			pass
	return JsonResponse({'status' : 'ko'})

def terms_of_service(request):
	return render(request, 'legal/terms.html', {'section' : 'shop'})

def privacy_policy(request):
	return render(request, 'legal/privacy.html', {'section' : 'shop'})	