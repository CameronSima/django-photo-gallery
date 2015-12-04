from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login, logout
from . import views
from pornsite.views import CustomRegView


urlpatterns = patterns('',
    url(r'^$', 'site.views.front', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^content/', include('photologue_custom.urls', 
                            namespace='custom_photologue')),
    url(r'^content/', include('photologue.urls', namespace='photologue')),
    url(r'^content/galleries/', include('galleries.urls', namespace='galleries')),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^about/', views.about, name='about'),

    url(r'^accounts/register/$',
                           CustomRegView.as_view(),
                           name='registration_register'),
    url(r'^accounts/register/complete/$', views.payment,
                           name='registration_complete'),


    url('https://37ea4b27.ngrok.com/', views.paypal_incoming), 
                            include('paypal.standard.ipn.urls')),


    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^accounts/profile/$', views.user_profile, name='user_profile'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
