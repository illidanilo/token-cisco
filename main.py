import requests
import json

url = "https://10.10.20.14/api/aalogin.json"
body = {
    "aaaUSer":{
        "attributes":{
            "name":"admin",
            "pwd":"Cisco12345"
        }
    }
}
cabecera = {
    "Content.Type":"application/json"
}
requests = requests.post(url, headers=cabecera, data=body, verify=False)

