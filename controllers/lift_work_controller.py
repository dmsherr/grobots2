import connexion
import six

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.lift_work import LiftWork  # noqa: E501
from swagger_server import util


def get_lift_location_work_list(LocationId):  # noqa: E501
    """get_lift_location_work_list

    Returns a list of all lift work for a specific location. # noqa: E501

    :param LocationId: Specify the Location ID as a string in quotes.
    :type LocationId: int

    :rtype: LiftWork
    """
    return 'do some magic!'


def get_lift_work_list(LiftIPV6Id):  # noqa: E501
    """get_lift_work_list

    Returns a list of work for a specific lift ID. # noqa: E501

    :param LiftIPV6Id: Specify the Lift IPV6 address as a string in quotes.
    :type LiftIPV6Id: int

    :rtype: LiftWork
    """
    return 'do some magic!'
