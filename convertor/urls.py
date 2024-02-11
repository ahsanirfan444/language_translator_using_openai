from django.urls import path
from convertor import views

urlpatterns = [
    path('', views.LanguageCovertorView.as_view(), name='language_conventor')
]