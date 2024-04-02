from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('squarearea/',views.squarearea,name="squarearea"),
    path('',views.squarearea,name="squarearea")
]