from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "post"

urlpatterns = [
    path('post/',views.post,name="post"),
    path('comp/', views.comp,name="comp"),
    path('view/', views.view2,name="view"),
    path('view/<int:post_id>',views.syousai,name="syousai"),
]
if settings.DEBUG:
    urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)