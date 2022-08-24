import json
import time
from sign import do_sign
from tt_encrypt import do_tt_encrypt
from utils import rand_str, hash_md5_hex, post_request, get_request

host = "https://log22-normal-alisg.tiktokv.com"

class AppInfo:
    appVersion = "25.1.1"
    buildNumber = "250101"
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
    userAgent = "TikTok 25.1.1 rv:250101 (iPhone; iOS 14.2; zh_CN) Cronet"

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


device_info = {
    "magic_tag": "ss_app_log",
    "header": {
        "region": DeviceInfo.region,
        "access": DeviceInfo.access,
        "os_version": DeviceInfo.osVersion,
        "device_model": DeviceInfo.model,
        "app_name": AppInfo.appName,
        "vendor_id": DeviceInfo.vendorId,
        "carrier": DeviceInfo.carrier,
        "scene": 0,
        "sdk_version": 265,
        "custom": {
            "app_region": AppInfo.region,
            "earphone_status": "off",
            "web_ua": "Mozilla\\/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit\\/605.1.15 (KHTML, like Gecko) Mobile\\/15E148",
            "is_kids_mode": 0,
            "is_pad": 0,
            "filter_warn": 0,
            "user_period": 0,
            "user_mode": 0,
            "app_language": AppInfo.language,
            "build_number": AppInfo.buildNumber
        },
        "model_display_name": DeviceInfo.model,
        "display_name": AppInfo.displayName,
        "device_token": "",
        "app_region": AppInfo.region,
        "auth_status": 0,
        "channel" : AppInfo.channel,
        "user_agent": AppInfo.userAgent,
        "idfa": DeviceInfo.idfa,
        "os": DeviceInfo.osName,
        "tz_name": DeviceInfo.timezoneName,
        "tz_offset": 28800,
        "app_language": AppInfo.language,
        "carrier_region": "",
        "is_upgrade_user": False,
        "mcc_mnc": "",
        "aid": AppInfo.id,
        "package": AppInfo.packageName,
        "is_jailbroken": False,
        "language": DeviceInfo.language,
        "cdid": DeviceInfo.cdid,
        "app_version": AppInfo.appVersion,
        "resolution": "1242*2208",
        "timezone": 8
    }
}


class DeviceRegister:
    def __init__(self):
        self.device_id = ""
        self.install_id = ""

    def _get_trace_id(self):
        timestamp = "%x" % (round(time.time() * 1000) & 0xffffffff)
        random_str = str(timestamp) + "010" + rand_str(17) + "0000"
        trace_id = "00-"
        trace_id += random_str
        trace_id += "-"
        trace_id += random_str[:16]
        trace_id += '-01'
        return trace_id

    def _get_body(self) -> bytes:
        """
        make register body
        """
        body_src = json.dumps(device_info)
        return do_tt_encrypt(body_src)
    
    def _get_url_params(self, dict):
        get_args = ''
        for k,v in dict.items():
            get_args += "&{k}={v}".format(k=k, v=v)
        get_args = get_args[1:]
        return get_args

    def post_device_register(self):
        """
        send registe quest
        """

        url = "/service/2/device_register/"
        url_params = {
            "aid" : AppInfo.id,
            "tt_data" : "a",
            "version_code" : AppInfo.appVersion,
            "language" : AppInfo.language,
            "app_name" : AppInfo.appName,
            "app_version" : AppInfo.appVersion,
            "op_region" : AppInfo.region,
            "carrier_region" : AppInfo.region,
            "account_region" : AppInfo.region,
            "locale" : DeviceInfo.locale,
            "sys_region" : DeviceInfo.region,
            "screen_width" : "1242",
            "uoo" : "1",
            "openudid" : DeviceInfo.openudid,
            "cdid" : DeviceInfo.cdid,
            "os_api" : "18",
            "idfv" : DeviceInfo.idfv,
            "ac" : DeviceInfo.access,
            "os_version" : DeviceInfo.osVersion,
            "app_language" : AppInfo.language,
            "tz_name" : DeviceInfo.timezoneName,
            "device_platform" : DeviceInfo.platform,
            "build_number" : AppInfo.buildNumber,
            "device_type" : DeviceInfo.model,
            "idfa" : DeviceInfo.idfa,
            "cronet_version" : AppInfo.cronetVersion,
            "ttnet_version" : AppInfo.ttnetVersion
        }
        get_args = self._get_url_params(url_params)

        body = self._get_body()
        # get_args = parse.urlencode(get_param_dict)

        query_str = f"{host}{url}?{get_args}"

        body_md5 = hash_md5_hex(body).upper()
        timestamp_ms = round(time.time() * 1000)
        timestamp = timestamp_ms // 1000
        x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon = do_sign("ios",
                                                                    app_ver=AppInfo.appVersion,
                                                                    sdk_ver=AppInfo.sdkVersion,
                                                                    device_id=self.device_id,
                                                                    timestamp=timestamp,
                                                                    device_model=DeviceInfo.model,
                                                                    os_version=DeviceInfo.osVersion,
                                                                    req_type="POST",
                                                                    req_url=query_str,
                                                                    body=body,
                                                                    open_udid=DeviceInfo.openudid,
                                                                    ios_idfa=DeviceInfo.idfa
                                                                    )
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

        response = post_request(host, url, get_args, headers, body)
        obj = json.loads(response)
        self.device_id = obj["device_id_str"]
        self.install_id = obj["install_id_str"]

        print("device_id_str", obj["device_id_str"])
        print("install_id_str", obj["install_id_str"])
        return response

    def get_app_alert_check(self):
        # host = 'http://log-va.tiktokv.com'
        url = "/service/2/app_alert_check/"
        url_params = {
            "app_name" : AppInfo.appName,
            "channel" : AppInfo.channel,
            "device_platform" : DeviceInfo.platform,
            "idfa" : DeviceInfo.idfa,
            "is_upgrade_user" : "0",
            "version_code" : AppInfo.appVersion,
            "ac" : DeviceInfo.access,
            "timezone" : DeviceInfo.timezone,
            "os_version" : DeviceInfo.osVersion,
            "aid" : AppInfo.id,
            "cronet_version" : AppInfo.cronetVersion,
            "ttnet_version" : AppInfo.ttnetVersion
        }

        get_args = self._get_url_params(url_params)

        query_str = f"{host}{url}?{get_args}"
        timestamp_ms = round(time.time() * 1000)
        timestamp = timestamp_ms // 1000
        x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon = do_sign("ios",
                                                                    app_ver=AppInfo.appVersion,
                                                                    sdk_ver=AppInfo.sdkVersion,
                                                                    device_id=self.device_id,
                                                                    timestamp=timestamp,
                                                                    device_model=DeviceInfo.model,
                                                                    os_version=DeviceInfo.osVersion,
                                                                    req_type="POST",
                                                                    req_url=query_str,
                                                                    open_udid=DeviceInfo.openudid,
                                                                    ios_idfa=DeviceInfo.idfa
                                                                    )
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
            'accept-encoding': 'gzip, deflate, br',
            'x-khronos': x_khronos,
            'x-gorgon': x_gorgon,
            'x-tyhon': x_tyhon,
            "x-argus": x_argus,
            "x-ladon": x_ladon
        }

        response = get_request(host, url, get_args, headers)
        obj = json.loads(response)
        print(obj)

if __name__ == '__main__':
    device = DeviceRegister()
    device.post_device_register()
    device.get_app_alert_check()
