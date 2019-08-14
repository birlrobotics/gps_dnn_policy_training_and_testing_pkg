import sys
import os
import gps_agent_pkg
sys.path.append(os.path.join(
    os.sep.join(gps_agent_pkg.__path__[0].split(os.sep)[:-7]),
    'python',
))

from gps.algorithm.policy.policy import Policy
import numpy as np

class DnnPolicy(Policy):
    def __init__(self, dU):
        Policy.__init__(self)
        self.dU = dU

    def act(self, x, obs, t, noise):
        return np.random.rand(self.dU)
