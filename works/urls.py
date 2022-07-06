from django.urls import path
from .views import WorksView, WorkDetailView

urlpatterns = [
    path('', WorksView.as_view(), name="works"),
    path('work/<int:pk>', WorkDetailView.as_view(), name="detail"),
]