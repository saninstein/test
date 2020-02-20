import os
import sys
from setuptools import setup, find_packages
from pip._internal.network.session import PipSession
from pip._internal.req import parse_requirements

pip_session = PipSession()


def parse_reqs(path):
    return [str(r.req) for r in parse_requirements(path, session=pip_session)]


setup(
    name='simplesum',
    packages=find_packages(include=["simplesum*"]),
    extras_require={
        "dev": parse_reqs("requirements.txt"),
    },
)
