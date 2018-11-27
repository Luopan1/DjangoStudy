# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime


# Create your models here.
class ShopInfo(models.Model):
    sName = models.CharField(max_length=20, verbose_name="店铺名称".encode("utf-8"))
    sAddress = models.CharField(max_length=40, verbose_name="店铺地址".encode("utf-8"))
    sType = models.CharField(max_length=20, verbose_name="店铺所属".encode("utf-8"))
    sOpenTime = models.DateTimeField(verbose_name="营业时间".encode("utf-8"))
    sCloseTime = models.DateTimeField(verbose_name="歇业时间".encode("utf-8"))
    sIsDelete = models.BooleanField(verbose_name="是否删除".encode("utf-8"))

    '''不推荐使用   推荐使用管理器来增加创建方法'''
    @classmethod
    def init(cls, name, address):
        shop = cls(sName=name, sAddress=address)
        shop.sName = name
        shop.sType = "红旗超市"
        shop.sOpenTime = datetime.datetime.now()
        shop.sCloseTime = datetime.datetime.now()
        shop.sType = "红旗超市"
        shop.sIsDelete = False
        return shop

    def __str__(self):
        result = "{shopName}"
        return (result.format(shopName=self.sName).encode("utf-8"))


class GoodsInfoManager(models.Manager):  # 自定义管理器  1  可以更改默认查询结果  同时会影响视图中的结果  下架的就不会再显示出来   #2 可以增加模型类的创建方法
    def get_queryset(self):
        return super(GoodsInfoManager, self).get_queryset().filter(gIsDelete=False)

    def create_good(self, name):
        goods = self.model()# 特别提醒
        goods.gName = name
        goods.gUpDate = datetime.datetime.now()
        goods.gDownDate = datetime.datetime.now()
        goods.gIsDelete = False
        return goods


class GoodInfo(models.Model):
    gName = models.CharField(max_length=20, verbose_name="商品名称".encode("utf-8"))
    gUpDate = models.DateTimeField(verbose_name="生产日期".encode("utf-8"))
    gDownDate = models.DateTimeField(verbose_name="过期日期".encode("utf-8"))
    gIsDelete = models.BooleanField(verbose_name="是否下架".encode("utf-8"))
    shop = models.ForeignKey("ShopInfo", on_delete=models.CASCADE, verbose_name="所在店铺".encode("utf-8"))
    goods = GoodsInfoManager()  # 创建管理器

    def __str__(self):
        result = "商品名:{gName} 生产日期:{gUpDate} 过期日期:{gDownDate}  所在商店：{gshop}"

        return (result.format(gName=self.gName, gUpDate=self.gUpDate,
                              gDownDate=self.gDownDate, gshop=self.shop.sName + (self.shop.sAddress))).encode("utf-8")
