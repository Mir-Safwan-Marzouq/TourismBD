from django.conf.urls import url
from django.urls import path
from TourismBD import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'TourismBD'

urlpatterns=[
    path('',views.index,name='index'),
    path('division/<int:b>',views.division,name='division'),
    path('feedback/',views.feedback,name='feedback'),
    path('about/',views.about,name='about'),
    path('district/<int:z>',views.district,name='district'),
    path('search_district/',views.search_district,name='search_district'),
    path('destination/<int:dest>',views.destination,name='destination')

]
urlpatterns= urlpatterns+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
