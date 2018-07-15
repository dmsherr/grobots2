import connexion
import six

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.lift_info import LiftInfo  # noqa: E501
from swagger_server import util


def updateliftinfo(LiftIPV6Id):  # noqa: E501
    """updateliftinfo

    Update Lift Information # noqa: E501

    :param LiftIPV6Id: Specify the Lift IPV6 address as a string in quotes.
    :type LiftIPV6Id: str

    :rtype: LiftInfo
    """
    return 'do some magic!'
