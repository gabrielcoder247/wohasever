from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views as core_views
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^signup/$', core_views.signup, name='signup'),
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)