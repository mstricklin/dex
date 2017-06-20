#!/usr/bin/env python
# CLASSIFICATION NOTICE: This file is UNCLASSIFIED

from __future__ import print_function
import sys, os, time
import boto3



## =============================================================================

os.environ['HTTP_PROXY'] = ''
os.environ['http_proxy'] = ''
PORT=8742

dyn = boto3.resource('dynamodb',endpoint_url="http://localhost:"+str(PORT))

tableName='Dex'

dexTable = dyn.Table(tableName)

now = int(time.time() * 1000)
response = dexTable.put_item(
        Item={ 'timestamp': 1495326473000,
               'value': 245,
               'trend': 8,
               'ts' : {
                   'PT': now,
                   'DT': "1495333623000-0700",
                   'ST': 1495337144000,
                   'WT': 1495326471000,
               }
             }
)


print("table:", dexTable.name)
print("response:", response)



