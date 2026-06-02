from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('nuevo/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/editar/', views.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/eliminar/', views.PostDeleteView.as_view(), name='post_delete'),
]
