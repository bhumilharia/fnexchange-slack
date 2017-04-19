# This documentation is in the reStructuredText format. More details about writing
# rst docs can be found here:
#   http://docutils.sourceforge.net/docs/user/rst/quickref.html
#
# Instructions for packaging and distributing python packages can be found here:
#    Doc: https://packaging.python.org/distributing/
#    Sample: https://github.com/pypa/sampleproject/blob/master/setup.py

"""
Overview
========
This is a plugin for the fnExchange API router for interacting with Slack.

This plugin currently only provides an Action for posting messages to a Slack
channel using inbound webhooks. This only requires the inbound webhook URL token.

More details about this plugin can be found `here <http://github.com/bhumilharia/fnexchange-slack>`_

More Information
================
fnExchange installation and usage instructions can be found on the project's
`GitHub page <http://github.com/dnif/fnExchange>`_

fnExchange sample plugin project and development instructions can be found at
`fnExchange-sample-plugin github <http://github.com/dnif/fnExchange-sample-plugin>`_
"""

from setuptools import setup, find_packages

setup(
    # name of package on PyPi
    name='fnexchange-slack',
    version='1.0.0',

    # URL to your repo (if open source)
    url='http://github.com/bhumilharia/fnexchange-slack',

    license='Apache',

    # your name
    author='Bhumil Haria',

    # your email here
    author_email='bhumilharia@gmail.com',
    description='A sample fnExchange plugin',
    long_description=__doc__,
    keywords='fnexchange plugin',

    # if cross-platform
    platforms='any',

    # add your dependencies here
    install_requires=[
        'fnexchange',
        'requests>=2.4.2',
    ],

    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers for a full list
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
