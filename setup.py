# Don't force people to install distribute unless we have to.
try:
    from setuptools import setup, Feature
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, Feature

import sys

classifiers = """\
Intended Audience :: Developers
License :: OSI Approved :: Apache Software License
Development Status :: 4 - Beta
Natural Language :: English
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.2
Programming Language :: Python :: 3.3
Operating System :: MacOS :: MacOS X
Operating System :: Unix
Programming Language :: Python
Programming Language :: Python :: Implementation :: CPython
"""

description = 'Non-blocking MongoDB driver for Tornado'

long_description = open("README.rst").read()

major, minor = sys.version_info[:2]

kwargs = {}
if major >= 3:
    kwargs['use_2to3'] = True

packages = ['motor']
package_data = {}
if 'test' in sys.argv:
    sys.argv.remove('test')
    sys.argv.append('nosetests')
    package_data['test'] = ['certificates/*']

if 'nosetests' in sys.argv:
    packages.append('test')
    package_data['test'] = ['certificates/ca.pem', 'certificates/client.pem']

pymongo_url = (
    'https://github.com/mongodb/mongo-python-driver/archive/2.7rc0.tar.gz'
    '#egg=pymongo-2.7rc0')

setup(name='motor',
      version='0.1+',
      packages=packages,
      package_data=package_data,
      description=description,
      long_description=long_description,
      author='A. Jesse Jiryu Davis',
      author_email='jesse@mongodb.com',
      url='https://github.com/mongodb/motor/',
      install_requires=[
          'tornado >= 3.1',
          'greenlet >= 0.4.0',
          'pymongo == 2.7rc0',
      ],
      dependency_links=[pymongo_url],
      license='http://www.apache.org/licenses/LICENSE-2.0',
      classifiers=filter(None, classifiers.split('\n')),
      keywords=[
          "mongo", "mongodb", "pymongo", "gridfs", "bson", "motor", "tornado",
      ],
      # Use 'python setup.py test' or 'python setup.py nosetests' to test.
      setup_requires=['nose'],
      test_suite='nose.main',
      zip_safe=False,
      **kwargs)
