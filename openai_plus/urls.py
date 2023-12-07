from django.urls import path, re_path
from openai_plus.views import query, default, errors
from django.conf.urls import handler404, handler500
# urls.py


handler404 = errors.custom_error_404
handler500 = errors.custom_error_500


urlpatterns = [
    path('', default.DefaultViewSet.as_view(), name='query'),
    re_path('query/(?P<value>\d+)/?$', query.QueryViewSet.as_view(), name='query'),
]