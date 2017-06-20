#!/usr/bin/env bash


curl -v \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "User-Agent: Dexcom Share/3.0.2.11 CFNetwork/711.2.23 Darwin/14.0.0" \
  -X POST https://share1.dexcom.com/ShareWebServices/Services/General/LoginPublisherAccountByName \
  -d '{"accountName":"strickli","applicationId":"d8665ade-9673-4e27-9ff6-92db4ce13d13","password":"Stricklin1"}' 

echo


# resp is sessionID (e.g.):
# e3e3e6a5-coolsessionid-bro
