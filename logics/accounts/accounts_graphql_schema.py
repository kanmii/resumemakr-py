# -*- coding: utf-8 -*-

import graphene
from graphene_django.types import ObjectType

from logics.accounts.accounts_types import (
    UserRegistrationError,
    USER_LOGIN_ERROR_MESSAGE,
)
from logics.accounts import AccountsLogic, user_to_jwt

from logics.logics_utils import TimestampsInterface


class User(ObjectType):
    class Meta:
        interfaces = (TimestampsInterface,)

    id = graphene.ID(required=True)
    jwt = graphene.String(required=True)
    name = graphene.String(required=True)
    email = graphene.String(required=True)

    def resolve_jwt(self, info):
        return user_to_jwt(self)


class RegistrationError(ObjectType):
    email = graphene.String()


class RegistrationInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    email = graphene.String(required=True)
    source = graphene.String(required=True)
    password = graphene.String(required=True)
    password_confirmation = graphene.String(required=True)


class LoginInput(graphene.InputObjectType):
    email = graphene.String(required=True)
    password = graphene.String(required=True)


class UserRegistrationMutation(graphene.Mutation):
    class Arguments:
        input = RegistrationInput(required=True)

    user = graphene.Field(User)
    errors = graphene.Field(RegistrationError)

    def mutate(self, info, **inputs):
        result = AccountsLogic.register_user_with_password(inputs["input"])

        if isinstance(result, UserRegistrationError):
            return UserRegistrationMutation(errors=result)

        return UserRegistrationMutation(user=result[0])


class UserSuccess(ObjectType):
    user = graphene.Field(User)


class LoginUserError(ObjectType):
    error = graphene.String(required=True)


class LoginUserPayload(graphene.Union):
    class Meta:
        types = (LoginUserError, UserSuccess)


class LoginMutation(graphene.Mutation):
    class Arguments:
        input = LoginInput(required=True)

    Output = LoginUserPayload

    def mutate(self, info, **inputs):
        result = AccountsLogic.login_with_password(inputs["input"])

        if result is None:
            return LoginUserError(error=USER_LOGIN_ERROR_MESSAGE)

        return UserSuccess(user=result[0])


class AccountsCombinedMutation(ObjectType):
    registration = UserRegistrationMutation.Field()
    login = LoginMutation.Field()
