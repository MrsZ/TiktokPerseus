import base64
import json
import requests
from key import key

sign_server_host = "https://sign-tt-xiheqqvsqx.us-west-1.fcapp.run"


def do_sign(platform: str,
               app_ver: str,
               sdk_ver: str,
               device_id: str,
               timestamp: int,
               device_model: str,
               os_version: str,
               req_type: str,
               req_url: str,
               body: bytes = None,
               android_id: str = "",
               open_udid: str = "",
               ios_idfa: str = ""
               ):
    """
    :param platform "android" or "ios"
    :param app_ver
    :param sdk_ver
    :param device_id
    :param timestamp
    :param device_model
    :param os_version
    :param req_type "GET" or "POST"
    :param req_url
    :param body  required when req_type = "POST"
    :param android_id required when platform = "android"
    :param open_udid  required when platform = "ios"
    :param ios_idfa  required when platform = "ios"
    :return x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon
    """

    url = f"{sign_server_host}/get_sign"

    # body need base46 encode
    req_body = ""
    if body is not None:
        req_body = base64.b64encode(body).decode()

    headers = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "key": key,  # Contact us for secret key
        "req_type": req_type,
        "req_url": req_url,
        "timestamp": timestamp,
        "req_body": req_body,
        "dev_info": {
            "app_ver": app_ver,
            "sdk_ver": sdk_ver,
            "platform": platform,
            "device_id": device_id,
            "device_model": device_model,
            "os_version": os_version,
            "android_id": android_id,
            "open_udid": open_udid,
            "idfa": ios_idfa
        }
    })
    print(payload)

    response = requests.post(url, headers=headers, data=payload)
    print(response.status_code)
    print(response.text)
    if response.status_code == 200:
        obj = json.loads(response.text)
        data = obj["data"]
        return data["x_l"], data["x_a"], data["x_g"], data["x_k"], data["x_t"]
