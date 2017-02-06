from setuptools import setup

requirements = ('requests')
setup(
    name='payfort-python',
    packages=['payfort'],
    version='0.0.1',
    description='Payfort Python bindings',
    install_requires=requirements,
)
