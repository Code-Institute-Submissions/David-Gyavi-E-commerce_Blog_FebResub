from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name="myblog"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path(
        '<slug:slug>/comment/', views.AddCommentView.as_view(),
        name='add_comment'),
    path(
        '<pk>/update_comment', views.EditCommentView.as_view(),
        name='update_comment'),
    path(
        '<pk>/delete_comment', views.DeleteCommentView.as_view(),
        name='delete_comment'),
]
