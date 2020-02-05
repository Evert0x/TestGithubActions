from setuptools import setup

setup(
    name="Testing",
    version="0.1.1",
    install_requires=[
        "wheel"
    ],
    packages=[
        "TestGithub"
    ],
    extras_require={
        'test': [
            'pytest'
        ]
    }
)
