from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index,name="index"),
    path("breakfast/",views.breakfast_cofee_tea_sugar,name="breakfast"),
    path('temp/',views.mytemplate),
    path('contact/',views.cont),
    path("Index/", views.index,name="index"),
    path("fruites/", views.fruites,name="Fruites"),
    path("Veggies/", views.veggies,name="vegg"),
    path("Staples/", views.Staples,name="staples"),
    path("chocolateanddrinks/", views.chocolate_drinks,name="chocolate"),
    path("munchies/", views.munchies,name="munchies"),
    path("biscuites/", views.biscuites,name="bisc"),

]
