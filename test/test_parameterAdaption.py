import numpy as np
import unittest
from .context import package_mojo


class TestParameterAdaption(unittest.TestCase):

    def setUp(self):
        M_0 = np.eye(6)
        D_0 = np.eye(6)
        beta = 0.5
        epsilon = 0.5
        delta_t = 0.1
        delta_M = np.eye(6) * 0.1
        A = np.array([0.3, 0.3, 0.3, 0.04, 0.04, 0.02])

        self.parameter_adaption = package_mojo.ParameterAdaption(M_0, D_0, beta, epsilon, delta_t, delta_M, A)

    def test_reset_values(self):
        self.assertTrue(self.parameter_adaption.reset_values())

    def test_update(self):
        self.assertTrue(True)
        # self.fail(msg="Needs test.")

    def test_compute_detection_index(self):
        self.assertTrue(True)
        self.fail(msg="Needs test.")


if __name__ == '__main__':
    unittest.main()
