from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.CreateBlog.as_view(), name="create"),
    path("list/", views.ListBlog.as_view(), name="list"),
    # path('<int:pk>/', views.detail_blog, name="detail"),
    path("<int:pk>/detail/", views.DetailBlog.as_view(), name="detail"),
    path("<int:pk>/update/", views.UpdateBlog.as_view(), name="update"),
    path("<int:pk>/delete/", views.DeleteBlog.as_view(), name="delete"),
]