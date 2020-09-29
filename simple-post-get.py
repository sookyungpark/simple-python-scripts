#!/bin/sh
# python 3

import requests
import pprint
import json

from io import BytesIO
from time import sleep

PHASE = 'ALPHA'
SLEEP_SEC = 1

def syncApp(appId):
    moduleSyncPath = 'http://appsync.url.com'
    response = requests.post(moduleSyncPath, data={ "nameList": [ "MYAPP" ] }, headers={ 'Content-Type': 'application/json' })

def getAppIds():
    response = requests.get("http://appids.path.com")
    return json.loads(response.content)

def isValidAppId(appId):
    return appId != None and appId.isalnum()

def main():
    appIds = getAppIds()
    for appId in appIds:
        if isValidAppId(appId):
            print("start sync app: " + appId)
            syncApp(appId)
            print("sync app: " + appId + " done. sleep for " + str(SLEEP_SEC) + " sec.")
            sleep(SLEEP_SEC)
    print("site app sync for " + PHASE + " completed.")

main()
