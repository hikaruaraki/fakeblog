from . import views
from django.urls import path

app_name = 'comment'

urlpatterns = [
    path('commentbase/',views.commentbase,name="commentbase"),
    path('comment/',views.comment,name='comment'),
    path('comment/',views.CommentView.as_view(),name='comment'),
    path('success/',views.success,name='success'),
]