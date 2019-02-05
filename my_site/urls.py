from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('stage/<int:id_stg>', views.base, name="stage_page")
]
