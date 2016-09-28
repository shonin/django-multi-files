from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^drinkinggourd/', include('drinking_gourd.urls', namespace='drinking_gourd')),
    url('^', include('django.contrib.auth.urls')),
]