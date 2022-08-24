import base64
import json
import requests
from key import key

sign_server_host = "https://sign-tt-xiheqqvsqx.us-west-1.fcapp.run"


def do_tt_encrypt(data: str) -> bytes:
    """
    :param :data device info json string
    :return ttEncrypt data
    """
    url = f"{sign_server_host}/tt_encrypt"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "key": key,  # Contact us for secret key
        "data": base64.b64encode(data.encode()).decode(),
    })
    print(payload)
    response = requests.post(url, headers=headers, data=payload)
    print(response.status_code)
    print(response.text)
    if response.status_code == 200:
        obj = json.loads(response.text)
        return base64.b64decode(obj["data"].encode())
