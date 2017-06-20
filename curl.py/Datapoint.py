#!/usr/bin/env python
# CLASSIFICATION NOTICE: This file is UNCLASSIFIED

from __future__ import print_function
import sys
import time
import json
from collections import namedtuple

## =============================================================================
DP = namedtuple('DP', 'TS DT WT ST Trend Value')

def make(DT=0, WT=0, ST=0, Trend=0, Value=100):
    now = int(time.time()*1000)
    return DP(TS=now, DT=DT, WT=WT, ST=ST, Trend=Trend, Value=Value)

def fromJson(jsonStr):
    return json.loads(jsonStr, object_hook=lambda x: make(**x))

def toJson(dp):
    return json.dumps(dp._asdict())


## =============================================================================



def test():
    data = """{"DT":"\/Date(1495333623000-0700)\/",
    "ST":"\/Date(1495337144000)\/",
    "Trend":8,
    "Value":245,
    "WT":"\/Date(1495326471000)\/"}"""

    dpa = make()
    print("dpa", dpa)
    dpb = fromJson(data)
    print("dpb", dpb)

    print("dpb", toJson(dpb))

