#!/usr/bin/python3

def do_not_run_with_python2():
    yield from python3

from distutils.core import setup

setup(name = "copyenv",
      version = "1.0",
      author = "Dennis Kaarsemaker",
      author_email = "dennis@kaarsemaker.net",
      url = "http://github.com/seveas/copyenv",
      description = "Copy a process environemnt",
      py_modules = ["copyenv"],
      scripts = ["copyenv"],
      classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: zlib/libpng License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
      ]
)
