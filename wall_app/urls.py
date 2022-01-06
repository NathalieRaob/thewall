from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('post_message', views.post_msg),
    path('post_comment/<int:id>', views.post_comment),
    path('user_profile/<int:id>', views.user_profile),
    path('like/<int:id>', views.add_like),
    path('delete/<int:id>', views.delete_comment),
    path('edit/<int:id>', views.edit),
    path('delete_post/<int:id>', views.delete_post),
    path('edit_profile/<int:id>', views.edit_profile),
    path('myprofile/<int:id>', views.myprofile)
]
