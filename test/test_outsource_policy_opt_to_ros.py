import rospy
import sys
import os
import gps_agent_pkg
sys.path.append(os.path.join(
    os.sep.join(gps_agent_pkg.__path__[0].split(os.sep)[:-7]),
    'python',
))

from gps.algorithm.policy_opt.outsource_policy_opt_to_ros import OutsourcePolicyOptToROS

import numpy as np

if __name__ == '__main__':
    rospy.init_node('test')
    hyperparams = {}
    dO = 32
    dU = 32
    N = 10
    T = 100
    ospotr = OutsourcePolicyOptToROS(
        hyperparams,
        dO,
        dU,
    )

    obs = np.zeros((N, T, dO))
    tgt_mu = np.zeros((N, T, dU))
    tgt_prc = np.zeros((N, T, dU, dU))
    tgt_wt = np.zeros((N, T))
    ospotr.update(obs, tgt_mu, tgt_prc, tgt_wt)
