from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^contact/', views.contactpage, name='contactpage'),
    url(r'^alt-home/', views.alt_homepage, name='alt_homepage'),
    url(r'^page/', views.simplepage, name='simplepage'),
    url(r'^favorites/', views.favoritespage, name='favoritespage'),
    url(r'^authors/author(?P<pk>[0-9]+)/$', views.author_detail, name='author_detail'),
    url(r'^authors/adminauthor', views.admin_author_detail, name='admin_author_detail'),
    url(r'^posts/post(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^posts/adminpost', views.admin_post_detail, name='admin_post_detail'),
    url(r'^categories/category(?P<pk>[0-9]+)/$', views.category_detail, name='category_detail'),
    url(r'^categories/', views.categories, name='categories'),
    url(r'^post-sidebar/', views.post_sidebar, name='post_sidebar'),
   ]
#for media
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT,}),
    ]