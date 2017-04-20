from setuptools import setup

setup(name='dpaw-utils',
      version='0.3a15',
      description='Utilities for Django/Python apps',
      url='https://github.com/parksandwildlife/dpaw-utils',
      author='Department of Parks and Wildlife',
      author_email='asi@dpaw.wa.gov.au',
      license='BSD',
      packages=['dpaw_utils', 'dpaw_utils.requests'],
      install_requires=[
          'django<2', 'requests', 'bottle', 'django-confy', 'ipython<6', 'six',
          'django-extensions', 'gevent', 'django-uwsgi', 'django-redis', 'psycopg2'],
      zip_safe=False)
