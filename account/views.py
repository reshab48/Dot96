from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.views import login, logout, logout_then_login, password_change, password_change_done, password_reset_complete, password_reset_done, password_reset, password_reset_confirm
from shop.models import Item, ItemColour
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileCreateEditForm, UserEditForm, AddressAddForm, FeedBackAddForm
from .models import Profile, Address, Order, WishList, FeedBack, OrderItem
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from common.decorators import ajax_required, check_recaptcha
from django.http import JsonResponse, HttpResponse
from cart.cart import Cart
from django.core.mail import send_mail
from common.validators import check_recaptcha_ajax
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from weasyprint import HTML

def account_login(request):
	items = Item.objects.all()[:8]
	return login(request, extra_context={'items' : items})

def account_logout(request):
	logout(request)
	return redirect("shop:index")

def account_logout_then_login(request):
	items = Item.objects.all()[:8]
	return logout_then_login(request, extra_context={'items' : items})

def account_password_change(request, **kwargs):
	items = Item.objects.all()[:8]
	return password_change(request, extra_context={'items' : items}, **kwargs)

def account_password_change_done(request):
	messages.success(request, "Account password successfully changed!")
	return redirect("shop:index")

def account_password_reset(request, **kwargs):
	items = Item.objects.all()[:8]
	return password_reset(request, extra_context={'items' : items}, **kwargs)

def account_password_reset_done(request):
	messages.success(request, "We have emailed you instructions for setting your password. If dont receive an e-mail, please make sure that you have entered the e-mail address you registered with.")
	return redirect("shop:index")

def account_password_reset_confirm(request, **kwargs):
	items = Item.objects.all()[:8]
	return password_reset_confirm(request, extra_context={'items' : items}, **kwargs)

def account_password_reset_complete(request):
	messages.success(request, "Account password successfully reset!")
	return redirect("account:login")

@check_recaptcha
def account_profile_create(request):
	if request.method == 'POST':
		items = Item.objects.all()[:8]
		user_form = UserRegistrationForm(request.POST)
		profile_form = ProfileCreateEditForm(request.POST)
		if all([user_form.is_valid(), profile_form.is_valid(), request.recaptcha_is_valid]):
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			if profile_form.cleaned_data:
				profile = profile_form.save(commit=False)
				profile.user = new_user
				profile.save()
				messages.success(request, "User Successfully created!")
				return redirect("account:login")
	else:
		user_form = UserRegistrationForm()
		profile_form = ProfileCreateEditForm()
		items = Item.objects.all()[:8]
	return render(request, 'registration/sign_up.html', {'section' : 'account', 'user_form' : user_form, 'profile_form' : profile_form, 'items' : items})

@login_required
def account_detail(request, username):
	user = get_object_or_404(User, username=username, is_active=True)
	profile = Profile.objects.get(user=user)
	if request.method == 'POST':
		user_form = UserEditForm(instance=user, data=request.POST)
		profile_form = ProfileCreateEditForm(instance=profile, data=request.POST)
		if all([user_form.is_valid(), profile_form.is_valid()]):
			user_form.save()
			profile_form.save()
			messages.success(request, "Profile edited successfully!")
			return redirect(user.get_absolute_url())
		else:
			messages.error(request, "Failed editing Profile!")
	else:
		user_form = UserEditForm(instance=user)
		profile_form = ProfileCreateEditForm(instance=user.profile)
	return render(request, 'account/detail.html', {'section' : 'account', 'user' : user, 'profile' : profile, 'user_form' : user_form, 'profile_form' : profile_form})

@login_required
def account_manage_address(request):
	user = request.user
	addresses = Address.objects.filter(user=user)
	if request.method == 'POST':
		address_form = AddressAddForm(request.POST)
		if address_form.is_valid():
			address = address_form.save(commit=False)
			address.user = user
			if not addresses:
				address.default = True
			address.save()
			messages.success(request, "Address added successfully!")
			return redirect('account:account_manage_address')
		else:
			messages.error(request, "Failed adding Address!")
	else:
		address_form = AddressAddForm()
	return render(request, 'account/manage_address.html', {'section' : 'account', 'user' : user, 'addresses' : addresses, 'address_form' : address_form})

@login_required
def account_edit_address(request, address_id):
	user = request.user
	addresses = Address.objects.filter(user=user)
	address = get_object_or_404(Address, user=user, id=address_id)
	if request.method == 'POST':
		address_form = AddressAddForm(instance=address, data=request.POST)
		if address_form.is_valid():
			address = address_form.save(commit=False)
			address.save()
			messages.success(request, "Address edited successfully!")
			return redirect('account:account_manage_address')
		else:
			messages.error(request, "Failed editing Address!")
	else:
		address_form = AddressAddForm(instance=address)
	return render(request, 'account/edit_address.html', {'section' : 'account', 'user' : user, 'addresses' : addresses, 'address_form' : address_form})

@login_required
def account_delete_address(request, address_id):
	user = request.user
	address = get_object_or_404(Address, user=user, id=address_id)
	try:
		address.delete()
		messages.success(request, "Address deletd Successfully!")
	except:
		messages.error(request ,"Error deleting Address!")
	return redirect('account:account_manage_address')

@login_required
def account_mark_address_default(request, address_id):
	user = request.user
	address = get_object_or_404(Address, user=user, id=address_id)
	default_address = get_object_or_404(Address, user=user, default=True)
	try:
		default_address.default = False
		address.default = True
		default_address.save()
		address.save()
		messages.success(request, "Address marked as default Successfully!")
	except:
		messages.error(request, "Error marking Address default!")
	return redirect('account:account_manage_address')

@login_required
def account_wishlist(request):
	user = request.user
	wish_items = WishList.objects.filter(user=user)
	return render(request, 'account/wish_list.html', {'section' : 'account', 'user' : user, 'wish_items' : wish_items})

@login_required
def account_manage_feedback(request):
	user = request.user
	feedbacks = FeedBack.objects.filter(user=user)
	if request.method == 'POST':
		feedback_form = FeedBackAddForm(request.POST)
		if feedback_form.is_valid():
			feedback = feedback_form.save(commit=False)
			feedback.user = user
			feedback.save()
			messages.success(request, "Feedback or Complain added successfully!")
			return redirect('account:account_manage_feedback')
		else:
			messages.error(request, "Failed adding Feedback or Complain!")
	else:
		feedback_form = FeedBackAddForm()
	return render(request, 'account/manage_feedback.html', {'section' : 'account', 'user' : user, 'feedbacks' : feedbacks, 'feedback_form' : feedback_form})

@login_required
def cart_checkout(request):
	if request.method == 'POST':
		address_form = AddressAddForm(request.POST)
		if address_form.is_valid():
			if not Address.objects.filter(user=request.user):
				address_form.default = True
			address = address_form.save(commit=False)
			address.user = request.user
			address.save()
			addresses = Address.objects.filter(user=request.user)
	else:
		addresses = Address.objects.filter(user=request.user)
		address_form = AddressAddForm()
	return render(request, 'order/cart_checkout.html', {'section' : 'account', 'addresses' : addresses, 'address_form' : address_form})

@login_required
@ajax_required
@require_POST
def create_order(request):
	order_items = request.POST.get('order_items').split(" ")[:-1]
	quans = request.POST.get('quans').split(" ")[:-1]
	order_total = request.POST.get('total')
	address_id = request.POST.get('address')
	recaptcha_response = request.POST.get('captcha')
	address = get_object_or_404(Address, id=int(address_id))
	if check_recaptcha_ajax(recaptcha_response):
		new_order = Order.objects.create(user=request.user, drop_out=address, order_total=int(order_total))
		for item_id in order_items:
			colour = get_object_or_404(ItemColour, id=int(item_id))
			b_item = colour.item
			b_item.popularity += 1
			b_item.save()
			qnt = int(quans[order_items.index(item_id)])
			if qnt >= colour.item.wholesale_at:
				item_cost = colour.item.wholesale_price*qnt
				item_tax = colour.item.sub_category.gst/100*item_cost
				amt = item_cost + item_tax
			else:
				item_cost = colour.item.retail_price*qnt
				item_tax = colour.item.sub_category.gst/100*item_cost
				amt = item_cost + item_tax
			item = OrderItem.objects.create(item=colour, quantity=qnt, amount=amt)
			item.save()
			new_order.order_item.add(item)
		mes = "Hello "+request.user.first_name+"\nYou have received this email from Dot96 for placing an order with Order ID "+str(new_order.id)+"\nYour order of "+str(len(order_items))+" Items has been placed for Rs: "+str(order_total)+". Please Visit https://dot96.com/"+new_order.get_absolute_url()+" to check your order."
		send_mail('Order Placed', mes, 'dot96info@gmail.com', [str(request.user.email)])
		Cart(request).clear()
		new_order.save()
		return JsonResponse({'status' : 'ok'})
	else:
		return JsonResponse({'status' : 'ko'})

@login_required
def account_orders(request):
	user = request.user
	orders = Order.objects.filter(user=user)
	return render(request, 'order/list.html', {'section' : 'account', 'orders' : orders})

@login_required
def order_detail(request, id):
	order = get_object_or_404(Order, id=id)
	return render(request, 'order/detail.html', {'section' : 'account', 'order' : order})

@login_required
def order_invoice(request, id):
	order = get_object_or_404(Order, id=id, user=request.user)
	file_name = '{}_{}_invoice.pdf'.format(request.user.first_name, str(order.id))
	html_string = render_to_string('order/order_invoice.html', {'order' : order, 'request': request})
	html = HTML(string= html_string)
	html.write_pdf(target='tmp/{}'.format(file_name))
	with open("tmp/"+file_name) as pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
		return response
	return response

@login_required
def order_item_return(request, order_id, order_item_id):
	order = get_object_or_404(Order, user=request.user, id=order_id)
	order_item = get_object_or_404(OrderItem, id=order_item_id)
	try:
		order.if_return = True
		order.return_item.add(order_item)
		order.save()
		messages.success(request, 'Item Returned Successfully!')
		return redirect(order.get_absolute_url())
	except:
		messages.error(request, 'Item could not be Returned. Please try again!!')
		return redirect(order.get_absolute_url())

@login_required
def order_item_exchange(request, order_id, order_item_id):
	order = get_object_or_404(Order, user=request.user, id=order_id)
	order_item = get_object_or_404(OrderItem, id=order_item_id)
	try:
		order.if_exchange = True
		order.exchange_item.add(order_item)
		order.save()
		messages.success(request, 'Item Exchanged Successfully!')
		return redirect(order.get_absolute_url())
	except:
		messages.error(request, 'Item could not be Exchanged. Please try again!!')
		return redirect(order.get_absolute_url())