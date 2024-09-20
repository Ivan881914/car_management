from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import Comment
from cars.models import Car

class AddCommentView(View):
    def post(self, request, car_id):
        car = get_object_or_404(Car, pk=car_id)
        content = request.POST.get('content')
        Comment.objects.create(car=car, content=content, author=request.user)
        return redirect('car-detail', pk=car_id)
