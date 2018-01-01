from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from shop.models import Item, ItemColour
from .cart import Cart

@require_POST
def cart_add(request):
	cart = Cart(request)
	item_id = request.POST.get('item')
	item = get_object_or_404(Item, id=int(item_id))
	quantity = request.POST.get('quantity')
	colour_id = request.POST.get('colour')
	colour = get_object_or_404(ItemColour, id=int(colour_id))
	update = request.POST.get('update')
	try:
		if update:
			cart.add(item=item, colour=colour, quantity=int(quantity), update=True)
		else:
			cart.add(item=item, colour=colour, quantity=int(quantity))
	except ValueError:
		pass
	return JsonResponse({'status' : 'ok'})

@require_POST
def cart_remove(request):
	cart = Cart(request)
	item_id = request.POST.get('item')
	item = get_object_or_404(Item, id=int(item_id))
	colour_id = request.POST.get('colour')
	colour = get_object_or_404(ItemColour, id=int(colour_id))
	cart.remove(item, colour)
	return JsonResponse({'status' : 'ok'})

def cart_detail(request):
	cart = Cart(request)
	return render(request, 'cart/detail.html', {'cart' : cart})