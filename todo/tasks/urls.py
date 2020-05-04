from django.urls import path
from . import views

urlpatterns = [
    path('', views.summary_view),
    path('new/', views.new_view),
    path('done/', views.done_view)
]