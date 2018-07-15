import connexion
import six

from swagger_server.models.err import Err  # noqa: E501
from swagger_server.models.lift_info import LiftInfo  # noqa: E501
from swagger_server import util


def get_scheduled_starts():  # noqa: E501
    """get_scheduled_starts

    Returns the list of lifts scheduled to start next. # noqa: E501


    :rtype: LiftInfo
    """
    return 'do some magic!'
