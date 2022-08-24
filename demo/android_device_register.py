import json
import time

from sign import do_sign
from tt_encrypt import do_tt_encrypt
from utils import rand_str, hash_md5_hex, post_request, get_request

# aid = 1180
# package = "com.ss.android.ugc.trill"

aid = 1233
package = "com.zhiliaoapp.musically"
tz = "SG"
user_agent = f"{package}/2022506250 (Linux; U; Android 9; zh; AOSP on taimen; Build/PQ1A.190105.004; Cronet/TTNetVersion:4cac2dc1 2022-07-06 QuicVersion:b67bcffb 2022-01-05)"
openudid = "78e8bb3548cccc89"
cdid = "27525802-873c-428a-86f3-476cec4ccc44"
app_ver = "25.6.25"
sdk_ver = "v04.04.00-ov-android"
device_model = "AOSP on taimen"
os_version = "9"

device_info = {
    "magic_tag": "ss_app_log",
    "header": {
        "display_name": "TikTok",
        "update_version_code": 2022506250,
        "manifest_version_code": 2022506250,
        "app_version_minor": "",
        "aid": aid,
        "package": package,
        "app_version": app_ver,
        "version_code": 250625,
        "sdk_version": "2.12.1-rc.38",
        "sdk_target_version": 29,
        "git_hash": "d81eeb26",
        "os": "Android",
        "os_version": os_version,
        "os_api": 28,
        "device_model": device_model,
        "device_brand": "Android",
        "device_manufacturer": "Google",
        "cpu_abi": "armeabi-v7a",
        "release_build": "9e1a1f5_20220802_df991ea6-1266-11ed-93f1-024200ac1131",
        "density_dpi": 560,
        "display_density": "mdpi",
        "resolution": "2712x1440",
        "language": "zh",
        "timezone": 8,
        "access": "wifi",
        "not_request_sender": 0,
        "rom": "eng.test.20211011.162604",
        "rom_version": "aosp_taimen-userdebug 9 PQ1A.199105.002 eng.test.20220211.162604 test-keys",
        "cdid": cdid,
        "sig_hash": "194326e82c85c023116f4a639a52effa",
        "openudid": openudid,
        "clientudid": "1bfcc86d-64ab-412c-a6d8-258499d67bb8",
        "region": tz,
        "tz_name": "Asia\\/Singapore",
        "tz_offset": 28800,
        "req_id": "1652e93a-acdb-4b3f-afae-23e2eb120ac2",
        "custom": {
            "screen_height_dp": 823,
            "screen_width_dp": 411
        },
        "apk_first_install_time": 1659496671130,
        "is_system_app": 0,
        "sdk_flavor": "global"
    },
    "_gen_time": round(time.time() * 1000)
}


class DeviceRegister:
    def __init__(self):
        self.device_id = ""
        self.install_id = ""

    @staticmethod
    def _get_trace_id():
        """
        gen trace id
        """
        timestamp = "%x" % (round(time.time() * 1000) & 0xffffffff)
        random_str = str(timestamp) + "010" + rand_str(17) + "0000"
        trace_id = "00-"
        trace_id += random_str
        trace_id += "-"
        trace_id += random_str[:16]
        trace_id += '-01'
        return trace_id

    def post_device_register(self):
        """
        send device_register request
        """
        timestamp_ms = round(time.time() * 1000)
        timestamp = timestamp_ms // 1000

        host = 'http://log-va.tiktokv.com'
        url = "/service/2/device_register/"
        query_args = f"ac=wifi" \
                     f"&aid={aid}" \
                     f"&app_name=musical_ly" \
                     f"&version_code=250625" \
                     f"&version_name={app_ver}" \
                     f"&device_platform=android" \
                     f"&ab_version={app_ver}" \
                     f"&ssmix=a" \
                     f"&device_type=AOSP+on+taimen" \
                     f"&device_brand=Android" \
                     f"&language=zh" \
                     f"&os_api=28" \
                     f"&os_version=9" \
                     f"&openudid={openudid}" \
                     f"&manifest_version_code=2022506250" \
                     f"&resolution=1440*2712" \
                     f"&dpi=560" \
                     f"&update_version_code=2022506250" \
                     f"&_rticket={timestamp_ms}" \
                     f"&app_type=normal" \
                     f"&sys_region={tz}" \
                     f"&timezone_name=Asia%Singapore" \
                     f"&app_language=zh-Hans" \
                     f"&carrier_region={tz}" \
                     f"&fake_region={tz}" \
                     f"&timezone_offset=28800" \
                     f"&host_abi=armeabi-v7a" \
                     f"&locale=zh-Hans" \
                     f"&ac2=wifi5g" \
                     f"&uoo=1" \
                     f"&op_region={tz}" \
                     f"&build_number={app_ver}" \
                     f"&region={tz}" \
                     f"&ts={timestamp}" \
                     f"&cdid={cdid}"

        body_src = json.dumps(device_info)
        body = do_tt_encrypt(body_src)
        print(body)
        query_str = f"{host}{url}?{query_args}"

        body_md5 = hash_md5_hex(body).upper()
        x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon = do_sign("android",
                                                                    app_ver=app_ver,
                                                                    sdk_ver=sdk_ver,
                                                                    device_id=self.device_id,
                                                                    timestamp=timestamp,
                                                                    device_model="",
                                                                    os_version=os_version,
                                                                    req_type="POST",
                                                                    req_url=query_str,
                                                                    body=body,
                                                                    android_id=openudid
                                                                    )

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
            "x-ss-dp": str(aid),
            'x-tt-trace-id': self._get_trace_id(),
            'user-agent': user_agent,
            'accept-encoding': 'gzip, deflate',
            "x-argus": x_argus,
            "x-ladon": x_ladon,
            "x_gorgon": x_gorgon,
            "x-khronos": x_khronos,
            "x-tyhon": x_tyhon,
        }

        response = post_request(host, url, query_args, headers, body)
        obj = json.loads(response)
        self.device_id = obj["device_id_str"]
        self.install_id = obj["install_id_str"]

        print("device_id_str", obj["device_id_str"])
        print("install_id_str", obj["install_id_str"])
        return response

    def send_app_alert_check(self):
        """
        send app_alert_check request activation device id
        """
        timestamp_ms = round(time.time() * 1000)
        timestamp = timestamp_ms // 1000

        host = 'http://log-va.tiktokv.com'
        url = "/service/2/app_alert_check/"
        query_args = f"timezone=8.0" \
                     f"&device_id={self.device_id}" \
                     f"&ac=wifi" \
                     f"&aid={aid}" \
                     f"&app_name=musical_ly" \
                     f"&version_code=250625" \
                     f"&version_name={app_ver}" \
                     f"&device_platform=android" \
                     f"&ab_version={app_ver}" \
                     f"&ssmix=a" \
                     f"&device_type=AOSP+on+taimen" \
                     f"&device_brand=Android" \
                     f"&language=zh" \
                     f"&os_api=28" \
                     f"&os_version=9" \
                     f"&openudid={openudid}" \
                     f"&manifest_version_code=2022506250" \
                     f"&resolution=1440*2712" \
                     f"&dpi=560" \
                     f"&update_version_code=2022506250" \
                     f"&_rticket={timestamp_ms}" \
                     f"&app_type=normal" \
                     f"&sys_region=CN" \
                     f"&timezone_name=Asia%2FShanghai" \
                     f"&app_language=zh-Hans" \
                     f"&carrier_region={tz}" \
                     f"&fake_region={tz}" \
                     f"&timezone_offset=28800" \
                     f"&host_abi=armeabi-v7a" \
                     f"&locale=zh-Hans" \
                     f"&ac2=wifi5g" \
                     f"&uoo=1" \
                     f"&op_region={tz}" \
                     f"&build_number={app_ver}" \
                     f"&region=CN" \
                     f"&ts={timestamp}" \
                     f"&cdid={cdid}" \
                     f"&req_id=120126cf-1934-40d5-a803-315925967fb6" \
                     f"&cronet_version=4cac2dc1_2022-07-06" \
                     f"&ttnet_version=4.1.89.18-tiktok"

        query_str = f"{host}{url}?{query_args}"
        x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon = do_sign("android",
                                                                    app_ver=app_ver,
                                                                    sdk_ver=sdk_ver,
                                                                    device_id=self.device_id,
                                                                    timestamp=timestamp,
                                                                    device_model=device_model,
                                                                    os_version=os_version,
                                                                    req_type="GET",
                                                                    req_url=query_str,
                                                                    android_id=openudid
                                                                    )

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
            "x-ss-dp": str(aid),
            'x-tt-trace-id': self._get_trace_id(),
            'user-agent': user_agent,
            'accept-encoding': 'gzip, deflate, br',
            "x-argus": x_argus,
            "x-ladon": x_ladon,
            "x_gorgon": x_gorgon,
            "x-khronos": x_khronos,
            "x-tyhon": x_tyhon,
        }

        response = get_request(host, url, query_args, headers)
        obj = json.loads(response)


if __name__ == '__main__':
    device = DeviceRegister()
    device.post_device_register()
    device.send_app_alert_check()
