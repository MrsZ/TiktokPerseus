# 已支持的 API 列表 / Supported API List

| API                                                   | Platform                                                                                              | Desc                                                                              |
|-------------------------------------------------------|:------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| [get_device_template](#get_device_template)           | <input type="checkbox" disabled checked /> iOS<br><input type="checkbox" disabled checked /> Android  | 获取设备信息模版 / Get Device Info Template                                               |
| [get_sign](#get_sign)                                 | <input type="checkbox" disabled checked /> iOS <br> <input type="checkbox" disabled checked />Android | 获取 Tiktok 签名 / Get Tiktok Signature (X-Argus/X-Ladon/X-Gorgon/X-khronos/X-Tyhon)  |
| [get_device_register_body](#get_device_register_body) | <input type="checkbox" disabled checked /> iOS <br> <input type="checkbox" disabled checked />Android | 获取设备注册 Body(内含 tt_encrypt) / Get Device Register Body(Including tt_encrypt inner) |
| [encrypt_get_token](#encrypt_get_token)               | <input type="checkbox" disabled checked /> iOS <br> <input type="checkbox" disabled checked />Android | 获取 sdi/get_token 接口请求加密后的 body / Get Encrpyted Body Used by sdi/get_token         |
| [decrypt_get_token](#decrypt_get_token)               | <input type="checkbox" disabled checked /> iOS <br> <input type="checkbox" disabled checked />Android | 解密 sdi/get_token 接口返回的内容 / Decrypt The Response of sdi/get_token                  |
| [get_ri_report_body](#get_ri_report_body)             | <input type="checkbox" disabled checked /> iOS  | 获取 ri/report post 接口的 Body / Get body of ri/report post request                                        |
| [get_web_sign](#get_web_sign)                         | <input type="checkbox" disabled checked /> Web                                                        | Web 端签名(_siangture & x-bogus) / Web Signature (_signature & x-bogus)              |
| X-Cylons                                              | <input type="checkbox" disabled />iOS<br> <input type="checkbox" disabled />Android                   | Coming soon.                                                                      |                                                                           |

# <a id="get_device_template">获取设备信息模版 / Get Device Info Template </a>

## URL

```
https://new-sign-tt-aycoaohohf.us-west-1.fcapp.run/get_device_template
```

## Method

<b>POST</b>

## Request

| Field    | Type    | Desc                                   |
|----------|---------|----------------------------------------|
| key      | string  | 咨询技术人员获取密卡 / Contact us for secret key |
| platform | string  | platform = "android" or "ios"          |

***

Android:

```json
{
  "key": "...",
  "platform": "android"
}
```

iOS:

```json
{
  "key": "...",
  "platform": "ios"
}
```

## Response

| Field | Type   | Desc          |
|-------|--------|---------------|
| code  | int    | Result code   |
| data  | object | dev_info      |
| msg   | string | Error message |

***

Android:

```json
{
  "code": 200,
  "data": {
    "IMEI": "b6eR12aEefay",
    "MSSDKVersion": "v04.04.00-ov-android",
    "MSSDKVersionCode": "67371040",
    "androidId": "GMvBNG3bm9Zx6azm3jZI0Q",
    "apiLevel": 28,
    "appId": "1233",
    "appVersion": "25.6.25",
    "appVersionCode": "2022506250",
    "bootTimeUTC": "1660725090",
    "brightness": 117,
    "cdid": "27525802-873c-428a-86f3-476cec4ccc44",
    "clientUdid": "1bfcc86d-64ab-412c-a6d8-258499d67bb8",
    "cpuAbi": "armeabi-v7a",
    "cronetVersion": "4cac2dc1_2022-07-06",
    "curBattery": 14,
    "dataModify": "1648621054",
    "densityDpi": 560,
    "deviceBrand": "Android",
    "deviceId": "",
    "deviceManufacturer": "Google",
    "deviceModel": "SAMSUNG",
    "dnsList": "[\"0.0.0.0\"]",
    "drmId": "FaEefb6eREHATUr+GMvBNG3bm9ZX6azm3jZI0Q=",
    "gitHash": "d81eeb26",
    "installId": "",
    "installTime": 1659496671130,
    "internalFreeSize": "52408725137",
    "internalStorageSize": "55886317271",
    "ipv6": "fe80::6047:5ebe:3613:4b48",
    "language": "en_US",
    "licenseId": "2142840551",
    "mac": "66:14:09:3e:bc:8b",
    "manifestVersionCode": 2022506250,
    "openUdid": "78e8bb3548cccc89",
    "os": "Android",
    "osVersion": "9",
    "package": "com.zhiliaoapp.musically",
    "packagePath": "/data/app/com.zhiliaoapp.musically-ILpHWVFOHFc1A==/base.apk",
    "platform": "android",
    "publicIP": "110.86.124.1",
    "ramTotalSize": "3475283943",
    "region": "SG",
    "regionType": "ov",
    "releaseBuild": "9e1a1f5_20220802_df991ea6-1266-11ed-93f1-024200ac1131",
    "rom": "eng.test.20220111.172604",
    "romCompileUTC": "1633940780",
    "romVersion": "SAMSUNG-userdebug eng.test.20220111.172604 20221011",
    "screenHeight": 2880,
    "screenHeightDpi": 823,
    "screenWidth": 1440,
    "screenWidthDpi": 411,
    "sdcardSize": "55788637211",
    "sdkTargetVersion": 29,
    "sigHash": "194326e82c85c023116f4a639a52effa",
    "storageChange": "1660725095",
    "timezone": "8",
    "timezoneName": "Asia/Singapore",
    "timezoneOffset": 28800,
    "ttnetVersion": "4.1.89.18-tiktok",
    "updateVersionCode": 2022506250,
    "wifiGateWayIP": "110.86.124.1",
    "wifiIP": "2038191626"
  },
  "msg": "success"
}
```

iOS:

```json
{
  "code": 200,
  "data": {
        "IDFA": "E1F9EC92-82FC-4E65-9415-DEE4D928097F",
        "IDFV": "4504F914-4A2E-4478-A790-2AA8A1E46859",
        "MSSDKVersion": "v04.04.00-ov-iOS",
        "MSSDKVersionCode": "67371041",
        "appId": "1233",
        "appName": "musical_ly",
        "appVersion": "25.9.0",
        "appVersionCode": "259000",
        "arch": "arm64 v8",
        "bootId": "2B772275-02ED-4471-AE36-544AE162281C",
        "bootTimeUTC": "1661486486",
        "brightness": 43,
        "buildNumber": "259000",
        "carrier": "",
        "carrierRegion": "PL",
        "cdid": "27525802-873c-428a-86f3-476cec4ccc44",
        "channel": "App Store",
        "cpuCoreNum": 6,
        "cronetVersion": "dcb1a66f_2022-07-04",
        "curBattery": 15,
        "densityDpi": 3,
        "deviceBrand": "iPhone10,2",
        "deviceId": "",
        "deviceModel": "D21AP",
        "dylbHash": "a389a4d993fdb2401a51635d73c7cb61",
        "dyldShareCache": "ZHlsZF92MSAgIGFybTY0",
        "dyldUuid": "F756A8D5-5A80-3B4D-9962-36FE0E7638C2",
        "gitHash": "d81eeb26",
        "infoProductVersion": "18B92",
        "installId": "",
        "installTime": "1663400748",
        "internalFreeSize": "45328261120",
        "internalStorageSize": "63968497664",
        "internalStorageUsedSize": "24068493312",
        "ipv6": "fe80::6047:5ebe:3613:4b48",
        "l1DCacheSize": "32768",
        "l2CacheSize": "8388608",
        "language": "en_US",
        "launchFirstTime": "1657622322664",
        "licenseId": "466012054",
        "mac": "66:14:09:3e:bc:8b",
        "openUdid": "d3986af2bdd746809d560532e1c531b6be927151",
        "os": "iOS",
        "osVersion": "14.2",
        "package": "com.zhiliaoapp.musically",
        "platform": "ios",
        "ramTotalSize": "3118235648",
        "region": "SG",
        "regionType": "ov",
        "romCompileUTC": "1633940780",
        "screenHeight": 2880,
        "screenWidth": 1440,
        "secDeviceIdToken": "",
        "sigHash": "194326e82c85c023116f4a639a52effa",
        "teamID": "MJ797D8U6F",
        "textHash": "4503600356763869",
        "timezone": "8",
        "timezoneName": "Asia/Singapore",
        "timezoneOffset": 28800,
        "ttnetVersion": "4.1.94.12",
        "userAgent": "TikTok 25.9.0 rv:259000 (iPhone; iOS 14.2; zh_CN) Cronet",
        "vendorId": "4594F944-2A2E-4471-A791-3AA8A2E46859",
        "webUA": "Mozilla\/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit\/605.1.15 (KHTML, like Gecko) Mobile\/15E148",
        "wifiGateWayIP": "10.85.115.255",
        "wifiIP": "10.85.115.234"
  },
  "msg": "success"
}

```

# <a id="get_sign">获取 Tiktok 签名 / Get Tiktok Signature</a>

## URL

```
https://new-sign-tt-aycoaohohf.us-west-1.fcapp.run/get_sign
```

## Method

<b>POST</b>

## Request

|  Field    | Type   | Desc                                                      |
|  ----     | ----   |-----------------------------------------------------------|
| key      | string | 咨询技术人员获取密卡 / Contact us for secret key                    |
| req_type  | string | "GET" or "POST"                                           |
| req_url   | string | 需要签名的 url / URL requiring signature                       |
| req_body  | base64 string | 需要签名的 body / Body requiring signature (req_type = "POST") |
| timestamp | int    | 时间戳（秒）/ timestamp (second)                                |
| dev_info  | object | 获取设备信息模版接口获取 / get_device_template api get             |

***

```json
{
  "key": "...",
  "req_type": "POST",
  "req_url": "http://xxxxxx/signature/xxxx?version_code=435&device_platform=android&aid=13",
  "timestamp": 1659080857,
  "req_body": "dGMFEAAA1kRx4+W8N0fcziL8Dyt8Br==",
  "dev_info": {
    ...
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
    "x_a": "+qFKX5TmBd7jCQ2IB0B/lcAPqxZS9R6/6E4lEGFnBCDt+hhDQ7qC1vgTyYV9xnpipIR9LvMWCSAZYxRyPkUKF+MnF7jqBBBA9HVyelJGQfjL4CzQ2rzECWKCxs2/wCPb5ea1S133jhTGAyZ77oNJPRVNf4kxbv...tHZIAyedsD8TPnl3FkRcTVBgNIcUCwTwwy3MdZs5wtPD1TVrXX0WHGLZ6m4oHAQ/sgubCiQSfQHSnOnxsn/8qIPda2Tvlg=",
    "x_l": "EuARcQ9Wpr55kJ9zpRVS5J...Bc1gGyA44PUxVcrI6e3uT",
    "x_k": "1661312953",
    "x_g": "08044abc000026b100bfba9...15b0634ff3d3b0c1c2fdac718a7",
    "x_t": "XN+Ntjl1w+R9b4...w6jfl3aMnjOTqNL10=",
    "app_ver": "25.6.25",
    "sdk_ver": "v04.04.00-ov-android"
  },
  "msg": "success"
}
```

# <a id="get_device_register_body">获取设备注册 Body / Get Device Register Body</a>

## URL

```
https://new-sign-tt-aycoaohohf.us-west-1.fcapp.run/get_device_register_body
```

## Method

<b>POST</b>

## Request

| Field    | Type   | Desc                                       |
|----------|--------|--------------------------------------------|
| key      | string | 咨询技术人员获取密卡 / Contact us for secret key     |
| dev_info  | object | 获取设备信息模版接口获取 / get_device_template api get |

***

```json
{
  "key": "...",
  "dev_info": {
    ...
  }
}

```

## Response

| Field | Type          | Desc          |
|-------|---------------|---------------|
| code  | int           | Result code   |
| data  | base64 string | Encrypt data  |
| msg   | string        | Error message |

```json
{
  "code": 200,
  "data": "dGMFEAAARTi29Oe6mnbuHWfU3SvYLJol0BX5Pl9+c6HF+LWb9S7cvv7hL6QUvXvxZ/5XjQrDn1akDImmpvy5b6xJGep96iBThgrQbGd8sqKdv537ICjfBOTVdC4n9gzSpULsWGuCA+Nit/i0FJexwseb8MHVQsEluC......QB4c7uwXP+4sNu8DtpfAXKH63lKlGtY18HN5WOfG4nnfbR12w2+3nCoMV6RyDo+mTmZUVspzdSPa3A/Ic0AhDc2l+odtdpe11HkIVt74IE1O/DTp7Vsqmm9fjXCBW5mixixBKTr4vU0LyQI6YGpd3LRNzwDPECXS359m2LLeWGCFNId+k6J2VmmEvjbTcDauJWrNb8/pG5yZmjjCdcljo3cRfP9P6PT+CCI5QoK0AxT2z+Gp3ERbvOGcW5upwsRnYgy77vDwnCJPJ2BMCs4eJigZ6Wh0YOf2bKVqkFUuLHsaOAoTY/DqLM33Xp9LMCK85S+Pt06+6/ck1UHEbffF74PMbZYjD9L4U+zqpAl3FZGQiMawuIfz7Cq9BIpAC5KIoxJ7Km/ih7wSFD2egQNRfsqEjE7HEKkVsMB7ogom6snJ+DDy8i6yYSFOlMLQtS8d2Eq7zP8MTm5C1tXcY7u6CHPRKuFobAMX2Y33uR24si/sG9fyJR8tehpft8jKe5G0SHM/UHkfbhbbVXG7WVxSq64uZ+CC2ufPpKaFpkpA2tQRhswMSQlig4bhreA5q4U2xeFPO23nh+MOO2HTsYRpZxrQkXL2mm6yUU1a7q1DdzzNcTTZ3y6cHIqOaiiBI0SlTSl8GQYQ50Njc87ZsF9JbKK1vdyBbeuY474+G8mK6pMiHqRJiIB3Jel0d0352ZupWbqrk5quYZHDTy62YZ/KMId/eAxoG2eedUWNqh5MW5UEf7pkNclBvw+T7dBP+wPUHH/KJYMQETTbj/f4vehTPbOiGFbbcMnsG83LiPeUmQyVpAwRO5gdSdCcXGZnU2PAZifRcy9WPRUkhlXUDg31CMzMaVV/Dcd7OC5M7CdGp24rkoJwOS/5FVssjZC5UqV9wPTqY0o=",
  "msg": "success"
}
```

# ~~Tiktok 加密 / ttEncrypt~~

> 废弃，请使用新的接口 `get_device_register_body`

> Deprecated, please use the new API `get_device_register_body`

## URL

```
https://sign-tt-xiheqqvsqx.us-west-1.fcapp.run/tt_encrypt
```

## Method

<b>POST</b>

## Request

| Field | Type          | Desc                                   |
|-------|---------------|----------------------------------------|
| key   | string        | 咨询技术人员获取密卡 / Contact us for secret key |
| data  | base64 string | 需要加密的 data / Data requiring encrypt    |

***

```json
{
  "key": "...",
  "data": "eyJtYWdpY190YWciOiAic3NfYXBwX2xvZyIsICJoZWFkZXIiOiB7ImRpc3BsYXlfbmFtZSI6ICJUaWtUb2siLCAidXBkYXRlX3ZlcnNpb25fY29kZSI6IDIwMjI1MDYyNTAsICJtYW5pZmVzdF92ZXJzaW9uX2NvZGUiOiAyMDIyNTA2MjUwLCAiYXBwX3ZlcnNpb25fbWlub3IiOiAiIiwgImFpZCI6IDEyMzMsICJwYWNrYWdlIjogImNvbS56aGlsaWFvYXBwLm11c2ljYWxseSIsICJhcHBfdmVyc2lvbiI6ICIyNS42LjI1IiwgInZlcnNpb25fY29kZSI6IDI1MDYyNSwgInNka192ZXJzaW9uIjogIjIuMTIuMS1yYy4zOCIsICJzZGtfdGFyZ2V0X...ImdpdF9oYXNoIjogImQ4MWVlYjI2IiwgIm9zIjogIkFuZHJvaWQiLCAib3NfdmVyc2lvbiI6ICI5IiwgIm9zX2FwaSI6IDI4LCAiZGV2aWNlX21vZGVsIjogIkFPU1Agb24gdGFpbWVuIiwgImRldmljZV9icmFuZCI6ICJBbmRyb2lkIiwgImRldmljZV9tYW51ZmFjdHVyZXIiOiAiR29vZ2xlIiwgImNwdV9hYmkiOiAiYXJtZWFiaS12N2EiLCAicmVsZWFzZV9idWlsZCI6ICI5ZTFhMWY1XzIwMjIwODAyX2RmOTkxZWE2LTEyNjYtMTFlZC05M2YxLTAyNDIwMGFjMTEzMSIsICJkZW5zaXR5X2RwaSI6IDU2MCwgImRpc3BsYXlfZGVuc2l0eSI6ICJtZHBpIiwgInJlc29sdXRpb24iOiAiMjcxMngxNDQwIiwgImxhbmd1YWdlIjogInpoIiwgInRpbWV6b25lIjogOCwgImFjY2VzcyI6ICJ3aWZpIiwgIm5vdF9yZXF1ZXN0X3NlbmRlciI6IDAsICJyb20iOiAiZW5nLnRlc3QuMjAyMTEwMTEuMTYyNjA0IiwgInJvbV92ZXJzaW9uIjogImFvc3BfdGFpbWVuLXVzZXJkZWJ1ZyA5IFBRMUEuMTkwMTA1LjAwNCBlbmcudGVzdC4yMDIxMTAxMS4xNjI2MDQgdGVzdC1rZXlzIiwgImNkaWQiOiAiMjc1MjU4MDItODIzZC00MThhLTg2ZjMtNDc2Y2VjNDJhMDQ0IiwgInNpZ19oYXNoIjogIjE5NDMyNmU4MmM4NWMwMjMxMTZmNGE2MzlhNTJlMTJhIiwgIm9wZW51ZGlkIjogIjc4ZThjYTM1NDg5ZWRjODkiLCAiY2xpZW50dWRpZCI6ICIxYmY3Zjg2ZC02NGFiLTQxMmMtYTZkOC0yNTg0OTlkNjdkYTgiLCAicmVnaW9uIjogIlNHIiwgInR6X25hbWUiOiAiQXNpYVxcL1NpbmdhcG9yZSIsICJ0el9vZmZzZXQiOiAyODgwMCwgInJlcV9pZCI6ICIxNjUyZTkzYS1hY2RiLTRiM2YtYWZhZS0yM2UyZWIxMjBhZjIiLCAiY3VzdG9tIjogeyJzY3JlZW5faGVpZ2h0X2RwIjogODIzLCAic2NyZWVuX3dpZHRoX2RwIjogNDExfSwgImFwa19maXJzdF9pbnN0YWxsX3RpbWUiOiAxNjU5NDk2NjcxMTIwLCAiaXNfc3lzdGVtX2FwcCI6IDAsICJzZGtfZmxhdm9yIjogImdsb2JhbCJ9LCAiX2dlbl90aW1lIjogMTY2MTMyMjUyNTE5N30="
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
  "data": "dGMFEAAALNW4NjX5BgUHpFCSkzJaI10FGgfK0Vp9cC95RbNEUPpkZIHZqTCvCobfA0irGQrZe+bdHNhBHqszsk+peQReMInABAt0spHGjJTmAvMUxBM96GSFDK....xPPge6fhcfC64cN78PUKIlqcwP4Lp3v2BRCS4J7apaI=",
  "msg": "success"
}
```

***

# <a id="encrypt_get_token">获取 get_token 接口请求 body / Get Token Body Encrypt</a>

## URL

```
https://new-sign-tt-aycoaohohf.us-west-1.fcapp.run/encrypt_get_token
```

## Method

<b>POST</b>

## Request

| Field    | Type   | Desc                                        |
|----------|--------|---------------------------------------------|
| key      | string | 咨询技术人员获取密卡 / Contact us for secret key      |
| dev_info | object | 获取设备信息模版接口获取 / get_device_template api get  |

***

```json
{
  "key": "...",
  "dev_info": {
    ...
  }
}
```

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
  "data": "CMSQgIIEEAIYAiKgBN13HyCgtk4+donHlnj63v7SPVYod+aQWngJQd1Xx3koCbcXKiiNHZmi4n1r06d0oGUl7KuxqoXXZVVYGKxB3kZG8uCi0uAn1CpRyejxGL51sBDiC/XCfrJFSSTWJJKuVkh52/uvy8DrSI+FxyzZtAPVu4QpFPlREJJFsblIdJECG9xzP2GSZMUkMooTtqQlsD8902QPSy6syWtpgp5Qv9LtJerjD2Qp7r0Dw6xKWXlEHIPEFtXzjju8vQsrPDzPW/Kvit07t8EgCiC3oB930mpvXiSDhAQgTe4H15a/+Tbi2C9bYgB9cxJSnA9SYGgDx6c3IoFfzWRN......veINGGljqhTsjjhq7OO/4rKIkdla59gQ7eC80xizPLFvJ+vZueBNFKZ0nptJx0v56szkgjo56NFehgbcGtGniXMRPNrCKYy2R7hhGsLprUT5myPTke/KStJ1PeQQG7znHzNTkm2CJvvu7G8goq5eUeebgwF/SZJowTK3tu9wn3froWYK9HG44290txPrHl0gJDECO+C2zvfUoUqav2YEvsjzO/SA/s5YHpNPZYeNlZOxCUuZIYVpjyQSpH8Aw9KIPuTYVAGN0NLz4fc3i05VCqQ5Bd2i+Ja8ZU2H2a1QBWGqFGdSsteN81IEhVWOFBOn6noBv2xylPs8tlBbga+XoGyE9LssjqUd9/4TrRpa15/DeWOhTYcqfn3vwUlUPkowIrT1d9g",
  "msg": "success"
}
```

# <a id="decrypt_get_token">解密 get_token 接口返回内容 / Decrypt Get Token Response</a>

## URL

```
https://new-sign-tt-aycoaohohf.us-west-1.fcapp.run/decrypt_get_token
```

## Method

<b>POST</b>

## Request

| Field    | Type          | Desc                                   |
|----------|---------------|----------------------------------------|
| key      | string        | 咨询技术人员获取密卡 / Contact us for secret key |
| platform | string        | platform = "android" or "ios"          |
| aid      | string        | app id                                 |
| data     | base64 string | 需要加密的 data / Data requiring encrypt    |

***

```json
{
  "key": "...",
  "platform": "android",
  "aid": "1233",
  "data": "CKSMkIEEEAIoAjJAGXtAQy8VFQZN.....ZMRC0xxmhWgfmZAMAddLsdDblTCrcv1329BMBaVVn8XvmG+L8h93IZQ=="
}
```

## Response

| Field | Type    | Desc          |
|-------|---------|---------------|
| code  | int     | Result code   |
| data  | object  | sec did token |
| msg   | string  | Error message |

***

```json
{
  "code": 200,
  "data": {
    "resultCode": 202,
    "token": "Aasc_A-qvr0ca....XEV-JH"
  },
  "msg": "success"
}
```

# <a id="get_ri_report_body">获取 ri/report 接口 Body / Get ri/report Body </a>

## URL

```
https://new-sign-tt-aycoaohohf.us-west-1.fcapp.run/get_ri_report_body
```

## Method

<b>POST</b>

## Request

| Field    | Type       | Desc                                       |
|----------|------------|--------------------------------------------|
| key      | string     | 咨询技术人员获取密卡 / Contact us for secret key     |
| dev_info | object     | 获取设备信息模版接口获取 / get_device_template api get |

***

```json
{
  "key": "...",
  "dev_info": {
    ...
  }
}
```

## Response

| Field | Type          | Desc          |
|-------|---------------|---------------|
| code  | int           | Result Code   |
| data  | base64 string | Encrypt Data  |
| msg   | string        | Error Message |

***

```json
{
  "code": 200,
  "data": "lREJJF2C9bYgB9cxJSnA9SYGgDx6c3IoFfzWRN......veINGGljqhTueBNFKZ0nptJx0vGniXMRPNrCKYy2R7hhGsLprUT5myPTke/KStJ1PeQQG7znHzNTkm2CJvvu7G8goq5eUeebgwF/SZJowTK3tu9wn3froWYK9HG44290txPrHl0gJDECO+C2zvfUoUqav2YEvsjzO/SA/s5YHpNPZYeNlZOxCUuZIYVpjyQSpH8Aw9KIPuTYVAGN0NLz4fc3i05VCqQ5Bd2i+Ja8ZU2H2a1QBWGqFGdSsteN81IEhVWOFBOn6noBv2xylPs8tlBbga+XoGyE9LssjqUd9/4TrRpa15/DeWOhTYcqfn3vwUlUPkowIrT1d9g",
  "msg": "success"
}
```

# <a id="get_web_sign">Web 签名 / Web Signature (_signature & x-bogus)</a>

## URL

```
https://new-sign-tt-aycoaohohf.us-west-1.fcapp.run/get_web_sign
```

## Method

<b>POST</b>

## Request

| Field   | Type          | Required | Desc                                    |
|---------|---------------|----------|-----------------------------------------|
| key     | string        | yes      | 咨询技术人员获取密卡 / Contact us for secret key  |
| req_url | string        | yes      | 需要签名的 url / URL requiring signature     |
| body    | base64 string | no       | 需要签名的 body / body requiring signature   |

GET:

```json
{
  "key": "...",
  "req_url": "https://webcast.tiktok.com/webcast/im/fetch/?aid=1988&app_language=en-US&app_name=tiktok_web&browser_language=en&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0+(Windows+NT+10.0;+Win64;+x64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/102.0.5005.63+Safari/537.36&cookie_enabled=true&cursor=&internal_ext=&device_platform=web&focus_state=true&from_page=user&history_len=4&is_fullscreen=false&is_page_visible=true&did_rule=3&fetch_rule=1&identity=audience&last_rtt=0&live_id=12&resp_content_type=protobuf&screen_height=1152&screen_width=2048&tz_name=Europe/Berlin&referer=https://www.tiktok.com/&root_referer=https://www.tiktok.com/&version_code=180800&webcast_sdk_version=1.3.0&update_version_code=1.3.0&room_id=7142747327864965934"
}
```

POST:

```json
{
  "key": "...",
  "req_url": "https://webcast.tiktok.com/webcast/im/fetch/?aid=1988&app_language=en-US&app_name=tiktok_web&browser_language=en&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0+(Windows+NT+10.0;+Win64;+x64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/102.0.5005.63+Safari/537.36&cookie_enabled=true&cursor=&internal_ext=&device_platform=web&focus_state=true&from_page=user&history_len=4&is_fullscreen=false&is_page_visible=true&did_rule=3&fetch_rule=1&identity=audience&last_rtt=0&live_id=12&resp_content_type=protobuf&screen_height=1152&screen_width=2048&tz_name=Europe/Berlin&referer=https://www.tiktok.com/&root_referer=https://www.tiktok.com/&version_code=180800&webcast_sdk_version=1.3.0&update_version_code=1.3.0&room_id=7142747327864965934"
  "body": "eyJpaWQiOjEyMTMyMzQzNDM0fQ=="
}
```

## Response

| Field | Type    | Desc          |
|-------|---------|---------------|
| code  | int     | Result code   |
| data  | object  | signed result |
| msg   | string  | Error message |

signed result detail:

| Field             | Type   | Desc             |
|-------------------| ----   |------------------|
| _signature        | string | Old signature    |
| x-bogus           | string | X-Bogus          |
| browser_language  | string | Browser language |
| browser_name      | string | Browser name     |
| browser_platform  | string | Browser platform |
| signed_url        | string | Full signed url  |
| user_agent        | string | User Agent       |

```json
{
  "code": 200,
  "data": {
    "_signature": "_02B4Z6wo00001YyF3xxxxIDBjIXcg1Tsg42MhdjAAAAAc6",
    "browser_language": "en",
    "browser_name": "Mozilla",
    "browser_platform": "Win32",
    "browser_version": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
    "signed_url": "https://webcast.tiktok.com/webcast/im/fetch/?aid=1988&app_language=en-US&app_name=tiktok_web&browser_language=en&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0+(Windows+NT+10.0;+Win64;+x64)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/102.0.5005.63+Safari/537.36&cookie_enabled=true&cursor=&internal_ext=&device_platform=web&focus_state=true&from_page=user&history_len=4&is_fullscreen=false&is_page_visible=true&did_rule=3&fetch_rule=1&identity=audience&last_rtt=0&live_id=12&resp_content_type=protobuf&screen_height=1152&screen_width=2048&tz_name=Europe/Berlin&referer=https://www.tiktok.com/&root_referer=https://www.tiktok.com/&version_code=180800&webcast_sdk_version=1.3.0&update_version_code=1.3.0&room_id=7142747327864965934&X-Bogus=DFSzswVO4uxANxxxxsIr3em4pIDt&_signature=_02B4Z6wo00001YyF3IxxxxIDBjIXcg1Tsg42MhdjAAAAAc6",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
    "x-bogus": "DFSzswVOxxxxaSsIr3em4pIDt"
  },
  "msg": "success"
}
```

