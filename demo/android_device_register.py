from api import *
from utils import rand_str, hash_md5_hex, post_request, get_request, to_query_str

# aid = "1180"
# package = "com.ss.android.ugc.trill"

aid = "1233"
package = "com.zhiliaoapp.musically"
tz = "SG"
user_agent = f"{package}/2022506250 (Linux; U; Android 9; zh; AOSP on taimen; Build/PQ1A.190105.004; Cronet/TTNetVersion:4cac2dc1 2022-07-06 QuicVersion:b67bcffb 2022-01-05)"
openudid = "78e8bb3548cccc89"
cdid = "27525802-873c-428a-86f3-476cec4ccc44"
app_ver = "25.6.25"
sdk_ver = "v04.04.00-ov-android"
device_model = "AOSP on taimen"
os_version = "9"


class DeviceRegister:
    def __init__(self):
        self.device_id = ""
        self.install_id = ""
        self.dev_info = None

    @staticmethod
    def _get_trace_id():
        timestamp = "%x" % (round(time.time() * 1000) & 0xffffffff)
        random_str = str(timestamp) + "010" + rand_str(17) + "0000"
        trace_id = f"00-{random_str}-{random_str[:16]}-01"
        return trace_id

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
            "aid": aid,
            "app_name": "musical_ly",
            "version_code": "250625",
            "version_name": app_ver,
            "device_platform": "android",
            "ab_version": app_ver,
            "ssmix": "a",
            "device_type": "AOSP+on+taimen",
            "device_brand": "Android",
            "language": "zh",
            "os_api": "28",
            "os_version": "9",
            "openudid": openudid,
            "manifest_version_code": "2022506250",
            "resolution": "1440*2712",
            "dpi": "560",
            "update_version_code": "2022506250",
            "_rticket": timestamp_ms,
            "app_type": "normal",
            "sys_region": tz,
            "timezone_name": self.dev_info["timezoneName"],
            "app_language": "zh-Hans",
            "carrier_region": tz,
            "fake_region": tz,
            "timezone_offset": "28800",
            "host_abi": "armeabi-v7a",
            "locale": "zh-Hans",
            "ac2": "wifi5g",
            "uoo": "1",
            "op_region": tz,
            "build_number": app_ver,
            "region": tz,
            "ts": timestamp,
            "cdid": cdid
        }

        query_args_str = to_query_str(query_args)
        req_url = f"{host}{url}?{query_args_str}"

        body = get_device_register_body(self.dev_info)
        print(body.hex())

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
            "x-tt-local-region": tz,
            "x-tt-store-region-uid": "none",
            "x-tt-store-region-did": "none",
            "x-ss-dp": aid,
            'x-tt-trace-id': self._get_trace_id(),
            'user-agent': user_agent,
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
            "timezone": "8.0",
            "device_id": self.device_id,
            "ac": "wifi",
            "aid": aid,
            "app_name": "musical_ly",
            "version_code": "250625",
            "version_name": app_ver,
            "device_platform": "android",
            "ab_version": app_ver,
            "ssmix": "a",
            "device_type": "AOSP+on+taimen",
            "device_brand": "Android",
            "language": "zh",
            "os_api": "28",
            "os_version": "9",
            "openudid": openudid,
            "manifest_version_code": "2022506250",
            "resolution": "1440*2712",
            "dpi": "560",
            "update_version_code": "2022506250",
            "_rticket": timestamp_ms,
            "app_type": "normal",
            "sys_region": "CN",
            "timezone_name": self.dev_info["timezoneName"],
            "app_language": "zh-Hans",
            "carrier_region": tz,
            "fake_region": tz,
            "timezone_offset": "28800",
            "host_abi": "armeabi-v7a",
            "locale": "zh-Hans",
            "ac2": "wifi5g",
            "uoo": "1",
            "op_region": tz,
            "build_number": app_ver,
            "region": "CN",
            "ts": timestamp,
            "cdid": cdid,
            "req_id": "120126cf-1934-40d5-a803-315925967fb6",
            "cronet_version": "4cac2dc1_2022-07-06",
            "ttnet_version": "4.1.89.18-tiktok"
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
            "x-tt-local-region": tz,
            "x-tt-store-region-uid": "none",
            "x-tt-store-region-did": "none",
            "x-ss-dp": aid,
            'x-tt-trace-id': self._get_trace_id(),
            'user-agent': user_agent,
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
            "lc_id": "2142840551",
            "platform": "android",
            "device_platform": "android",
            "sdk_ver": sdk_ver,
            "sdk_ver_code": "67371040",
            "app_ver": app_ver,
            "version_code": "2022506250",
            "aid": aid,
            "iid": self.install_id,
            "did": self.device_id,
            "region_type": "ov",
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
            "user-agent": user_agent,
            "x-tt-cmpl-token": "APNAgQQSF-R5wJVIRPsLJx0i-Ew0aZYMqqyP6zfGEA",
            "sdk-version": "2",
            "passport-sdk-version": "19",
            "x-ss-stub": body_md5,
            "x-tt-store-idc": "useast5",
            "x-tt-store-region": tz,
            "x-tt-store-region-src": "uid",
            "x-bd-kmsv": "0",
            "x-ss-dp": aid,
            "x-tt-trace-id": self._get_trace_id(),
            "accept-encoding": "gzip, deflate",
            "x-argus": x_argus,
            "x-ladon": x_ladon,
            "x_gorgon": x_gorgon,
            "x-khronos": x_khronos,
            "x-tyhon": x_tyhon,
        }
        resp = post_request(host, url, query_args_str, header, post_body=body, is_text=False)
        ret = decrypt_get_token("android", aid, resp)
        print(ret)

    def process_dev_info(self, platform: str):
        """
        replace your device info
        """
        self.dev_info = do_get_dev_tmpl(platform)

        self.dev_info["appId"] = aid
        self.dev_info["appVersion"] = app_ver
        self.dev_info["MSSDKVersion"] = sdk_ver

        # fill other devices info according to yourself.....

        return self.dev_info


if __name__ == '__main__':
    device = DeviceRegister()
    print("\n====== START GET DEV TEMPLATE ======")
    device.process_dev_info("android")
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
    device.get_token()
    print("\n====== FINISH GET SEC DEV ID ======")
