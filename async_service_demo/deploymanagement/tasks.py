from __future__ import absolute_import, unicode_literals
from celery import shared_task
from time import sleep

@shared_task(name="DeployAVE")
def deploy_ave(ip="10.98.137.54"):
    sleep(120)
    return ip


@shared_task(name="DeployAvamar")
def deploy_ads(ip="10.98.137.53"):
    sleep(60)
    return ip

