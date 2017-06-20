#!/usr/bin/env bash

SESS=${1}


curl -v \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "User-Agent: Dexcom Share/3.0.2.11 CFNetwork/711.2.23 Darwin/14.0.0" \
  -H "Content-Length: 0" \
  -X POST https://share1.dexcom.com/ShareWebServices/Services/Publisher/ReadPublisherLatestGlucoseValues?minutes=1440\&maxCount=10\&sessionId=${SESS}

echo
