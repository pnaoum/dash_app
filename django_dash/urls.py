
from django.contrib import admin
from django.urls import path, include
from dash_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('^django_plotly_dash/', include('django_plotly_dash.urls')),

]
