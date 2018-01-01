from django.conf import settings
from .models import Item
import datetime

class ItemsViewed(object):
	def __init__(self, request):
		self.session = request.session
		items_viewed = self.session.get(settings.VIEW_SESSION_ID)
		if not items_viewed:
			items_viewed = self.session[settings.VIEW_SESSION_ID] = {}
		self.items_viewed = items_viewed

	def add(self, item):
		item_id = item.id
		if item_id not in self.items_viewed:
			self.items_viewed[item_id] = {"item" : item, "date-time" : datetime.datetime.now() }
		else:
			self.items_viewed[item_id]["date-time"] = datetime.datetime.now()
		self.save()

	def save(self):
		self.session[settings.VIEW_SESSION_ID] = self.items_viewed
		self.session.modified = True 