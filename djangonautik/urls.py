from django.contrib import admin
from django.conf.urls import url,include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^about/$', views.about),
    url(r'^$', views.homepage),
    url(r'^api/', include('articles.urls'))
]

urlpatterns += staticfiles_urlpatterns()