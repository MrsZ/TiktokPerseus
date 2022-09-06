import json
import time

from api import do_tt_encrypt, do_sign_v5, do_get_dev_tmpl, decrypt_get_token, encrypt_get_token, \
    get_device_register_body
from utils import rand_str, hash_md5_hex, post_request, get_request, to_query_str

host = "https://log22-normal-alisg.tiktokv.com"


class AppInfo:
    appVersion = "25.9.0"
    buildNumber = "259000"
    appName = "trill"
    cronetVersion = "dcb1a66f_2022-07-04"
    ttnetVersion = "4.1.94.12"
    packageName = "com.ss.iphone.ugc.Ame"
    id = "1180"
    channel = "App Store"
    sdkVersion = "v04.04.00-ov-iOS"
    displayName = "Tiktok"
    region = "jp"
    language = "jp"
    userAgent = "TikTok 25.9.0 rv:259000 (iPhone; iOS 14.2; zh_CN) Cronet"


class DeviceInfo:
    model = "iPhone10,2"
    platform = "iphone"
    osName = "iOS"
    osVersion = "14.2"
    idfa = "E1F9EC92-82FC-4E65-9415-DEE4D928097F"
    cdid = "DEEBA33C-D1E6-30FF-BA78-8EC2997C1074"
    vendorId = "4594F944-2A2E-4471-A791-3AA8A2E46859"
    openudid = "d3986af2bdd746809d560532e1c531b6be927151"
    idfv = "E8F9EC92-24FC-4E32-9135-DEE3D908397F"
    mac = "00:01:6C:06:A6:29"
    region = "jp"
    language = "zh-Hans-CN"
    timezone = "8"
    timezoneName = "Asia\\/Singapore"
    access = "WIFI"
    carrier = ""
    locale = "zh-Hans"


class DeviceRegister:
    def __init__(self):
        self.device_id = ""
        self.install_id = ""
        self.dev_info = None

    def _get_trace_id(self):
        timestamp = "%x" % (round(time.time() * 1000) & 0xffffffff)
        random_str = str(timestamp) + "010" + rand_str(17) + "0000"
        trace_id = f"00-{random_str}-{random_str[:16]}-01"
        return trace_id

    def post_device_register(self):
        """
        send registe quest
        """
        url = "/service/2/device_register/"
        url_params = {
            "aid": AppInfo.id,
            "tt_data": "a",
            "version_code": AppInfo.appVersion,
            "language": AppInfo.language,
            "app_name": AppInfo.appName,
            "app_version": AppInfo.appVersion,
            "op_region": AppInfo.region,
            "carrier_region": AppInfo.region,
            "account_region": AppInfo.region,
            "locale": DeviceInfo.locale,
            "sys_region": DeviceInfo.region,
            "screen_width": "1242",
            "uoo": "1",
            "openudid": DeviceInfo.openudid,
            "cdid": DeviceInfo.cdid,
            "os_api": "18",
            "idfv": DeviceInfo.idfv,
            "ac": DeviceInfo.access,
            "os_version": DeviceInfo.osVersion,
            "app_language": AppInfo.language,
            "tz_name": DeviceInfo.timezoneName,
            "device_platform": DeviceInfo.platform,
            "build_number": AppInfo.buildNumber,
            "device_type": DeviceInfo.model,
            "idfa": DeviceInfo.idfa,
            "cronet_version": AppInfo.cronetVersion,
            "ttnet_version": AppInfo.ttnetVersion
        }

        query_args_str = to_query_str(url_params)
        req_url = f"{host}{url}?{query_args_str}"

        body = get_device_register_body(self.dev_info)
        print(body.hex())

        body_md5 = hash_md5_hex(body).upper()

        timestamp_ms = round(time.time() * 1000)
        timestamp = timestamp_ms // 1000

        x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon = do_sign_v5("POST", timestamp=timestamp, req_url=req_url,
                                                                    body=body, dev_info=self.dev_info)

        trace_id = self._get_trace_id()

        headers = {
            'sdk-version': '2',
            'passport-sdk-version': '19',
            "x-ss-req-ticket": str(timestamp_ms),
            "x-vc-bdturing-sdk-version": "2.2.1.i18n",
            "x-tt-dm-status": "login=0;ct=0;rt=7",
            'content-type': 'application/octet-stream;tt-data=a',
            'x-ss-stub': body_md5,
            "x-tt-local-region": AppInfo.region,
            "x-tt-store-region-uid": "none",
            "x-tt-store-region-did": "none",
            "x-ss-dp": AppInfo.id,
            'x-tt-trace-id': trace_id,
            'user-agent': AppInfo.userAgent,
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
        # host = 'http://log-va.tiktokv.com'
        url = "/service/2/app_alert_check/"
        url_params = {
            "app_name": AppInfo.appName,
            "channel": AppInfo.channel,
            "device_platform": DeviceInfo.platform,
            "idfa": DeviceInfo.idfa,
            "is_upgrade_user": "0",
            "version_code": AppInfo.appVersion,
            "ac": DeviceInfo.access,
            "timezone": DeviceInfo.timezone,
            "os_version": DeviceInfo.osVersion,
            "aid": AppInfo.id,
            "cronet_version": AppInfo.cronetVersion,
            "ttnet_version": AppInfo.ttnetVersion
        }

        query_args_str = to_query_str(url_params)
        req_url = f"{host}{url}?{query_args_str}"

        timestamp_ms = round(time.time() * 1000)
        timestamp = timestamp_ms // 1000

        x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon = do_sign_v5("GET", timestamp=timestamp, req_url=req_url,
                                                                    dev_info=self.dev_info)

        trace_id = self._get_trace_id()
        timestamp_ms = round(time.time() * 1000)

        headers = {
            'sdk-version': '2',
            'passport-sdk-version': '19',
            "x-ss-req-ticket": str(timestamp_ms),
            "x-vc-bdturing-sdk-version": "2.2.1.i18n",
            "x-tt-dm-status": "login=0;ct=0;rt=7",
            'content-type': 'application/octet-stream;tt-data=a',
            "x-tt-local-region": AppInfo.region,
            "x-tt-store-region-uid": "none",
            "x-tt-store-region-did": "none",
            "x-ss-dp": AppInfo.id,
            'x-tt-trace-id': trace_id,
            'user-agent': AppInfo.userAgent,
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
            "lc_id": "1225625952",
            "platform": DeviceInfo.osName,
            "device_platform": DeviceInfo.osName.lower(),
            "sdk_ver": AppInfo.sdkVersion,
            "sdk_ver_code": "67371040",
            "app_ver": AppInfo.appVersion,
            "version_code": "2022506250",
            "aid": AppInfo.id,
            "iid": self.install_id,
            "did": self.device_id,
            "region_type": "ov",
            "mode": "2"
        }
        query_args_str = to_query_str(query_args)
        req_url = f"{host}{url}?{query_args_str}"
        body = encrypt_get_token(dev_info)
        x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon = do_sign_v5("POST", dev_info=self.dev_info, timestamp=timestamp,
                                                                    req_url=req_url, body=body)

        body_md5 = hash_md5_hex(body).upper()
        header = {
            "x-tt-dm-status": "login=1;ct=1;rt=1",
            "x-vc-bdturing-sdk-version": "2.2.0",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": AppInfo.userAgent,
            "x-tt-cmpl-token": "APNAgQQSF-R5wJVIRPsLJx0i-Ew0aZYMqqyP6zfGEA",
            "sdk-version": "2",
            "passport-sdk-version": "19",
            "x-ss-stub": body_md5,
            "x-tt-store-idc": "useast5",
            "x-tt-store-region": AppInfo.region,
            "x-tt-store-region-src": "uid",
            "x-bd-kmsv": "0",
            "x-ss-dp": AppInfo.id,
            "x-tt-trace-id": self._get_trace_id(),
            "accept-encoding": "gzip, deflate",
            "x-argus": x_argus,
            "x-ladon": x_ladon,
            "x_gorgon": x_gorgon,
            "x-khronos": x_khronos,
            "x-tyhon": x_tyhon,
        }
        resp = post_request(host, url, query_args_str, header, post_body=body, is_text=False)
        ret = decrypt_get_token("ios", AppInfo.id, resp)
        print(ret)

    def process_dev_info(self, platform: str):
        """
        replace your device info
        """
        self.dev_info = do_get_dev_tmpl(platform)

        self.dev_info["appId"] = AppInfo.id
        self.dev_info["appVersion"] = AppInfo.appVersion
        self.dev_info["MSSDKVersion"] = AppInfo.sdkVersion

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
    device.get_token()
    print("\n====== FINISH GET SEC DEV ID ======")