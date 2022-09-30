# Change Log

## [V2.4.0】 - 2022-09-30

### Added

- Supported the latest TikTok Android **risk information report** `ri/report`! See the [android device register demo](demo/android_device_register.py). Now both ios and android platform are supported.
- Supported the latest Tiktok both Android and iOS **Cylons** algorithm! See the `get_xcylons` in [api](doc/API#get_xcylons).
- Supported query your **account useage** of our service. See the `/user/get_info` in [api](doc/API#user_get_info).

### Improved 

- None

### BugFix

- None

## [V2.3.0] - 2022-09-23

### Added

- Supported the latest TikTok iOS **risk information report** `ri/report`! See the [ios device register demo](demo/ios_device_register.py). And the android platform is coming soon.

### Improved

- Improved the **ios device template** significantly, please update it and decrease the risk control by tiktok.

### BugFix

- None

## [v2.2.0] - 2022-09-15

### Added

- Supported lastest tiktok web signature x-bogus as well as _signature;

### Improved 

- None

### BugFix

- Fixed the bug of url encoding.

## [v2.1.0] - 2022-09-08

### Added

- Supported lastest tiktok-lite 26.4.4, aid is 1340.

### Improved 

- None

### BugFix

- None

## [v2.0.0] - 2022-09-06

### Added

- Supported `sdi/get_token` on both android and ios platform. Ref [API](doc/API.md) `encrypt_get_token` and `decrypt_get_token` interface to get more detail information.
- Added new api `get_device_template` to get android/ios device template. Now you can generate device fingerprint easily with our device template. Ref [API](doc/API.md) to get more information too.

### Improved

- Use new api `get_device_register_body` to replace the old deprecated api `tt_encrypt`. The new api significantly reduces the complex of calling.

### BugFix

- Supported automatically get **aid** from the request body of `get_sign` api, if the aid parameter is not explicitly passed from the url.

## [v1.1.0] - 2022-08-29

### Added

- Added the demo of `sdi/get_token` on **iOS** platform. Presently, we do not provide the enc/dec method of this token, because in my opinion, it's not hard for you with our signature api. However, if this is necessary for my big customers, I will support it quickly.

### Improved

- None

### BugFix

- None

## [v1.0.0] - 2022-08-26

### Added

- None

### Improved

- Changed how free key is used. Now each free key is available for 2 days with 1 api call every 1 second. So you can test mostly business scenario you want.
- 改变免费试用密钥的使用策略：从以前的每个 key 只能支持每 5 秒钟调用一次提升到每秒钟可调用一次(相应地我们将每个 key 的使用时长从 5 天缩减到 2 天)。现在你可以测试你想要的绝大部分业务场景了。

### BugFix

- None