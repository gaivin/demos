#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Gaivin Wang 
@license: Apache Licence  
@contact: gaivin@outlook.com
@site:  
@software: PyCharm 
@file: schema.py 
@time: 4/28/2019 2:21 PM 
"""

import graphene

import moments.schema


class Query(moments.schema.Query):
    pass


class Mutation(moments.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)