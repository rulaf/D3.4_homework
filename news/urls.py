from django.urls import path
from .views import NewsList, NewDetail  # импортируем наше представление

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewDetail.as_view()),
]
