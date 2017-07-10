from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin

from kitinda.authentication import views as kitinda_auth_views
from kitinda.core import views as core_views
from kitinda.accounts import urls as acc_urls
from .views import HomePageView, AboutPageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^about/$', AboutPageView.as_view(), name='about'),
    url(r'^', include(acc_urls, namespace='accounts')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^centres/', include('kitinda.centres.urls', namespace='centre')),
    url(r'^employees/', include('kitinda.employees.urls', namespace='employees')),
    url(r'^payment/', include('kitinda.payments.urls', namespace='payment')),
    url(r'^production/', include('kitinda.productions.urls', namespace ='production')),
    url(r'^login/$', kitinda_auth_views.logini, {'template_name': 'homke.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logoaaaaaaaut'),
    url(r'^signup/$', kitinda_auth_views.signup, name='signup'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/picture/$', core_views.picture, name='picture'),
    url(r'^settings/upload_picture/$', core_views.upload_picture,
        name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', core_views.save_uploaded_picture,
        name='save_uploaded_picture'),
    url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^messages/', include('kitinda.messenger.urls')),
    url(r'^u/(?P<username>[^/]+)/$', core_views.profile, name='profile'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
