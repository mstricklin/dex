#!/usr/bin/env python
# CLASSIFICATION NOTICE: This file is UNCLASSIFIED

from __future__ import print_function
import sys, os
import boto3


## =============================================================================

os.environ['HTTP_PROXY'] = ''
os.environ['http_proxy'] = ''
PORT=8742

dyn = boto3.resource('dynamodb',endpoint_url="http://localhost:"+str(PORT))

tableName='Dex2'
table = dyn.create_table(
    TableName=tableName,
    KeySchema=[
        {
            'AttributeName': 'value',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'timestamp',
            'KeyType': 'RANGE'  #Partition key
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'value',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'timestamp',
            'AttributeType': 'N'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
print("Table key_schema:", table.key_schema)



