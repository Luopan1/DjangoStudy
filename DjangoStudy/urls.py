from django.conf.urls import url
from DjangoStudy import views

urlpatterns=[
    url(r"^$",views.index),
    url(r"^(\d+)$",views.show)
]