from django.conf.urls import url

from . import views

app_name = 'mainpage'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^complete_info$', views.complete_info, name='complete'),
    url(r'^location$', views.location, name='location'),
    url(r'^personal_center$', views.jmp_to_personal, name='personal_center'),
    url(r'^jmp_to_complete_info$', views.jmp_to_complete_info, name="jmp_to_complete_info"),
    url(r'^query_user_info$', views.query_user_info, name="query_user_info"),
    url(r'^check_origin_pwd$', views.check_origin_pwd, name="check_origin_pwd"),
    url(r'^change_password$', views.change_password, name="change_password"),
    url(r'^add_addr$', views.add_address, name="add_addr"),
    url(r'^get_address_count$', views.get_address_count, name="get_address_count"),
    url(r'^show_first_page$', views.show_first_page, name="show_first_page"),
    url(r'^del_addr$', views.del_addr, name="del_addr"),
    url(r'^conf_default_addr$', views.conf_default_addr, name="conf_default_addr"),
    url(r'^(?P<shop_id>[0-9]+)/jmp_to_shop_detail/$', views.jmp_to_shop_detail, name='jmp_to_shop_detail'),
    url(r'^(?P<shop_id>[0-9]+)/shop_detail/$', views.shop_detail, name='shop_detail'),
    url(r'^shoppingcar$', views.jmp_to_shoppingcar, name='shoppingcar'),
    url(r'^show_shops_orderby_sales$', views.show_shops_orderby_sales, name='show_shops_orderby_sales'),
    url(r'^get_merchandises$', views.get_merchandises, name="get_merchandises"),
    url(r'^get_spec_shopinfo$', views.get_spec_shopinfo, name="get_spec_shopinfo"),
    url(r'^get_my_threemonth_order$', views.get_my_threemonth_order, name='get_my_threemonth_order'),
    url(r'^add_to_shopcar$', views.add_to_shopcar, name='add_to_shopcar'),
    url(r'^get_cart$', views.get_cart, name='get_cart'),
    url(r'^flush_cart$', views.flush_cart, name='flush_cart'),
    url(r'^get_shop_by_keywords$', views.get_shop_by_keywords, name="get_shop_by_keywords"),
    url(r'^get_shopinfo_by_id$', views.get_shopinfo_by_id, name="get_shopinfo_by_id"),
    url(r'^get_merchan_by_id$', views.get_merchan_by_id, name="get_merchan_by_id"),
    url(r'^place_order$', views.place_order, name="place_order"),
]