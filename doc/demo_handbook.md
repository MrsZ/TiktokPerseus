# Demo Handbook / Demo 测试手册

## Forward / 前言

Presently, we provide a complete demo (dual-platform device registration and activation) for the users to do some test of our service. And to launch the demo successfully you should apply for a free test key from us by email/qq.

当前，我们提供了 android/iOS 双平台的设备注册 demo，供大家测试我们的签名服务。为了正确运行该测试 demo，你需要先通过 gmail/telegram 来联系我们申请 10$ 的测试 key。

## Step

### English version

1. `git clone https://github.com/reverse4free/TiktokPerseus.git` 
2. `cd TiktokPerseus/demo`
3. replace the key of key.py with the test key applied from us.
4. `python android_device_register.py` # launch the android device register and activation demo, you can get an device_id and install_id
5. `python ios_device_register.py` # the ios demo
6. you can change the device info and app info by yourself to generate new did and iid;
7. have fun!

> Tips: please read the content below with [api.md](API.md).

In this demo, we supported 4 core risk control apis of 3 core biz scenarios, covering Tiktok's current strongest risk control scenario:
* General scenario:
    * core signature api `do_sing_v5`: get the signature result, such as x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon;
* Device template getting: `DeviceRegister.process_dev_info("android" or "ios")` in demo
    * get devive tenplate api `do_get_dev_tmpl`: get the device template, android or ios, from our server. For more information about device template please refer the [api.md](API.md). Device fingerprints are the core of risk control countermeasures, and many interfaces are strongly correlated. Therefore, in order to reduce the difficulty of analyzing and understanding device fingerprints, and to avoid filling ib different device fingerprint data through different interfaces, which may cause risk control , we directly return the general device template through this interface, you only need to fill in the correct value as needed.
* Device register:`DeviceRegister.post_device_register()` in demo
    * Device registration request body Encryption API `get_device_register_body`: Connotation `tt_encrypt` API(**Deprecated**), user only needs to send the correct device fingerprint template, which filled in correct value, as a parameter to the API. We automatically complete the complex format conversion as well as body encryption.
* Device activate:  `DeviceRegister.send_app_alert_check()` in demo
* Sec device token getting: `DeviceRegister.get_token()` in demo
    * SecDeviceToken encrypt interface `encrypt_get_token`: encrypt the device fingerprint to get the correct request body of `sdi/get_token`. The parameter is the same as `get_device_register_body`;
    * SecDeviceToken decrypt interface `decrypt_get_token`: decrypt the response from `sdi/get_token`, you can get the important `token` from the result.
* RI(maybe risk info?) Report: `DeviceRegister.post_ri_report()` in demo(just ios now, android is coming soon).

Finally, you can get three important id:
* device id
* install id
* sec device token
* risk information report


### 中文版

1. `git clone https://github.com/reverse4free/TiktokPerseus.git` 
2. `cd TiktokPerseus/demo`
3. 使用从我们这申请的测试 key 替换 key.py 中的 key 值.
4. `python android_device_register.py` # 测试 android 平台的设备注册，成功的话你会收到 device_id and install_id
5. `python ios_device_register.py` # 测试 ios 平台
6. 你可以按需更改 demo 中的 device info 和 APP info，以便生成任意的新 did/iid;
7. have fun!


> Tips: 下面内容配合 [api.md](API.md) 阅读体验更佳。

在这个 demo 中，我们主要支持 3 个场景所涉及到 4 个核心风控接口，以及一个通用的核心签名接口，覆盖了 Tiktok 目前最强风控对抗场景：
* 绝大部分业务场景通用：
    * 核心签名接口 `do_sign_v5`: 完成诸如 x_ladon, x_argus, x_gorgon, x_khronos, x_tyhon 的签名
* 设备模版获取场景：Demo 中 `DeviceRegister.process_dev_info("android" or "ios")`
    * 设备模版接口 `do_get_dev_tmpl`: 从服务端获取 android/ios 的通用设备模版, json 类型（关于该模版更详细的信息请参考 [api.md](API.md)）。**设备指纹是风控对抗核心中的核心，不少接口之间具有强关联性，所以为了减轻大家对设备指纹的分析和理解难度，同时避免在不同接口传入不同的设备指纹数据造成被风控，我们直接通过该接口返回通用设备模版，大家只需要按需往里面填写正确的值即可**。
* 设备注册场景：Demo 中 `DeviceRegister.post_device_register()`
    * 设备注册请求 body 加密接口 `get_device_register_body`: 内涵 `tt_encrypt` 接口(已经废弃), 用户只需要把填写正确的设备指纹模版作为参数传送给改接口即可。我们会自动完成复杂的格式转换和 body 加密功能。
* 设备激活场景：Demo 中 `DeviceRegister.send_app_alert_check()`
* 获取 Sec Device Token 场景：Demo 中 `DeviceRegister.get_token()`
    * SecDeviceToken 加密接口 `encrypt_get_token`: 将设备指纹按需加密，得到 `sdi/get_token` 正确的请求 body, 传参方式同 `get_device_register_body`;
    * SecDeviceToken 解密接口 `decrypt_get_token`: 将服务端返回数据进行解密，从中提取关键的 token;
* RI(Risk Info?) 上报：Demo 中 `DeviceRegister.post_ri_report()`, 目前只提供 ios ，android 即将支持

最终你会获取已经完成设备注册和风控注册的：
* device id
* install id
* sec device token
* 风控设备信息上报