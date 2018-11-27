# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from DjangoStudy.models import *


# Create your views here.

def index(request):
    list = ShopInfo.objects.all()
    context = {"list": list}
    return render(request, "html/index.html", context)


def show(request, id):
    shop = ShopInfo.objects.get(pk=id)
    goodslists=shop.goodinfo_set.all()
    context = {"list": goodslists}
    return render(request, "html/show.html", context)
