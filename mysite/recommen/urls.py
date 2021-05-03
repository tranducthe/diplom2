from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name ='recommen'

urlpatterns = [
path('<int:id>/',views.recom1,name='recom1'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)