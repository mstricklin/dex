#!/usr/bin/env python

from __future__ import print_function
import json


#x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

def zunserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)   # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d
def unserialize_object(d):
    print("unserialize_object")
    for key, value in d.items():
        #setattr(obj, key, value)
        print(key, " => ", value)

data = """[{"DT":"\/Date(1495333623000-0700)\/",
"ST":"\/Date(1495337144000)\/",
"Trend":8,
"Value":245,
"WT":"\/Date(1495326471000)\/"}]"""

print(data)
print()

a = json.loads(data, object_hook=unserialize_object)
