from django.conf.urls import url
from . import views
from djang.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^accounts/profile/(\d+)' views.profile, name='profile'),
    
]
