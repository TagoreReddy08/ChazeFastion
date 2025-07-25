#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Default to ChazeFashion.settings for local dev or override via DJANGO_SETTINGS_MODULE
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChazeFashion.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and "
            "available on your PYTHONPATH environment variable. Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
