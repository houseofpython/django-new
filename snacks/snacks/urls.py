from django.urls import path
from .views import SnackDetailView, SnackListView, SnackCreateView, SnackDeleteView, SnackUpdateView

urlpatterns = [
    path('', SnackListView.as_view(), name='snack-list'),
    path('<int:pk>/', SnackDetailView.as_view(), name='detail-view'),
    path('new/', SnackCreateView.as_view(), name='create-view'),
    path('<int:pk>/edit', SnackUpdateView.as_view(), name='update-view'),
    path('<int:pk>/delete', SnackDeleteView.as_view(), name='delete-view')
]

