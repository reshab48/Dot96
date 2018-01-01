from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from shop.models import Item, ItemColour
from django.utils.crypto import get_random_string
from django.core.urlresolvers import reverse
from django.utils import timezone

CITY = (
	('SLG', 'Siliguri'),
	('JPG', 'Jalpaiguri')
	)

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, db_index=True)
	mobile_no = models.CharField(max_length=10)

	def __unicode__(self):
		return "{}: {}".format(self.user, self.mobile_no)

class Address(models.Model):
	user = models.ForeignKey(User, db_index=True)
	full_name = models.CharField(max_length=50)
	street = models.CharField(max_length=100)
	city = models.CharField(max_length=3, choices=CITY)
	pin = models.CharField(max_length=6)
	landmark = models.CharField(max_length=100)
	phone = models.CharField(max_length=10, blank=True)
	default = models.BooleanField(default=False)

	def __unicode__(self):
		return "{}, {}".format(self.landmark, self.city)

	def get_absolute_edit_url(self):
		return reverse('account:account_edit_address', args=[self.id])

	def get_absolute_del_url(self):
		return reverse('account:account_delete_address', args=[self.id])

	def get_absolute_mark_as_def_url(self):
		return reverse('account:account_mark_address_default', args=[self.id])

class OrderItem(models.Model):
	item = models.ForeignKey(ItemColour, db_index=True)
	quantity = models.PositiveIntegerField()
	amount = models.PositiveIntegerField()

	def __unicode__(self):
		return "{}: {}".format(self.item.item.name, self.quantity)

class Order(models.Model):
	user = models.ForeignKey(User, db_index=True)
	order_item = models.ManyToManyField(OrderItem, related_name='items_ordered')
	drop_out = models.ForeignKey(Address)
	order_total = models.PositiveIntegerField()
	paid = models.BooleanField(default=False)
	if_return = models.BooleanField(default=False)
	return_item = models.ManyToManyField(OrderItem, blank=True, related_name='items_returned')
	cashback = models.BooleanField(default=False)
	if_exchange = models.BooleanField(default=False)
	exchange_item = models.ManyToManyField(OrderItem, blank=True, related_name='items_exchanged')
	exchanged = models.BooleanField(default=False)
	delivered_on = models.DateTimeField(blank=True, default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = '-created', '-if_exchange', '-if_return', '-updated',

	def __unicode__(self):
		return "{}: {}".format(self.id, self.user)

	def get_absolute_url(self):
		return reverse('account:order_detail', args=[self.id])

	def get_absolute_invoice_url(self):
		return reverse('account:order_invoice', args=[self.id])

class WishList(models.Model):
	user = models.ForeignKey(User, db_index=True)
	item = models.ForeignKey(Item)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ('user', 'item')
		ordering = '-created', '-updated',

	def __unicode__(self):
		return "{}: {}".format(self.user, self.item.name)

class FeedBack(models.Model):
	user = models.ForeignKey(User, db_index=True)
	subject = models.CharField(max_length=100)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = '-created', '-updated',

	def __unicode__(self):
		return self.user