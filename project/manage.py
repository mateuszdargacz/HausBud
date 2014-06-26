#!/usr/bin/env python
import os
import sys
from os.path import abspath, dirname

if __name__ == "__main__":
    SITE_ROOT = dirname(dirname(abspath(__file__)))
    APPS_ROOT = os.path.join(dirname(abspath(__file__)), 'apps')
    sys.path.append(SITE_ROOT)
    sys.path.append(APPS_ROOT)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
