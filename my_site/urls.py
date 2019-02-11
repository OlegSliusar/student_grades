from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('stage/', views.base),
    path('section/<int:id_sec>/stage/<int:id_stg>', views.base, name="stage_page")
]
