#!/usr/bin/env python
# CLASSIFICATION NOTICE: This file is UNCLASSIFIED

from __future__ import print_function
import sys, os
import boto3
import json
from decimal import Decimal


## =============================================================================

os.environ['HTTP_PROXY'] = ''
os.environ['http_proxy'] = ''
PORT=8742

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dyn = boto3.resource('dynamodb',endpoint_url="http://localhost:"+str(PORT))

tableName='Dex'

dexTable = dyn.Table(tableName)

response = dexTable.scan()
for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))

print("table:", dexTable.name)
print("response:", response)

{u'trend': Decimal('8'), u'timestamp': Decimal('1495326471000'), u'value': Decimal('245'), u'ST': Decimal('1495337144000'), u'WT': Decimal('1495326471000'), u'DT': u'1495333623000-0700'}
{u'trend': Decimal('8'), u'timestamp': Decimal('1495326472000'), u'value': Decimal('245'), u'ST': Decimal('1495337144000'), u'WT': Decimal('1495326471000'), u'DT': u'1495333623000-0700'}




