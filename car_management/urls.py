from django.contrib import admin
from django.urls import path, include
from cars.views import CarListView  

urlpatterns = [
    path('admin/', admin.site.urls),

    path('cars/', include('cars.urls')),
    
    # Главная страница
    path('', CarListView.as_view(), name='home'),  # Используем список автомобилей в качестве главной страницы

    # маршруты для входа и выхода
    path('accounts/', include('django.contrib.auth.urls')), 

    # Маршрут для регистрации
    path('accounts/', include('registration.backends.simple.urls')),

    # # Подключение маршрутов API
    # path('api/cars/', include('cars.api_urls')),
]
