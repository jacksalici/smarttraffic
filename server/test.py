import json
import requests as re

offset=0
limit=100
refine="refine.comune=PORTO+GARIBALDI"

stations = []

while True:
    href=f'https://opendata.comune.bologna.it/api/v2/catalog/datasets/tper-fermate-autobus/records?limit={limit}&offset={offset}&refine=quartiere%3A%22Santo%20Stefano%22&timezone=UTC'
    res = json.loads(re.get(href).text)
    print(res)
    for record in res["records"]:
        field = record["record"]["fields"]
        station = {
            "name": field["denominazione"],
            "code": field["codice"],
            "coord": [field["geopoint"]["lat"],field["geopoint"]["lon"]]
        }
        stations.append(station)

    mylen = int(res["total_count"])
    if len(stations) == mylen:
        break
    else:
        print(len(stations))

    offset+=limit

print(stations)
with open("busStopDatasetBologna.json", "w") as f:
    json.dump(stations, f)