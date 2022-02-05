from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include(('home.urls', 'home'), namespace="home")),
    path('', include(('account.urls', 'account'), namespace='account')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
