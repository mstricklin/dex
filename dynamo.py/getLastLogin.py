#!/usr/bin/env python
# CLASSIFICATION NOTICE: This file is UNCLASSIFIED

from __future__ import print_function
import sys, os
import boto3
from boto3.dynamodb.conditions import Key, Attr
import json
from DecimalEncoder import DecimalEncoder
from decimal import Decimal
from pprint import pprint


## =============================================================================

os.environ['HTTP_PROXY'] = ''
os.environ['http_proxy'] = ''
PORT=8742

dyn = boto3.resource('dynamodb',endpoint_url="http://localhost:"+str(PORT))

tableName='config'

cfgTable = dyn.Table(tableName)

response = cfgTable.scan()
for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))



r = cfgTable.query(KeyConditionExpression=Key('key').eq('sessionID'))
print(r)
print(r['Count'])
print(r['Items'][0])
ll = r['Items'][0]
print(ll['value'])
print(ll['timestamp'])
pprint(ll)
