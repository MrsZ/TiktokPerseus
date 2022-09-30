import base64
import time
import requests
import json

from key import key

requests.packages.urllib3.disable_warnings()

sign_server_host = "https://new-sign-tt-aycoaohohf.us-west-1.fcapp.run"


def do_get_dev_tmpl(platform: str):
    url = f"{sign_server_host}/get_device_template"
    payload = json.dumps({
        "key": key,
        "platform": platform
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    time.sleep(1)
    return json.loads(response.text)["data"]


def get_device_register_body(dev_info) -> bytes:
    url = f"{sign_server_host}/get_device_register_body"
    payload = json.dumps({
        "key": key,
        "dev_info": dev_info
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    time.sleep(1)
    data = json.loads(response.text)["data"]
    return base64.b64decode(data)


def get_ri_report_body(dev_info) -> bytes:
    url = f"{sign_server_host}/get_ri_report_body"
    payload = json.dumps({
        "key": key,
        "dev_info": dev_info
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    time.sleep(1)
    data = json.loads(response.text)["data"]
    return base64.b64decode(data)


def do_sign_v5(req_type: str, dev_info, timestamp: int, req_url: str, body: bytes = None):
    """

    :param dev_info
    :param timestamp
    :param req_type "GET" or "POST"
    :param req_url
    :param body  required when req_type = "POST"
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
        "dev_info": dev_info
    })
    print(payload)

    response = requests.post(url, headers=headers, data=payload)
    print(response.text)

    time.sleep(1)

    if response.status_code == 200:
        obj = json.loads(response.text)
        data = obj["data"]
        return data["x_l"], data["x_a"], data["x_g"], data["x_k"], data["x_t"]


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
    print(response.text)

    time.sleep(1)
    if response.status_code == 200:
        obj = json.loads(response.text)
        return base64.b64decode(obj["data"].encode())


def encrypt_get_token(dev_info):
    url = f"{sign_server_host}/encrypt_get_token"
    payload = json.dumps({
        "key": key,
        "dev_info": dev_info
    })
    print(payload)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    time.sleep(1)

    if response.status_code == 200:
        obj = json.loads(response.text)
        data = obj["data"]
        return base64.b64decode(data)


def decrypt_get_token(platform, aid, data):
    url = f"{sign_server_host}/decrypt_get_token"
    payload = json.dumps({
        "key": key,
        "platform": platform,
        "aid": aid,
        "data": base64.b64encode(data).decode()
    })
    headers = {
        'Content-Type': 'application/json'
    }
    print(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    time.sleep(1)

    if response.status_code == 200:
        obj = json.loads(response.text)
        return obj["data"]


def get_xcylons(req_url: str, dev_info, payload: bytes = None):
    url = f"{sign_server_host}/get_xcylons"

    req_payload = ""
    if payload is not None:
        req_payload = base64.b64encode(payload).decode()

    data = json.dumps({
        "key": key,
        "req_url": req_url,
        "payload": req_payload,
        "dev_info": dev_info
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=data)
    print(response.text)
    time.sleep(1)
    if response.status_code == 200:
        obj = json.loads(response.text)
        return obj["data"]["xc"]
