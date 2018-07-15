import connexion
import six

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.o_auth_token import OAuthToken  # noqa: E501
from swagger_server.models.success import Success  # noqa: E501
from swagger_server import util


def get_auth_code(grant_type, client_id, redirect_uri):  # noqa: E501
    """get_auth_code

    Request a temporary code for the desired API Access Token Scope(s) # noqa: E501

    :param grant_type: value &#x3D; authorization_code
    :type grant_type: str
    :param client_id: a valid OAuth2 client id registered to the app authorized to use the API is required (this changes with each app store version iteration)
    :type client_id: str
    :param redirect_uri: App Callback URI
    :type redirect_uri: str

    :rtype: Success
    """
    return 'do some magic!'


def get_token_request(grant_type, client_id, client_secret):  # noqa: E501
    """get_token_request

    Applications request an implicit token with a client id and secret prior to user authentication # noqa: E501

    :param grant_type: value &#x3D; implicit
    :type grant_type: str
    :param client_id: a valid  OAuth2 client id registered to the app authorized to use the API is required (this changes with each app store version iteration)
    :type client_id: str
    :param client_secret: the client secret associated to the app client id (this changes with each app store version iteration)
    :type client_secret: str

    :rtype: OAuthToken
    """
    return 'do some magic!'


def post_token_request():  # noqa: E501
    """post_token_request

    Authorization Code grant types require a POST to the token endpoint after a GET for Authorization code. # noqa: E501


    :rtype: OAuthToken
    """
    return 'do some magic!'
