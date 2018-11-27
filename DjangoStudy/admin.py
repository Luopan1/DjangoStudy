# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import GoodInfo, ShopInfo


# Register your models here.
class GoodsInfoInline(admin.TabularInline):
    model = GoodInfo
    extra = 2


class ShopInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "sName","sAddress", "sOpenTime" ,"sCloseTime", "sIsDelete", "sType"]
    list_filter = ["sName", "sOpenTime", "sCloseTime", "sIsDelete", "sType"]
    list_per_page = 10
    inlines = [GoodsInfoInline]


admin.site.register(ShopInfo, ShopInfoAdmin)
admin.site.register(GoodInfo)
