from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello, current_datetime, contact
from books import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$', contact),
]




