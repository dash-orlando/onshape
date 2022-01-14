from onshape_client.oas.api_client import ApiClient
from onshape_client.client import Client
import json

# Objects
client = Client()

# Variables
did     = "f3aa9da213f80c828db344b4"
wvm     = "w"
wvmid   = "18666aab92f5056d10b09fd2"
eid     = "f237e7ebb9aee86dd078ece2"

# Process
print(client.configuration.api_key)

URL="{}/api/elements/d/{}/{}/{}/e/{}/configuration".format(client.configuration.host,did,wvm,wvmid,eid)
print(URL)

result = client.api_client.request(
        method="GET",
        url=URL,
        headers={
            "Accept": "application/vnd.onshape.v1+json;charset=utf-8;qs=0.1, application/json;charset=utf-8; qs=0.09"
        },
        query_params={},
    )


result = json.loads(result.data)
print(result["configurationParameters"][0]["message"]["rangeAndDefault"]["message"]["defaultValue"])

payload = result
payload["configurationParameters"][0]["message"]["rangeAndDefault"]["message"]["defaultValue"] = 80.00

postURL="{}/api/elements/d/{}/{}/{}/e/{}/configuration".format(client.configuration.host,did,wvm,wvmid,eid)
result = client.api_client.request(
        method="POST",
        url=postURL,
        headers={
            "Accept": "application/vnd.onshape.v1+json;charset=utf-8;qs=0.1, application/json;charset=utf-8; qs=0.09"
        },
        query_params={},
        body=payload,
    )

result = json.loads(result.data)
print(result["configurationParameters"][0]["message"]["rangeAndDefault"]["message"]["defaultValue"])