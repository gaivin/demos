#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: Gaivin Wang
@license: Apache Licence
@contact: gaivin@outlook.com
@site: https://github.com/gaivin/
@software: PyCharm
@file: tasks.py
@time: 6/8/2018 3:43 PM
"""

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

