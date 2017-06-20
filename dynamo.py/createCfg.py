#!/usr/bin/env python
# CLASSIFICATION NOTICE: This file is UNCLASSIFIED

from __future__ import print_function
import sys, os, time
import boto3
from boto3.dynamodb.conditions import Key, Attr


## =============================================================================

os.environ['HTTP_PROXY'] = ''
os.environ['http_proxy'] = ''
PORT=8742

dynResource = boto3.resource('dynamodb', endpoint_url="http://localhost:"+str(PORT))

print( list(dynResource.tables.all()) )

# dynClient.table is a dict
# dynResource.table is a boto3.resources.factory.dynamodb.Table

tableName='config'
table = dynResource.create_table(
    TableName=tableName,
    KeySchema=[
        {
            'AttributeName': 'key',
            'KeyType': 'HASH'  #Partition key
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'key',
            'AttributeType': 'S'
        },
    ],
    # TODO: not sure where to set these...
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("table:", table)
print("Table key_schema:", table.key_schema)

now = int(time.time() * 1000)
table.put_item( Item={ 'key': 'sessionID', 'value': 'e3e3e6a5-coolsessionid-bro-0', 'timestamp': now })
print(now)

now = int(time.time() * 1000)
table.put_item( Item={ 'key': 'sessionID', 'value': 'e3e3e6a5-coolsessionid-bro-1', 'timestamp': now }, ConditionExpression=Attr('key').eq('sessionID'))
print(now)
