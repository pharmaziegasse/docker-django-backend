from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from esite.user.models import User
from esite.customer.models import Customer

class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude_fields = ['password']


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username=username,
            email=email,
        )

        if info.context.user.is_anonymous:
            raise GraphQLError('You must be logged to create a user')

        if not info.context.user.is_superuser:
            raise GraphQLError('You must be superuser to create a user')

        user.set_password(password)
        user.save()
        # saved to our user objects as a wagtail user

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(graphene.ObjectType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)
    customers = graphene.List(UserType)

    # List all Users
    def resolve_users(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged to list a user')
        if not user.is_superuser:
            raise Exception('You must be superuser to list a user')
        return User.objects.all()

    # List all Customers
    def resolve_customers(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged to list customer')
        if not user.is_superuser:
            raise Exception(f'You must be superuser to list customer {user.is_superuser}')
        return Customer.objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('You must be logged')
        return user
