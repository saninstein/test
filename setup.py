from setuptools import setup, find_packages
from pip._internal.network.session import PipSession
from pip._internal.req import parse_requirements

pip_session = PipSession()


def parse_reqs(path):
    return [str(r.req) for r in parse_requirements(path, session=pip_session)]


setup(
    name='simple-sum',
    version="0.0.1",
    author="Alex Bibik",
    author_email="saninstein@gmail.com",
    description="simple sum",
    long_description="""
    # simplesum
    Just a sum)
    """,
    long_description_content_type="text/markdown",
    url="https://github.com/saninstein/test",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=find_packages(include=["simplesum*"]),
    extras_require={
        "dev": parse_reqs("requirements.txt"),
    },
)
