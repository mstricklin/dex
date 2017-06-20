#!/usr/bin/env python
# CLASSIFICATION NOTICE: This file is UNCLASSIFIED

from __future__ import print_function
import sys, os
import boto3
import json
from DecimalEncoder import DecimalEncoder


## =============================================================================

os.environ['HTTP_PROXY'] = ''
os.environ['http_proxy'] = ''
PORT=8742

dyn = boto3.resource('dynamodb',endpoint_url="http://localhost:"+str(PORT))

tableName='Dex'

dexTable = dyn.Table(tableName)

response = dexTable.scan()
for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))


print()
print("table:", dexTable.name)
print("response:", response)



