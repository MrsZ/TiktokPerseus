# Demo Handbook / Demo 测试手册

## Forward / 前言

Presently, we provide a complete demo (dual-platform device registration and activation) for the users to do some test of our service. And to launch the demo successfully you should apply for a free test key from us by email/qq.

当前，我们提供了 android/iOS 双平台的设备注册 demo，供大家测试我们的签名服务。为了正确运行该测试 demo，你需要先通过 gmail/qq 来联系我们申请免费的测试 key。

## Step

### English version

1. `git clone https://github.com/reverse4free/TiktokPerseus.git` 
2. `cd TiktokPerseus/demo`
3. replace the key of key.py with the test key applied from us.
4. `python android_device_register.py` # launch the android device register and activation demo, you can get an device_id and install_id
5. `python ios_device_register.py` # the ios demo
6. you can change the device info and app info by yourself to generate new did and iid;
7. have fun!

We also supported the `sid/get_token` api in ios demo, but you must do some manual modification of the `ios_device_register.py` before you testing it. To prevent us from being tracing, we do not upload the `get_token_req_body.bin` file used by this api, because this file contains some information of our real test device. This file is dumped from the real test device, we get it from the Charles network capture tool, so you can get it by yourself with any network capture tool. 

> NOTE!!! If you want to support this core secure api automatically, you can give me a quote, it's not too hard for us.

### 中文版

1. `git clone https://github.com/reverse4free/TiktokPerseus.git` 
2. `cd TiktokPerseus/demo`
3. 使用从我们这申请的测试 key 替换 key.py 中的 key 值.
4. `python android_device_register.py` # 测试 android 平台的设备注册，成功的话你会收到 device_id and install_id
5. `python ios_device_register.py` # 测试 ios 平台
6. 你可以按需更改 demo 中的 device info 和 APP info，以便生成任意的新 did/iid;
7. have fun!

在 ios demo 中我们也添加了支持 `sid/get_token` 接口的测试代码。但是出于保护自己的原因，你需要做一定的手工改动才能正确运行此接口的测试函数。测试改函数需要一个 `get_token_req_body.bin` 文件，此文件我们暂时不提供，因为里面含有大量个人测试设备的信息。但你可以通过诸如 Charles 之类的抓包工具从你自己的真实设备中抓取该请求中的 request body 信息，然后保存为 `get_token_req_body.bin` 就可以正确运行此函数的测试代码了。

> 注意！这是一个关键的安全接口函数，如果你需要我们将之协议化、自动化，只要你能给出合适的报价我们也很快就能搞定，对我们来说真的不难。

