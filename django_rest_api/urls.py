from django.conf.urls import include, url, patterns
from django.contrib.auth.models import User
from django.conf.urls import include

from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = patterns('',
    url(r'^', include('snippets.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^$', TemplateView.as_view(template_name='index.html')),
)
