import os
import re

def find_process(name):
    for d in os.listdir('/proc'):
        if not d.isdigit():
            continue
        try:
            exe = os.readlink(os.path.join('/proc', d, 'exe'))
        except OSError:
            continue
        if exe == name or os.path.basename(exe) == name:
            return int(d)
    else:
        raise EnvironmentError("Could not find a process with the name %s" % name)

def from_name(name, update=False):
    return from_pid(find_process(name), update)

def from_pid(pid, update=False):
    env = open(os.path.join('/proc/%d/environ' % pid)).read()
    env = dict([x.split('=', 1) for x in env.split('\x00') if x])
    if update:
       os.environ.update(env)
    return env

def to_csh(env, export=False):
    yield from _set(env, prefix='setenv ' if export else 'set ', infix=' ' if export else '=')

def to_sh(env, export=False):
    yield from _set(env, prefix='export ' if export else '', infix='=')

def _set(env, prefix, infix):
    for key, val in env.items():
        yield '%s%s%s"%s"' % (prefix, key, infix, re.sub(r'([\\$"`])', r'\\\1', val))
