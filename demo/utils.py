import hashlib
import random
from urllib import parse

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
    get_args = ''
    for k, v in query_dict.items():
        get_args += f"&{k}={v}"
    get_args = get_args[1:]
    return get_args


if __name__ == '__main__':
    pass

