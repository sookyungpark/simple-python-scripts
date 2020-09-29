import requests
import json
import time
import datetime

INPUT_DATA_DIR='datas/input-data'
OUTPUT_DATA_DIR='datas/input-data'

THRESHOLD_DATETIME = datetime.datetime(2019, 5, 1, 0, 0)
APPS=["MYAPP", "MYAPP2"]

for app in APPS:
    with open(INPUT_DATA_DIR + "/" + app + ".json", 'r') as f:
        rawData = json.load(f)
        with open(OUTPUT_DATA_DIR + "/" + app + ".txt", 'w') as wf:
            for k in rawData['datakey1']:
                pkg = rawData['datakey1'][k]            
                toDate = THRESHOLD_DATETIME
                try:
                    toDate = datetime.datetime.strptime(pkg['toDate'], '%Y-%m-%dT%H:%M:%SZ')
                except:
                    pass
                try:
                    toDate = datetime.datetime.strptime(pkg['toDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
                except:
                    pass
                if toDate < THRESHOLD_DATETIME:
                    print(app + "::" + promotionId + "::" + packageId + "\t\t\t# toDate: " + pkg['toDate'])
                    # wf.write(pkg)

print('done')
