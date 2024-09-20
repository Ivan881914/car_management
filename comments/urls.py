from django.urls import path
from .views import AddCommentView

urlpatterns = [
    path('add/<int:car_id>/', AddCommentView.as_view(), name='add-comment'),
]
