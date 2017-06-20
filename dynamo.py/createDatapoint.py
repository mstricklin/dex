#!/usr/bin/env python
# CLASSIFICATION NOTICE: This file is UNCLASSIFIED

from __future__ import print_function
import sys, os
import boto3
from boto3.dynamodb.types import NUMBER
from time import time
from collections import namedtuple
from pprint import pprint


## =============================================================================

os.environ['HTTP_PROXY'] = ''
os.environ['http_proxy'] = ''
PORT=8742

dynResource = boto3.resource('dynamodb', endpoint_url="http://localhost:"+str(PORT))

# TS DT WT ST Trend Value

print( list(dynResource.tables.all()) )

tableName='datapoint'
table = dynResource.create_table(
    TableName=tableName,
    KeySchema=[
        { 'KeyType': 'HASH',  'AttributeName': 'Value' },
        { 'KeyType': 'RANGE', 'AttributeName': 'timestamp' }
    ],
    AttributeDefinitions=[
        { 'AttributeName': 'Value',     'AttributeType': 'N' },
        { 'AttributeName': 'timestamp', 'AttributeType': 'N' },
    ],
    LocalSecondaryIndexes=[
            {
                'IndexName': 'timestamp-idx',
                'KeySchema': [
                    { 'KeyType': 'HASH',  'AttributeName': 'Value' },
                    { 'KeyType': 'RANGE', 'AttributeName': 'timestamp' }
                ],
                'Projection': { 'ProjectionType': 'KEYS_ONLY' }
            }
        ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10
    }
)

print("table:", table)
print("Table key_schema:", table.key_schema)

# https://gist.github.com/parijatmishra/6560564a681c17e5ecf6
# table = dynamodb.Table('videos')
# video_id = 25
# response = table.query(
    # IndexName='video_id-index',
    # KeyConditionExpression=Key('video_id').eq(video_id)
# )

print("table:", table)
print("Table key_schema:", table.key_schema)

now = int(time() * 1000)
DP = namedtuple('DP', 'timestamp DT WT ST Trend Value')
for i in xrange(0, 10):
    dp = {'timestamp': now-(i*10000), 'DT': "14", "WT":"24", "ST":"34", "Trend":"8", "Value":99+i}
    print(dp)
    table.put_item( Item=dp )


