from django.conf.urls import url

from views import get_task_view, deploy_ave_view, deploy_ads_view

service_route = {'get': 'list', 'post': 'create'}

urlpatterns = [
    url('^task', get_task_view),
    url('^ads', deploy_ads_view),
    url('^ave', deploy_ave_view),
]
