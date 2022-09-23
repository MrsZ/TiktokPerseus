from api import *
from utils import *
from uuid import uuid1

host = "https://log22-normal-alisg.tiktokv.com"


class DeviceRegister:
    def __init__(self):
        self.device_id = ""
        self.install_id = ""
        self.dev_info = None

    def _get_trace_id(self):
        return get_trace_id(self.dev_info["appId"], self.dev_info["deviceId"])

    def post_device_register(self):
        """
        send device register request
        """
        url = "/service/2/device_register/"
        url_params = {
            "aid": self.dev_info["appId"],
            "tt_data": "a",
            "version_code": self.dev_info["appVersion"],
            "language": self.dev_info["language"],
            "app_name": self.dev_info["appName"],
            "app_version": self.dev_info["appVersion"],
            "op_region": self.dev_info["region"],
            "carrier_region": self.dev_info["region"],
            "account_region": self.dev_info["region"],
            "locale": self.dev_info["language"],
            "sys_region": self.dev_info["region"],
            "screen_width": str(self.dev_info["screenWidth"]),
            "uoo": "1",
            "openudid": self.dev_info["openUdid"],
            "cdid": self.dev_info["cdid"],
            "os_api": "18",
            "idfv": self.dev_info["IDFV"],
            "ac": "WIFI",
            "os_version": self.dev_info["osVersion"],
            "app_language": self.dev_info["language"],
            "tz_name": self.dev_info["timezoneName"],
            "device_platform": self.dev_info["platform"],
            "build_number": self.dev_info["appVersionCode"],
            "device_type": self.dev_info["deviceBrand"],
            "idfa": self.dev_info["IDFA"],
            "cronet_version": self.dev_info["cronetVersion"],
            "ttnet_version": self.dev_info["ttnetVersion"],
        }

        query_args_str = to_query_str(url_params)
        req_url = f"{host}{url}?{query_args_str}"

        body = get_device_register_body(self.dev_info)

        body_md5 = hash_md5_hex(body).upper()
        timestamp_ms = round(time.time() * 1000)
        timestamp = timestamp_ms // 1000
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
            'user-agent': self.dev_info["userAgent"],
            'accept-encoding': 'gzip, deflate',
            'x-khronos': x_khronos,
            'x-gorgon': x_gorgon,
            'x-tyhon': x_tyhon,
            "x-argus": x_argus,
            "x-ladon": x_ladon
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

        """
        url = "/service/2/app_alert_check/"
        url_params = {
            "app_name": self.dev_info["appName"],
            "channel": self.dev_info["channel"],
            "device_platform": self.dev_info["platform"],
            "idfa": self.dev_info["IDFA"],
            "is_upgrade_user": "0",
            "version_code": self.dev_info["appVersion"],
            "ac": "WIFI",
            "timezone": self.dev_info["timezone"],
            "os_version": self.dev_info["osVersion"],
            "aid": self.dev_info["appId"],
            "cronet_version": self.dev_info["cronetVersion"],
            "ttnet_version": self.dev_info["ttnetVersion"],
        }

        query_args_str = to_query_str(url_params)
        req_url = f"{host}{url}?{query_args_str}"

        timestamp_ms = round(time.time() * 1000)
        timestamp = timestamp_ms // 1000

        x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon = do_sign_v5("GET", timestamp=timestamp, req_url=req_url,
                                                                    dev_info=self.dev_info)
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
            'x-khronos': x_khronos,
            'x-gorgon': x_gorgon,
            'x-tyhon': x_tyhon,
            "x-argus": x_argus,
            "x-ladon": x_ladon
        }

        response = get_request(host, url, query_args_str, headers)
        obj = json.loads(response)
        print(obj)

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
            "platform": self.dev_info["os"],
            "device_platform": self.dev_info["platform"],
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
        body = encrypt_get_token(dev_info)
        x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon = do_sign_v5("POST",
                                                                    dev_info=self.dev_info,
                                                                    timestamp=timestamp,
                                                                    req_url=req_url,
                                                                    body=body)
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
        ret = decrypt_get_token("ios", self.dev_info["appId"], resp)
        print(ret)
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
            'sdk-version': '2',
            'x-vc-bdturing-sdk-version': '2.2.0',
            'passport-sdk-version': '5.12.1',
            'x-tt-store-idc': 'useast5',
            'x-tt-store-region': self.dev_info["region"],
            'x-tt-store-region-src': 'uid',
            'x-bd-kmsv': '0',
            'x-ss-dp': self.dev_info["appId"],
            'x-tt-trace-id': self._get_trace_id(),
            'accept-encoding': 'gzip, deflate',
            "x-tt-dm-status": "login=0;ct=1;rt=6",
            "content-type": "application/octet-stream",
            "user-agent": "ByteDance-MSSDK",
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

        self.dev_info["appId"] = "1233"
        self.dev_info["appVersion"] = "25.9.0"
        self.dev_info["MSSDKVersion"] = "v04.04.00-ov-iOS"

        # replace other device info
        self.dev_info["cdid"] = str(uuid1())
        self.dev_info["IDFV"] = str(uuid1()).upper()
        self.dev_info["IDFA"] = str(uuid1()).upper()
        self.dev_info["openUdid"] = "3986af5d531b6be92715d60532e1c2bdd7468091"
        self.dev_info["vendorId"] = str(uuid1()).upper()

        # fill other devices info according to yourself.....

        return self.dev_info


if __name__ == '__main__':
    device = DeviceRegister()
    print("\n====== START GET DEV TEMPLATE ======")
    device.process_dev_info("ios")
    print("\n====== FINISH GET DEV TEMPLATE ======")

    print("\n====== START DO DEV REGISTER ======")
    device.post_device_register()
    print("\n====== FINISH DO DEV REGISTER ======")

    print("\n====== START DO DEV ACTIVATE ======")
    device.send_app_alert_check()
    print("\n====== FINISH DO DEV ACTIVATE ======")

    print("\n====== START GET SEC DEV ID ======")
    dev_info = device.dev_info
    dev_info["installId"] = device.install_id
    dev_info["deviceId"] = device.device_id
    token = device.get_token()
    print("\n====== FINISH GET SEC DEV ID ======")

    print("\n====== START ri/report ======")
    dev_info["secDeviceIdToken"] = token
    device.post_ri_report()
    print("\n====== FINISH ri/report ======")
