import connexion
import six

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.lift_info import LiftInfo  # noqa: E501
from swagger_server import util


def get_lift_locations(STATUS):  # noqa: E501
    """get_lift_locations

    This operation returns a list of lifts and their location details  # noqa: E501

    :param STATUS: Specify the Lift STATUS as an integer. 0 &#x3D; inactive 1 &#x3D; active
    :type STATUS: int

    :rtype: LiftInfo
    """
    return 'do some magic!'


def get_starts(LOCATION):  # noqa: E501
    """get_starts

    Returns a list of lifts scheduled to start for a specific location. # noqa: E501

    :param LOCATION: Specify the value of the LOCATION ID as a string
    :type LOCATION: str

    :rtype: LiftInfo
    """
    return 'do some magic!'


def getlifts():  # noqa: E501
    """getlifts

    Returns a list of lifts based on the token entitlement scope of the client. # noqa: E501


    :rtype: LiftInfo
    """
    return 'do some magic!'
