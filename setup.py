import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-featureflags',
    version='0.1',
    packages=['featureflags'],
    include_package_data=True,
    license='Apache License',  # example license
    description='A feature flags module for Django that allows you to quickly disable features on a site.',
    long_description=README,
    url='https://github.com/gregbaker/django-featureflags',
    author='Greg Baker',
    author_email='ggbaker@sfu.ca',
    classifiers=[
	'Development Status :: Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

