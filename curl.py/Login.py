#!/usr/bin/env python
# CLASSIFICATION NOTICE: This file is UNCLASSIFIED

from __future__ import print_function
import sys
import time
import requests


#curl -v \
  #-H "Accept: application/json" \
  #-H "Content-Type: application/json" \
  #-H "User-Agent: Dexcom Share/3.0.2.11 CFNetwork/711.2.23 Darwin/14.0.0" \
  #-X POST https://share1.dexcom.com/ShareWebServices/Services/General/LoginPublisherAccountByName \
  #-d '{"accountName":"strickli","applicationId":"d8665ade-9673-4e27-9ff6-92db4ce13d13","password":"Stricklin1"}'

#url = 'https://share1.dexcom.com/ShareWebServices/Services/General/LoginPublisherAccountByName'
#headers = {'Content-Type': "application/json",
#          'Accept': "application/json",
#          'User-Agent': 'Dexcom Share/3.0.2.11 CFNetwork/711.2.23 Darwin/14.0.0'}
#data = "{'accountName':'strickli','applicationId':'d8665ade-9673-4e27-9ff6-92db4ce13d13','password': 'Stricklin1'}"
#res = requests.post(url, json=data, headers=headers)

## =============================================================================
class Login(object):
    def __init__(self):
        now = int(time.time())
        print("foo", now)


l = Login()
