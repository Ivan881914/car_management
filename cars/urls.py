from django.urls import path
from .views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView, AddCommentView, SignupView

urlpatterns = [
    path('', CarListView.as_view(), name='car-list'),
    path('<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('create/', CarCreateView.as_view(), name='car-create'),
    path('<int:pk>/edit/', CarUpdateView.as_view(), name='car-edit'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
    path('<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'),
    path('signup/', SignupView.as_view(), name='signup'),
]
