#!/usr/bin/env python
# CLASSIFICATION NOTICE: This file is UNCLASSIFIED

from __future__ import print_function
import os
import boto3

os.environ['HTTP_PROXY'] = ''
os.environ['http_proxy'] = ''
PORT=8742

dynResource = boto3.resource('dynamodb', endpoint_url="http://localhost:"+str(PORT))

[t.delete() for t in dynResource.tables.all()]
