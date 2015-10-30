"""Siscon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns
# urlpatterns =(
#     '',
#     url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
#     url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^chaining/', include('smart_selects.urls')),
#     url(r'^adm/', include('adm.urls')),
#     # url(r'^admin/', include(admin.site.urls)),
# )

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
    # url(r'^ckeditor/', include('ckeditor.urls')),
    # url(r'^tinymce/', include('tinymce.urls')),
)