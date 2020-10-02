from setuptools import setup


setup(
    name='mscazurefunctionhelpers',
    version='0.1.0',
    description='Library of helpers for use with Azure Functions',
    url='https://github.com/test',
    author='AirWalk Consulting',
    author_email='info@airwalkconsulting.com',
    license='MIT',
    packages=['azurefunctionhelpers'],
    install_requires=['elastic-apm==5.9.0']
)
