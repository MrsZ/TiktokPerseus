import hashlib
import random
import time
import urllib
import requests


def hash_md5_hex(data):
    md5 = hashlib.md5()
    md5.update(data)
    return md5.hexdigest()


def rand_str(length):
    rand = ''
    random_str = '0123456789abcdef'
    for _ in range(length):
        rand += random.choice(random_str)
    return rand


def post_request(host, url, get_args, header, post_body, cookies=None, is_text=True):
    url = host + url + '?' + get_args
    resp = requests.post(url,
                         headers=header,
                         data=post_body,
                         verify=False,
                         cookies=cookies
                         )
    print(resp.headers)

    if is_text is True:
        print("resp:", resp.text)
        return resp.text
    else:
        return resp.content


def get_request(host, url, get_args, header, cookies=None):
    url = host + url + '?' + get_args
    resp = requests.get(url,
                        headers=header,
                        verify=False,
                        cookies=cookies
                        )
    print(resp.headers)
    print("resp:", resp.text)
    return resp.text


def to_query_str(query_dict: dict):
    return urllib.parse.urlencode(query_dict)


def get_trace_id(aid: str, device_id: str):
    timestamp = "%x" % (round(time.time() * 1000) & 0xffffffff)

    if device_id == "":
        device_str = rand_str(16)
    else:
        device_str = hex(int(device_id))[2:]

    aid_str = hex(int(aid))[2:]
    random_str = str(timestamp) + "10" + device_str + rand_str(2) + "0" + aid_str
    trace_id = f"00-{random_str}-{random_str[:16]}-01"
    return trace_id


if __name__ == '__main__':
    print(get_trace_id("1233", ""))
