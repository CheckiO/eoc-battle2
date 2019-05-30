from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "check"
    FUNCTION_NAMES = {
        "python_3": "check",
        "js_node": "check"
    }
    ENV_COVERCODE = {
        
    }