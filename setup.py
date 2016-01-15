from setuptools import setup

setup(name='dpaw-utils',
      version='0.3a3',
      description='Utilities for django/python apps',
      url='https://bitbucket.org/dpaw/dpaw-utils',
      author='Department of Parks and Wildlife',
      author_email='asi@dpaw.wa.gov.au',
      license='BSD',
      packages=['dpaw_utils','dpaw_utils.requests'],
      install_requires=["django", "requests", "bottle", "django-confy", "ipython",
          "django-extensions", "gevent", "django-uwsgi", "django-redis", "psycopg2"],
      zip_safe=False)

