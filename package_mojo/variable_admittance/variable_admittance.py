import logging
import numpy as np
from datetime import datetime

_LOGGER = logging.getLogger(__name__)


class ParameterAdaption:

    def __init__(self, M_0, D_0, beta, epsilon, delta_t, delta_M, A):
        _LOGGER.debug("Initialize.")
        self.n = max(M_0.shape)  # DOF`s in task space

        self.M_0 = M_0  # Desired inertia matrix
        self.D_0 = D_0  # Desired damping matrix
        self.beta = beta  # Forgetting factor
        self.epsilon = epsilon  # Oscillation detection threshold
        self.delta_t = delta_t  # Discrete time step
        self.delta_M = delta_M  # Maximum allowed inertia variation matrix
        self.A = A  # Vector of weights to distribute energy

        self.time_utc_initialized = datetime.utcnow().isoformat()

        self.k = 0  # Counts of instances above threshold
        self.zeta_0 = 0  # First time instance. TODO: consider using time_utc_initialized
        self.zeta = {self.zeta_0}  # instances in time of detected oscillations
        self.S_0 = np.zeros((self.n, self.n))  # Matrix of inertia variation

        self.R_d_0 = np.linalg.inv(self.M_0)*self.D_0  # Damping to inertia ratio

        self.__sanity_check_inputs()

        self.x = None  # Measured pose
        self.x_bar = None  # Compliant frame
        self.x_hat = None  # Deviance

        self.x_dot = None
        self.x_bar_dot = None
        self.x_hat_dot = None

        self.x_Ddot = None
        self.x_bar_Ddot = None
        self.x_hat_Ddot = None

    def __sanity_check_inputs(self):
        if not max(self.D_0.shape) == self.n \
                or not len(self.A) == self.n \
                or not np.sum(self.A) == 1.0 \
                or not (0.0 <= self.beta <= 1.0):
            _LOGGER.error("Inputs are insane!")
            raise ValueError

    def reset_values(self):
        _LOGGER.debug("Reset values.")
        self.k = 0
        self.zeta_0 = 0
        # self.zeta = {self.zeta}
        self.S_0 = np.zeros((self.n, self.n))
        return True

    def update(self, x, current_delta_t):
        self.x_Ddot = self.x_dot - (self.x - x)/current_delta_t
        self.x_dot = (self.x - x) / current_delta_t

        self.x_bar_Ddot = None

        self.x_hat_Ddot = None

        self.x_bar_dot = None
        self.x_hat_dot = None

        self.x = x
        self.x_bar = 0
        self.x_hat = self.x_bar - self.x

    def compute_detection_index(self):
        self.psi = np.linalg.norm()
