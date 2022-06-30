from django.urls import path
from .views import WorksView

urlpatterns = [
    path('', WorksView.as_view(), name="works"),
]