from django.contrib import admin
from django.conf.urls import url,include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    url(r'^articles/', include(('articles.urls', 'articles'), namespace='articles')),
    url(r'^about/$', views.about),
    url(r'^$', views.homepage),
    url(r'^api/', include('articles.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)