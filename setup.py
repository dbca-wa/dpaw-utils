from setuptools import setup

setup(name='dpaw-utils',
      version='0.4.1',
      description='Utilities for Django/Python apps',
      url='https://github.com/parksandwildlife/dpaw-utils',
      author='Department of Parks and Wildlife',
      author_email='asi@dbca.wa.gov.au',
      license='BSD',
      packages=['dpaw_utils', 'dpaw_utils.requests'],
      zip_safe=False)
