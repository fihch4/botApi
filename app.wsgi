#!/usr/bin/python
import sys

sys.path.insert(0, "/var/www/ibotapi/")
from app import app as application
application.secret_key = 'tech'