import logging
import variable_admittance
import numpy as np
from config import get_config

config = get_config()
_LOGGER = logging.getLogger(__name__)


def main():
    _LOGGER.debug("here goes.")
    M_0 = np.eye(6)
    D_0 = np.eye(6)
    beta = 0.5
    epsilon = 0.5
    delta_t = 0.1
    delta_M = np.eye(6) * 0.1
    A = np.array([0.3, 0.3, 0.3, 0.04, 0.04, 0.02])
    paramater_adaption = variable_admittance.ParameterAdaption(M_0, D_0, beta, epsilon, delta_t, delta_M, A)

    paramater_adaption.reset_values()


if __name__ == '__main__':
    _LOGGER.debug('Starting')
    main()
