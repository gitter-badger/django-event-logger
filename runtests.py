import os
import sys
from django.conf import settings

DIRNAME = os.path.dirname(__file__)
settings.configure(DEBUG=True,
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.postgresql_psycopg2',
                           'NAME': 'travis_ci',
                           'USER': 'postgres',
                           'HOST': 'localhost',
                       }
                   },
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.admin',
                                   'events',
                                   'events.tests',))
try:
    # Django <= 1.8
    from django.test.simple import DjangoTestSuiteRunner

    test_runner = DjangoTestSuiteRunner(verbosity=1)
except ImportError:
    # Django >= 1.8
    from django.test.runner import DiscoverRunner

    test_runner = DiscoverRunner(verbosity=1)
failures = test_runner.run_tests(['events', ], verbosity=1)
if failures:
    sys.exit(failures)
