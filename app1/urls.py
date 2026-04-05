from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
    path("admin/", admin.site.urls),
    path("coffeebeans/",views.CoffeeBeansList.as_view(), name="coffee-bean-list-view"),
    path("coffeebeans/<int:pk>",views.CoffeeBeansListDelete.as_view(), name="update"),
    path("coffeebeans/new/",views.CustomCoffeeBeansList.as_view(), name="coff"),
]