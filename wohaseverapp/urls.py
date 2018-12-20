from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views as core_views
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^question/', views.search_results,name='question'),
    url(r'^category/', views.search_category,name='category'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    # urlpatterns=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    