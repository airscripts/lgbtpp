from gay import Gay
from lesbian import Lesbian
from bisexual import Bisexual
from transgender import Transgender
from queer import Queer
from questioning import Questioning
from intersex import Intersex
from asexual import Asexual
from aromantic import Aromantic
from agender import Agender
from plus import Plus

def is_gay(object):
    return isinstance(object, Gay)

def is_lesbian(object):
    return isinstance(object, Lesbian)

def is_bisexual(object):
    return isinstance(object, Bisexual)

def is_transgender(object):
    return isinstance(object, Transgender)

def is_queer(object):
    return isinstance(object, Queer)

def is_questioning(object):
    return isinstance(object, Questioning)

def is_intersex(object):
    return isinstance(object, Intersex)

def is_asexual(object):
    return isinstance(object, Asexual)

def is_aromantic(object):
    return isinstance(object, Aromantic)

def is_agender(object):
    return isinstance(object, Agender)

def is_plus(object):
    return isinstance(object, Plus)
