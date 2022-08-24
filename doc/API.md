# 获取 Tiktok 签名 / Get Tiktok Signature

## URL

```
https://sign-tt-xiheqqvsqx.us-west-1.fcapp.run/get_sign
```

## Method

<b>POST</b>

## Request

|  Field    | Type   | Desc                                                      |
|  ----     | ----   |-----------------------------------------------------------|
| key      | string | 咨询客服获取密卡 / Contact us for secret key                    |
| req_type  | string | "GET" or "POST"                                           |
| req_url   | string | 需要签名的 url / URL requiring signature                       |
| req_body  | base64 string | 需要签名的 body / Body requiring signature (req_type = "POST") |
| timestamp | int    | 时间戳（秒）/ timestamp (second)                                |
| dev_info  | object | 设备详细信息见下表 / See the following table for details           |

***

|  Field    | Type   | Desc                                                                 |
|  ----     | ----   |----------------------------------------------------------------------|
| app_ver   | string | App Version (为空时使用内置版本号 / Use the built-in version when it is empty) |
| sdk_ver   | string | SDK Version (为空时使用内置版本号 / Use the built-in version when it is empty) |
| platform   | string | "android" or "ios"                                                   |
| device_model  | string | 设备型号 / Device model                                             |
| os_version | string    | 系统版本 / System version                                           |
| device_id  | string | TikTok did                                                           |
| android_id | string | Android Id (platform = "android")                                    |
| open_udid  | string | iOS 设备唯一标识符 / Open Unique Device Identifier (platform = "ios")   |
| ios_idfa  | string | iOS 广告主标识符 / Identifier for advertisers (platform = "ios")   |

***

```json
{
  "key": "xxx",
  "req_type": "POST",
  "req_url": "http://xxxxxx/signature/xxxx?version_code=435&device_platform=android&aid=13",
  "timestamp": 1659080857,
  "req_body": "dGMFEAAA1kRx4+W8N0fcziL8Dyt8Br==",
  "dev_info": {
    "app_ver": "25.6.25",
    "sdk_ver": "v04.04.00-ov-android",
    "platform": "android",
    "device_id": "",
    "device_model": "Pixel 6",
    "os_version": "12.1",
    "android_id": "9234923948d9392934dkk3939935d93939r3a3s3"
  }
}
```

## Response

|  Field    | Type   | Desc |
|  ----     | ----   |----  |
| x_a      | string | X-Argus  |
| x_l      | string | X-Ladon  |
| x_g      | string | X-Gorgon  |
| x_k      | string | X-khronos |
| x_t      | string | x-Tyhon   |
| sdk_ver  | string | SDK Version |
| app_ver  | string | App Version |

***

```json
{
  "code": 200,
  "data": {
    "x_a": "+qFKX5TmBd7jCQ2IB0B/lcAPqxZS9R6/6E4lEGFnBCDt+hhDQ7qC1vgTyYV9xnpipIR9LvMWCSYAZYxRyPkUKF+MnF7jqBBBA9HVyelJGQfjL4CzQ2rzECWKCxs2/wCPb5ea1S133jhTGAyZ77oNJPRVNf4kxbvIASCvtHZIAyedsD8TPnl3FkRcTVBgNIcUCwTwwy3MdZs5wtPD1TVrXX0WHGLZ6m4oHAQ/sgubCiQSfQHSnOnxsn/8aqIPda2Tvlg=",
    "x_l": "EuARcQ9Wpr55kJ9zpRVS5J49Z+Bca1gGyA44PUxVcrI6e3uT",
    "x_k": "1661312953",
    "x_g": "84044abc000026b100bfba97715b0634ff3d3b0c1c2fdac718a7",
    "x_t": "XN+Ntjl1w+R9b422dnTf8mw6jfl3aMnjOTqNL10=",
    "app_ver": "25.6.25",
    "sdk_ver": "v04.04.00-ov-android"
  },
  "msg": "success"
}
```

# Tiktok 加密 / ttEncrypt

## URL

```
https://sign-tt-xiheqqvsqx.us-west-1.fcapp.run/tt_encrypt
```

## Method

<b>POST</b>

## Request

| Field | Type          | Desc                                   |
|-------|---------------|----------------------------------------|
| key   | string        | 咨询客服人员获取密卡 / Contact us for secret key |
| data  | base64 string | 需要加密的 data / Data requiring encrypt    |

***

```json
{
  "card": "eHSeiNs+3oA28FOQpLxYG5MgrL+crcRPN9V705Y15YzmDLY0DMwe3w==",
  "data": "eyJtYWdpY190YWciOiAic3NfYXBwX2xvZyIsICJoZWFkZXIiOiB7ImRpc3BsYXlfbmFtZSI6ICJUaWtUb2siLCAidXBkYXRlX3ZlcnNpb25fY29kZSI6IDIwMjI1MDYyNTAsICJtYW5pZmVzdF92ZXJzaW9uX2NvZGUiOiAyMDIyNTA2MjUwLCAiYXBwX3ZlcnNpb25fbWlub3IiOiAiIiwgImFpZCI6IDEyMzMsICJwYWNrYWdlIjogImNvbS56aGlsaWFvYXBwLm11c2ljYWxseSIsICJhcHBfdmVyc2lvbiI6ICIyNS42LjI1IiwgInZlcnNpb25fY29kZSI6IDI1MDYyNSwgInNka192ZXJzaW9uIjogIjIuMTIuMS1yYy4zOCIsICJzZGtfdGFyZ2V0X3ZlcnNpb24iOiAyOSwgImdpdF9oYXNoIjogImQ4MWVlYjI2IiwgIm9zIjogIkFuZHJvaWQiLCAib3NfdmVyc2lvbiI6ICI5IiwgIm9zX2FwaSI6IDI4LCAiZGV2aWNlX21vZGVsIjogIkFPU1Agb24gdGFpbWVuIiwgImRldmljZV9icmFuZCI6ICJBbmRyb2lkIiwgImRldmljZV9tYW51ZmFjdHVyZXIiOiAiR29vZ2xlIiwgImNwdV9hYmkiOiAiYXJtZWFiaS12N2EiLCAicmVsZWFzZV9idWlsZCI6ICI5ZTFhMWY1XzIwMjIwODAyX2RmOTkxZWE2LTEyNjYtMTFlZC05M2YxLTAyNDIwMGFjMTEzMSIsICJkZW5zaXR5X2RwaSI6IDU2MCwgImRpc3BsYXlfZGVuc2l0eSI6ICJtZHBpIiwgInJlc29sdXRpb24iOiAiMjcxMngxNDQwIiwgImxhbmd1YWdlIjogInpoIiwgInRpbWV6b25lIjogOCwgImFjY2VzcyI6ICJ3aWZpIiwgIm5vdF9yZXF1ZXN0X3NlbmRlciI6IDAsICJyb20iOiAiZW5nLnRlc3QuMjAyMTEwMTEuMTYyNjA0IiwgInJvbV92ZXJzaW9uIjogImFvc3BfdGFpbWVuLXVzZXJkZWJ1ZyA5IFBRMUEuMTkwMTA1LjAwNCBlbmcudGVzdC4yMDIxMTAxMS4xNjI2MDQgdGVzdC1rZXlzIiwgImNkaWQiOiAiMjc1MjU4MDItODIzZC00MThhLTg2ZjMtNDc2Y2VjNDJhMDQ0IiwgInNpZ19oYXNoIjogIjE5NDMyNmU4MmM4NWMwMjMxMTZmNGE2MzlhNTJlMTJhIiwgIm9wZW51ZGlkIjogIjc4ZThjYTM1NDg5ZWRjODkiLCAiY2xpZW50dWRpZCI6ICIxYmY3Zjg2ZC02NGFiLTQxMmMtYTZkOC0yNTg0OTlkNjdkYTgiLCAicmVnaW9uIjogIlNHIiwgInR6X25hbWUiOiAiQXNpYVxcL1NpbmdhcG9yZSIsICJ0el9vZmZzZXQiOiAyODgwMCwgInJlcV9pZCI6ICIxNjUyZTkzYS1hY2RiLTRiM2YtYWZhZS0yM2UyZWIxMjBhZjIiLCAiY3VzdG9tIjogeyJzY3JlZW5faGVpZ2h0X2RwIjogODIzLCAic2NyZWVuX3dpZHRoX2RwIjogNDExfSwgImFwa19maXJzdF9pbnN0YWxsX3RpbWUiOiAxNjU5NDk2NjcxMTIwLCAiaXNfc3lzdGVtX2FwcCI6IDAsICJzZGtfZmxhdm9yIjogImdsb2JhbCJ9LCAiX2dlbl90aW1lIjogMTY2MTMyMjUyNTE5N30="
}
```

***

## Response

| Field | Type          | Desc          |
|-------|---------------|---------------|
| code  | int           | Result code   |
| data  | base64 string | Encrypt data  |
| msg   | string        | Error message |

***

```json
{
  "code": 200,
  "data": "dGMFEAAALNW4NjX5BgUHpFCSkzJaI10FGgfK0Vp9cC95RbNEUPpkZIHZqTCvCobfA0irGQrZe+bdHNhBHqszsk+peQReMInABAt0spHGjJTmAvMUxBM96GSFDKR5T572zraCRxzCxPPge6fhcfC64cN78PUKIlqcwP4Lp3v2BRCS4J7apaI=",
  "msg": "success"
}
```

***
