from setuptools import setup

setup(name='dpaw-utils',
      version='0.4.3',
      description='Utilities for Django/Python apps',
      url='https://github.com/dbca-wa/dpaw-utils',
      author='Department of Biodiversity, Conservation and Attractions',
      author_email='asi@dbca.wa.gov.au',
      license='BSD',
      packages=['dpaw_utils', 'dpaw_utils.requests'],
      zip_safe=False)
