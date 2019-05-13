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
@time: 4/23/2019 5:41 PM
"""
import graphene
from graphene_django import DjangoObjectType

from .models import User, Post


class UserType(DjangoObjectType):
    class Meta:
        model = User


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class Query(graphene.ObjectType):
    user = graphene.List(UserType, id=graphene.ID())
    post = graphene.List(PostType, first=graphene.Int())

    def resolve_user(self, info, id=0):
        if id == 0:
            return User.objects.all()
        else:
            return User.objects.filter(id=id)
    def resolve_post(self, info, first=10):
        return Post.objects.all()[0:first]


class CreateUser(graphene.Mutation):
    id = graphene.Int()
    firstName = graphene.String()
    lastName = graphene.String()

    class Arguments:
        firstName = graphene.String()
        lastName = graphene.String()

    def mutate(self, info, firstName, lastName):
        user = User(first_name=firstName, last_name=lastName)
        user.save()

        return CreateUser(
            id=user.id,
            firstName=user.first_name,
            lastName=user.last_name,
        )


class Mutation(graphene.ObjectType):
    createUser = CreateUser.Field()
