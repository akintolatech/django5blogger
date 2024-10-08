from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<slug:post>/<int:year>/<int:month>/<int:day>/', views.post_detail, name='post_detail'),
]
