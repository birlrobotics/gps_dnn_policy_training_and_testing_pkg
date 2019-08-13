#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=[
        'gps_dnn_policy_training_and_testing_pkg',
    ],
    package_dir={'': 'src'},
)

setup(**setup_args)
