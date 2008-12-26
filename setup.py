#!/usr/bin/env python
from distutils.core import setup

setup(name = "django-localize",
      version = '0.1',
      author = "Artiom Diomin",
      author_email = "kron82@gmail.com",
      url = "http://github.com/kron4eg/django-localize",
      license = "BSD",
      description = "Localize your django URLs",
      long_description = "Localization of django URLs with appending language prefix to it.",
      packages = ['localize'],
      platforms = ['any'],
      classifiers = [
          'Development Status :: 4 - Beta',
          'Framework :: Django',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ]
)

