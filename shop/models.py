from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)

	class Meta:
		index_together = (('id', 'slug'),)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_list_by_category', args=[self.slug])


class SubCategory(models.Model):
	category = models.ForeignKey(Category, db_index=True, related_name='sub_categories')
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)
	gst = models.DecimalField(default=18, max_digits=4, decimal_places=2)

	class Meta:
		index_together = (('id', 'slug'),)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_list_by_sub_category', args=[self.slug])


class Item(models.Model):
	category = models.ForeignKey(Category, db_index=True)
	sub_category = models.ForeignKey(SubCategory, db_index=True)
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)
	wished = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='items_liked')
	index_image = models.ImageField(upload_to='items/', blank=True)
	description = models.TextField(blank=True)
	available = models.BooleanField(default=True)
	wholesale_at = models.PositiveIntegerField(default=3)
	price = models.DecimalField(max_digits=15, decimal_places=2)
	retail_dis = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
	wholesale_dis = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
	retail_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
	wholesale_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
	popularity = models.PositiveIntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = '-created', '-updated',

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		if self.retail_price or self.wholesale_price != 0:
			ret_dis = self.price-self.retail_price
			self.retail_dis = ret_dis/self.price*100
			who_dis = self.price-self.wholesale_price
			self.wholesale_dis = who_dis/self.price*100
		super(Item, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('shop:item_detail', args=[self.slug])


class ItemColour(models.Model):
	item = models.ForeignKey(Item, db_index=True)
	colour_image = models.ImageField(upload_to='colours/')
	stock = models.PositiveIntegerField(default=30)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = '-created', '-updated',

	def __unicode__(self):
		return self.item.name

	def save(self, *args, **kwargs):
		if self.stock == 0:
			self.available = False
		else:
			self.available = True
		super(ItemColour, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('shop:item_detail_by_colour', args=[self.item.slug, self.id])


class ItemImage(models.Model):
	item_colour = models.ForeignKey(ItemColour, db_index=True, related_name='item_images')
	image = models.ImageField(upload_to='items/images')

	def __unicode__(self):
		return self.item_colour.item.name


class Detail(models.Model):
	item = models.ForeignKey(Item, db_index=True, related_name='details')
	info = models.CharField(max_length=150)

	class Meta:
		ordering = 'item',

	def __unicode__(self):
		return "{} : {}".format(self.item.name, self.info)


class Promo(models.Model):
	sub_category = models.ForeignKey(SubCategory, db_index=True, related_name='promotions')
	image = models.ImageField(upload_to='promos/')
	m_image = models.ImageField(upload_to='m_promos/', blank=True)
	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = '-created',

	def __unicode__(self):
		return self.sub_category.name