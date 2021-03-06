# -*- coding: utf-8 -*-

import pytest
from graphene.test import Client

from logics.accounts.accounts_types import (  # noqa
    ATTRIBUTE_NOT_UNIQUE_ERROR_MESSAGE,
    USER_LOGIN_ERROR_MESSAGE,
)
from logics.accounts import (
    AccountsLogic,  # noqa
    user_params_to_graphql_variable,
)

pytestmark = pytest.mark.django_db


def test_register_with_password_succeeds(
    graphql_client: Client, user_registration_query: str, create_user_params
) -> None:  # noqa
    variables = {"input": user_params_to_graphql_variable(create_user_params)}

    result = graphql_client.execute(
        user_registration_query, variables=variables
    )  # noqa

    registration = result["data"]["registration"]
    user = registration["user"]

    assert user["email"] == create_user_params["email"]
    assert type(user["jwt"]) == str
    assert registration["errors"] is None


def test_register_with_password_fails_cos_email_not_unique(
    graphql_client: Client,
    user_registration_query: str,
    registered_user,
    create_user_params,
) -> None:  # noqa
    variables = {"input": user_params_to_graphql_variable(create_user_params)}

    result = graphql_client.execute(
        user_registration_query, variables=variables
    )  # noqa

    registration = result["data"]["registration"]

    assert registration["errors"]["email"] == ATTRIBUTE_NOT_UNIQUE_ERROR_MESSAGE
    assert registration["user"] is None


def test_login_user_with_password_succeeds(
    login_query, graphql_client, registered_user, create_user_params
):
    login_params = {"email": "a@b.com", "password": "nicePWord"}

    result = graphql_client.execute(
        login_query, variables={"input": login_params}
    )  # noqa

    user = result["data"]["login"]["user"]

    assert user["email"] == create_user_params["email"]
    assert type(user["jwt"]) == str


def test_login_user_with_password_fails_cos_wrong_password(
    login_query, graphql_client, registered_user, create_user_params
):  # noqa
    login_params = {"email": "a@b.com", "password": "bogusPassword"}

    result = graphql_client.execute(
        login_query, variables={"input": login_params}
    )  # noqa

    error = result["data"]["login"]["error"]

    assert error == USER_LOGIN_ERROR_MESSAGE


def test_login_user_with_password_fails_cos_user_not_found(
    registered_user, create_user_params
):
    login_params = {"email": "b@b.com", "password": "nicePassword"}
    result = AccountsLogic.login_with_password(login_params)
    assert result is None


def test_user_by_id_succeeds(registered_user):
    user = AccountsLogic.get_user_by_id(registered_user.id)
    assert user.email == registered_user.email  # type: ignore


def test_user_by_id_returns_none_cos_user_does_not_exist(bogus_uuid):
    assert AccountsLogic.get_user_by_id(bogus_uuid) is None
