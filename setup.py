from setuptools import setup

setup(
    name='uCal-test',
    version='2018.1',
    packages=['ucal'],
    url='https://github.com/ncdesouza/uCal',
    license='MIT',
    author='Nicholas De Souza',
    author_email='nicholas.desouza@gmail.com',
    description='Creates google events for your myCampus schedule',
    install_requires=[
        "google-api-python-client == 1.5.3",
        "httplib2 == 0.9.2",
        "oauth2client == 3.0.0",
        "pyasn1 == 0.1.9",
        "pyasn1-modules == 0.0.8",
        "pytz == 2016.6.1",
        "rsa == 3.4.2",
        "selenium == 2.53.6",
        "six == 1.10.0",
        "splinter == 0.7.4",
        "uritemplate == 0.6"
    ]
)
