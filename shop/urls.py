from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^products/category/(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
	url(r'^products/sub_category/(?P<sub_category_slug>[-\w]+)/$', views.product_list, name='product_list_by_sub_category'),
	url(r'^products/category/sort/(?P<category_slug>[-\w]+)/(?P<sort_type>\d+)/$', views.product_list, name='product_sortlist_by_category'),
	url(r'^products/sub_category/sort/(?P<sub_category_slug>[-\w]+)/(?P<sort_type>\d+)/$', views.product_list, name='product_sortlist_by_sub_category'),
	url(r'^products/trend/all/(?P<trending>\d+)/$', views.product_list, name='product_list_by_trend'),
	url(r'^products/trend/sort/(?P<trending>\d+)/(?P<sort_type>\d+)/$', views.product_list, name='product_sortlist_by_trend'),
	url(r'^product/detail/(?P<item_slug>[-\w]+)/$', views.product_detail, name='item_detail'),
	url(r'^product/detail/(?P<item_slug>[-\w]+)/(?P<colour_id>\d+)/$', views.product_detail, name='item_detail_by_colour'),
	url(r'^products/search/$', views.item_class_search_ajax, name='item_class_search_ajax'),
	url(r'^product/wish/$', views.item_wished, name='item_wished'),
	url(r'^terms_of_service/$', views.terms_of_service, name='terms_of_service'),
	url(r'^privacy_policy/$', views.privacy_policy, name='privacy_policy'),
]