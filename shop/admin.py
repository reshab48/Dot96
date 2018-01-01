from django.contrib import admin
from .models import Category, SubCategory, Item, Detail, Promo, ItemColour, ItemImage


class SubCategoryInline(admin.TabularInline):
	model = SubCategory
	raw_id_fields = ['category']
	prepopulated_fields = {'slug' : ('name',)}

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug' : ('name',)}
	inlines = [SubCategoryInline]
admin.site.register(Category, CategoryAdmin)

class DetailInline(admin.TabularInline):
	model = Detail
	raw_id_fields = ['item']

class ItemColourInline(admin.TabularInline):
	model = ItemColour
	raw_id_fields = ['item']

class ItemAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'retail_price', 'wholesale_price', 'created', 'updated']
	list_filter = ['category', 'sub_category', 'created', 'updated']
	list_editable = ['price', 'retail_price', 'wholesale_price']
	search_fields = ('name',)
	prepopulated_fields = {'slug' : ('name',)}
	inlines = [DetailInline, ItemColourInline]
admin.site.register(Item, ItemAdmin)

class ItemImageInline(admin.TabularInline):
	model = ItemImage
	raw_id_fields = ['item_colour']

class ItemColourAdmin(admin.ModelAdmin):
	list_display = ['item', 'stock', 'available']
	list_filter = ['item__sub_category', 'created', 'updated']
	inlines = [ItemImageInline]
admin.site.register(ItemColour, ItemColourAdmin)

admin.site.register(Promo)