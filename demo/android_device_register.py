from uuid import uuid1
from api import *
from utils import *


class DeviceRegister:
    def __init__(self):
        self.device_id = ""
        self.install_id = ""
        self.dev_info = None

    def _get_trace_id(self):
        return get_trace_id(self.dev_info["appId"], self.dev_info["deviceId"])

    def post_device_register(self):
        """
        send device_register request
        """
        timestamp_ms = round(time.time() * 1000)
        timestamp = timestamp_ms // 1000

        host = 'http://log-va.tiktokv.com'
        url = "/service/2/device_register/"
        query_args = {
            "ac": "wifi",
            "aid": self.dev_info["appId"],
            "app_name": self.dev_info["appName"],
            "version_code": self.dev_info["appVersionCode"],
            "version_name": self.dev_info["appVersion"],
            "device_platform": "android",
            "ab_version": self.dev_info["appVersion"],
            "ssmix": "a",
            "device_type": self.dev_info["deviceModel"],
            "device_brand": self.dev_info["deviceBrand"],
            "language": self.dev_info["language"],
            "os_api": str(self.dev_info["apiLevel"]),
            "os_version": self.dev_info["osVersion"],
            "openudid": self.dev_info["openUdid"],
            "manifest_version_code": str(self.dev_info["manifestVersionCode"]),
            "resolution": f'{self.dev_info["screenWidth"]}*{self.dev_info["screenHeight"]}',
            "dpi": self.dev_info["densityDpi"],
            "update_version_code": str(self.dev_info["updateVersionCode"]),
            "_rticket": timestamp_ms,
            "app_type": "normal",
            "sys_region": self.dev_info["region"],
            "timezone_name": self.dev_info["timezoneName"],
            "app_language": self.dev_info["language"],
            "carrier_region": self.dev_info["carrierRegion"],
            "fake_region": self.dev_info["region"],
            "timezone_offset": self.dev_info["timezoneOffset"],
            "host_abi": self.dev_info["cpuAbi"],
            "locale": self.dev_info["language"],
            "ac2": "wifi5g",
            "uoo": "1",
            "op_region": self.dev_info["region"],
            "build_number": self.dev_info["appVersion"],
            "region": self.dev_info["region"],
            "ts": timestamp,
            "cdid": self.dev_info["cdid"],
        }

        query_args_str = to_query_str(query_args)
        req_url = f"{host}{url}?{query_args_str}"

        body = get_device_register_body(self.dev_info)
        body_md5 = hash_md5_hex(body).upper()
        x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon = do_sign_v5("POST", timestamp=timestamp, req_url=req_url,
                                                                    body=body, dev_info=self.dev_info)
        headers = {
            'sdk-version': '2',
            'passport-sdk-version': '19',
            "x-ss-req-ticket": str(timestamp_ms),
            "x-vc-bdturing-sdk-version": "2.2.1.i18n",
            "x-tt-dm-status": "login=0;ct=0;rt=7",
            'content-type': 'application/octet-stream;tt-data=a',
            'x-ss-stub': body_md5,
            "x-tt-local-region": self.dev_info["region"],
            "x-tt-store-region-uid": "none",
            "x-tt-store-region-did": "none",
            "x-ss-dp": self.dev_info["appId"],
            'x-tt-trace-id': self._get_trace_id(),
            "x-tt-trace": "1",
            'user-agent': self.dev_info["userAgent"],
            'accept-encoding': 'gzip, deflate',
            "x-argus": x_argus,
            "x-ladon": x_ladon,
            "x_gorgon": x_gorgon,
            "x-khronos": x_khronos,
            "x-tyhon": x_tyhon,
        }

        response = post_request(host, url, query_args_str, headers, body)
        obj = json.loads(response)

        self.device_id = obj["device_id_str"]
        self.install_id = obj["install_id_str"]
        print("device_id_str", self.device_id)
        print("install_id_str", self.install_id)

        return response

    def send_app_alert_check(self):
        """
        send app_alert_check request activation device id
        """
        timestamp_ms = round(time.time() * 1000)
        timestamp = timestamp_ms // 1000

        host = 'http://log-va.tiktokv.com'
        url = "/service/2/app_alert_check/"
        query_args = {
            "timezone": self.dev_info["timezone"],
            "device_id": self.device_id,
            "ac": "wifi",
            "aid": self.dev_info["appId"],
            "app_name": self.dev_info["appName"],
            "version_code": self.dev_info["appVersionCode"],
            "version_name": self.dev_info["appVersion"],
            "device_platform": "android",
            "ab_version": self.dev_info["appVersion"],
            "ssmix": "a",
            "device_type": self.dev_info["deviceModel"],
            "device_brand": self.dev_info["deviceBrand"],
            "language": self.dev_info["language"],
            "os_api": str(self.dev_info["apiLevel"]),
            "os_version": self.dev_info["osVersion"],
            "openudid": self.dev_info["openUdid"],
            "manifest_version_code": str(self.dev_info["manifestVersionCode"]),
            "resolution": f'{self.dev_info["screenWidth"]}*{self.dev_info["screenHeight"]}',
            "dpi": self.dev_info["densityDpi"],
            "update_version_code": str(self.dev_info["updateVersionCode"]),
            "_rticket": timestamp_ms,
            "app_type": "normal",
            "sys_region": self.dev_info["language"],
            "timezone_name": self.dev_info["timezoneName"],
            "app_language": self.dev_info["language"],
            "carrier_region": self.dev_info["region"],
            "fake_region": self.dev_info["region"],
            "timezone_offset": self.dev_info["timezoneOffset"],
            "host_abi": self.dev_info["cpuAbi"],
            "locale": self.dev_info["language"],
            "ac2": "wifi5g",
            "uoo": "1",
            "op_region": self.dev_info["region"],
            "build_number": self.dev_info["appVersion"],
            "region": self.dev_info["region"],
            "ts": timestamp,
            "cdid": self.dev_info["cdid"],
            "req_id": "120126cf-1934-40d5-a803-315925967fb6",
            "cronet_version": self.dev_info["cronetVersion"],
            "ttnet_version": self.dev_info["ttnetVersion"]
        }
        query_args_str = to_query_str(query_args)
        req_url = f"{host}{url}?{query_args_str}"
        x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon = do_sign_v5("GET", dev_info=self.dev_info, timestamp=timestamp,
                                                                    req_url=req_url)
        headers = {
            'sdk-version': '2',
            'passport-sdk-version': '19',
            "x-ss-req-ticket": str(timestamp_ms),
            "x-vc-bdturing-sdk-version": "2.2.1.i18n",
            "x-tt-dm-status": "login=0;ct=0;rt=7",
            'content-type': 'application/octet-stream;tt-data=a',
            "x-tt-local-region": self.dev_info["region"],
            "x-tt-store-region-uid": "none",
            "x-tt-store-region-did": "none",
            "x-ss-dp": self.dev_info["appId"],
            'x-tt-trace-id': self._get_trace_id(),
            'user-agent': self.dev_info["userAgent"],
            'accept-encoding': 'gzip, deflate',
            "x-argus": x_argus,
            "x-ladon": x_ladon,
            "x_gorgon": x_gorgon,
            "x-khronos": x_khronos,
            "x-tyhon": x_tyhon,
        }

        response = get_request(host, url, query_args_str, headers)
        obj = json.loads(response)

    def get_token(self):
        """
        send get_token get sec_did_token
        """
        timestamp_ms = round(time.time() * 1000)
        timestamp = timestamp_ms // 1000

        host = "https://mssdk-va.tiktokv.com"
        url = "/sdi/get_token"
        query_args = {
            "lc_id": self.dev_info["licenseId"],
            "platform": "android",
            "device_platform": "android",
            "sdk_ver": self.dev_info["MSSDKVersion"],
            "sdk_ver_code": self.dev_info["MSSDKVersionCode"],
            "app_ver": self.dev_info["appVersion"],
            "version_code": self.dev_info["appVersionCode"],
            "aid": self.dev_info["appId"],
            "iid": self.install_id,
            "did": self.device_id,
            "region_type": self.dev_info["regionType"],
            "mode": "2"
        }
        query_args_str = to_query_str(query_args)
        req_url = f"{host}{url}?{query_args_str}"
        body = encrypt_get_token(self.dev_info)
        x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon = do_sign_v5("POST", dev_info=self.dev_info,
                                                                    timestamp=timestamp, req_url=req_url, body=body)

        body_md5 = hash_md5_hex(body).upper()
        header = {
            "x-tt-dm-status": "login=1;ct=1;rt=1",
            "x-vc-bdturing-sdk-version": "2.2.0",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": self.dev_info["userAgent"],
            "x-tt-cmpl-token": "APNAgQQSF-R5wJVIRPsLJx0i-Ew0aZYMqqyP6zfGEA",
            "sdk-version": "2",
            "passport-sdk-version": "19",
            "x-ss-stub": body_md5,
            "x-tt-store-idc": "useast5",
            "x-tt-store-region": self.dev_info["region"],
            "x-tt-store-region-src": "uid",
            "x-bd-kmsv": "0",
            "x-ss-dp": self.dev_info["appId"],
            "x-tt-trace-id": self._get_trace_id(),
            "accept-encoding": "gzip, deflate",
            "x-argus": x_argus,
            "x-ladon": x_ladon,
            "x_gorgon": x_gorgon,
            "x-khronos": x_khronos,
            "x-tyhon": x_tyhon,
        }
        resp = post_request(host, url, query_args_str, header, post_body=body, is_text=False)
        ret = decrypt_get_token("android", self.dev_info["appId"], resp)
        return ret["token"]

    def post_ri_report(self):
        """
        send get_token get sec_did_token
        """
        timestamp_ms = round(time.time() * 1000)
        timestamp = timestamp_ms // 1000

        host = "https://mssdk-va.tiktokv.com"
        url = "/ri/report"

        query_args = {
            "lc_id": self.dev_info["licenseId"],
            "platform": self.dev_info["os"],
            "device_platform": self.dev_info["platform"],
            "sdk_ver": self.dev_info["MSSDKVersion"],
            "sdk_ver_code": self.dev_info["MSSDKVersionCode"],
            "app_ver": self.dev_info["appVersion"],
            "version_code": self.dev_info["appVersionCode"],
            "aid": self.dev_info["appId"],
            "iid": self.dev_info["installId"],
            "did": self.dev_info["deviceId"],
            "region_type": self.dev_info["regionType"],
            "mode": "2"
        }
        query_args_str = to_query_str(query_args)
        req_url = f"{host}{url}?{query_args_str}"

        body = get_ri_report_body(self.dev_info)
        x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon = do_sign_v5("POST",
                                                                    dev_info=self.dev_info,
                                                                    timestamp=timestamp,
                                                                    req_url=req_url,
                                                                    body=body)
        body_md5 = hash_md5_hex(body).upper()
        header = {
            "user-agent": "ByteDance-MSSDK",
            "x-tt-request-tag": "t=1;n=0",
            "x-vc-bdturing-sdk-version": "2.2.1.i18n",
            "content-type": "application/octet-stream",
            "x-tt-dm-status": "login=0;ct=1;rt=6",
            'x-tt-store-region': self.dev_info["region"],
            'x-tt-store-region-src': 'did',
            'x-ss-dp': self.dev_info["appId"],
            'x-tt-trace-id': self._get_trace_id(),
            'accept-encoding': 'gzip, deflate',
            "x-ss-stub": body_md5,
            "x-argus": x_argus,
            "x-ladon": x_ladon,
            "x_gorgon": x_gorgon,
            "x-khronos": x_khronos,
            "x-tyhon": x_tyhon,
        }
        resp = post_request(host, url, query_args_str, header, post_body=body, is_text=False)
        print(resp)

    def process_dev_info(self, platform: str):
        """
        replace your device info
        """
        self.dev_info = do_get_dev_tmpl(platform)

        self.dev_info["openUdid"] = rand_str(40)
        self.dev_info["clientUdid"] = str(uuid1())
        self.dev_info["cdid"] = str(uuid1())
        self.dev_info["androidId"] = rand_str(20)

        # fill other devices info according to yourself.....

        return self.dev_info


if __name__ == '__main__':
    device = DeviceRegister()
    print("====== START GET DEV TEMPLATE ======")
    device.process_dev_info("android")
    print("====== FINISH GET DEV TEMPLATE ======")

    print("\n====== START DO DEV REGISTER ======")
    device.post_device_register()
    print("====== FINISH DO DEV REGISTER ======")

    print("\n====== START DO DEV ACTIVATE ======")
    device.send_app_alert_check()
    print("====== FINISH DO DEV ACTIVATE ======")

    print("\n====== START GET SEC DEV ID ======")
    dev_info = device.dev_info
    dev_info["installId"] = device.install_id
    dev_info["deviceId"] = device.device_id
    token = device.get_token()
    print("====== FINISH GET SEC DEV ID ======")

    print("\n====== START ri/report ======")
    dev_info["secDeviceIdToken"] = token
    device.post_ri_report()
    print("====== FINISH ri/report ======")
