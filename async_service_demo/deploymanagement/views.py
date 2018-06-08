# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .tasks import deploy_ads, deploy_ave

from libs.django_utils import validate_request
from libs.django_celery_utils import get_task_info


# Create your views here.

@validate_request(types=["POST"], view_return="object")
def deploy_ave_view(request, ip):
    result = {"status": "START_FAILED", "task_id": None,
              "comments": "Test task start failed"}

    test_task_result = deploy_ave.delay(ip=ip)
    comments = "Test task initialized"
    result.update(status=test_task_result.status, task_id=test_task_result.id, comments=comments)
    return result


@validate_request(types=["POST"], view_return="object")
def deploy_ads_view(request, ip):
    result = {"status": "START_FAILED", "task_id": None,
              "comments": "Test task start failed"}
    test_task_result = deploy_ads.delay(ip=ip)
    comments = "Test task initialized"
    result.update(status=test_task_result.status, task_id=test_task_result.id, comments=comments)
    return result


@validate_request(types=["GET"], view_return="object")
def get_task_view(request, task_id):
    task = get_task_info(task_id=task_id)
    if task:
        result = {"status": 0, "task_info": task}
    else:
        result = {"status": 1, "comments": "The task_id [%s] is not valid." % task_id}
    return result
