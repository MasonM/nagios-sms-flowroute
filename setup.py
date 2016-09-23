#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='nagios-sms-flowroute',
    version='0.1',
    description='Nagios plugin to send SMS alerts via Flowroute',
    license='BSD',
    author='Mason Malone',
    author_email='mason.malone@gmail.com',
    url='http://github.com/MasonM/nagios-sms-flowroute/',
    scripts=['nagios_sms_flowroute.py'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: System :: Monitoring',
    ],
)

