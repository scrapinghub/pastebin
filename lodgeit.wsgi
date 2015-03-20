#!/usr/bin/env python
import codecs
from lodgeit import make_app

# http://stackoverflow.com/questions/21517358/django-mysql-unknown-encoding-utf8mb4
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

try:
    from local_settings import DBURI
except ImportError:
    DBURI = 'sqlite:////tmp/lodgeit.db'

application = make_app(dburi=DBURI, secret_key='useless')


if __name__ ==  '__main__':
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 5000, application)
