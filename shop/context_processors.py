from .models import Category, SubCategory
from django.conf import settings

def sub_categories(request):
	sub_categories = SubCategory.objects.all()
	return {'sub_categories' : sub_categories}

def categories(request):
	categories = Category.objects.all()
	return {'categories' : categories}

def items_viewed(request):
	viewed = request.session.get(settings.VIEW_SESSION_ID)
	if not viewed:
		viewed = request.session[settings.VIEW_SESSION_ID] = {}
	all_items_viewed = viewed.values()
	items_viewed = sorted(all_items_viewed, key=lambda all_items_viewed: all_items_viewed["date-time"], reverse=True)[:4]
	return {'items_viewed' : items_viewed}