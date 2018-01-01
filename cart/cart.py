from decimal import Decimal
from django.conf import settings
from shop.models import Item

class Cart(object):

	def __init__(self, request):
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def add(self, item, colour, quantity=1, update=False):
		item_id = str(item.id)+"/"+str(colour.id)
		if quantity >= item.wholesale_at:
			price = item.wholesale_price
		else:
			price = item.retail_price
		if item_id not in self.cart:
			self.cart[item_id] = {'quantity': 0, 'price': str(price), 'item' : item, 'colour' : colour, 'gst' : item.sub_category.gst}
		if quantity > colour.stock:
			quantity = colour.stock
		if update:
			self.cart[item_id]['quantity'] = quantity
			self.cart[item_id]['price'] = price
		else:
			if self.cart[item_id]['quantity']+quantity > colour.stock:
				self.cart[item_id]['quantity'] = quantity
			else:
				self.cart[item_id]['quantity'] += quantity
			self.cart[item_id]['price'] = price
		self.save()

	def save(self):
		self.session[settings.CART_SESSION_ID] = self.cart
		self.session.modified = True

	def remove(self, item, colour):
		item_id = str(item.id)+"/"+str(colour.id)
		if item_id in self.cart:
			del self.cart[item_id]
			self.save()

	def __iter__(self):
		for obj in self.cart.values():
			obj['price'] = Decimal(obj['price'])
			obj['total_price'] = obj['price'] * obj['quantity']
			obj['total_gst'] = obj['gst']/100 * obj['total_price']
			yield obj

	def __len__(self):
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_gst(self):
		return int(sum(Decimal(item['total_gst']) for item in self.cart.values()))

	def get_total_price(self):
		return int(sum(Decimal(item['total_price']) for item in self.cart.values())+self.get_total_gst())

	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True