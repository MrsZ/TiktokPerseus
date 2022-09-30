# TikTokApi

The **strongest** and **cheapest** TikTok signature/encryption protocol service on the market, stably support for a single customer with an average of millions of calls per day. 市面上**最强**, 价格最实惠的 TikTok 签名/加密协议服务。稳定支持单客户日均百万级调用。

Contact: 
* gmail: reverse4free@gmail.com
* Telegram: https://t.me/reverse4free2


## ⚠️WARNING WARNING WARNING / ⚠️警告警告警告

For understanding our service clearly, you must read 3 documents carefully with just 3 minutes.
- [API Description](doc/API.md) to see what interfaces we have supported and how to invoke these APIs.
- [DEMO HANDBOOK](doc/demo_handbook.md) to see how to run the demo with our service.
- [UPDATE LOG](UPDATE_LOG.md) to see what new capabilities we have added recently.

为了快速清晰地了解我们目前提供的服务能力，请您务必花费 3 分钟仔细阅读下面 3 个文档：
- [API Description](doc/API.md)：快速了解我们当前支持了 TikTok 哪些接口，以及如何使用这些接口；
- [DEMO HANDBOOK](doc/demo_handbook.md)：快速了解我们提供了哪些 demo，以及如何运行测试这些 demo;
- [UPDATE LOG](UPDATE_LOG.md): 快速了解我们服务的更新日志，了解我们最近新增了什么能力；


## BREAKING NEWS / 劲爆更新

### 2022-09-30 v2.4.0

* Supported the latest TikTok Android **risk information report** `ri/report`! See the [android device register demo](demo/android_device_register.py). Now both ios and android platform are supported.
* Supported the latest Tiktok both Android and iOS **Cylons** algorithm! See the `get_xcylons` in [api](doc/API#get_xcylons).
* Supported query your **account useage** of our service. See the `/user/get_info` in [api](doc/API#user_get_info).

* 已经支持了最新版本的 Android 平台 TikTok 设备风险上报接口 `ri/report`！详情见[android device register demo](demo/android_device_register.py)。现在双平台我们都支持了。
* 已经支持了最新版的双平台 X-Cylons 算法。详情见`get_xcylons` in [api](doc/API#get_xcylons)。
* 已经支持了付费账户的使用情况查询服务。详情见`/user/get_info` in [api](doc/API#user_get_info)。

### 2022-09-23 v2.3.0

* Supported the latest TikTok iOS **risk information report** `ri/report`! See the [ios device register demo](demo/ios_device_register.py). And the android platform is coming soon.
* Improved the **ios device template** significantly, please update it and decrease the risk control by tiktok.

* 已经支持了最新版本的 iOS 平台 TikTok 设备风险上报接口 `ri/report`！详情见[ios device register demo](demo/ios_device_register.py)。另外，android 版马上到来！
* 大幅度提升了 iOS 设备模版的效果，请务必使用最新的模版以减少被风控的风险；

### 2022-09-15 v2.2.0

* Supported the latest TikTok Web Signature **X-bogus** as well as **_signature**! Look at the [demo](https://github.com/reverse4free/TiktokPerseusWeb) project to find out how to use it!
* The X-Cylons is coming soon~

* 已经支持最新版本的 TikTok Web 签名 **X-bogus** 和 **_signature**，快来试试吧！具体使用 demo 请参考 [demo](https://github.com/reverse4free/TiktokPerseusWeb)。
* X-Cylons 字段的加解密算法也正在攻破中，敬请期待。

### 2022-09-08

* **The latest Tiktok-lite 26.4.4 is supported!**, try our server and have fun! Now we supported 1180, 1233, 1340.
* The web signature is coming soon, so stay tuned!

* **已经支持最新版 Tiktok-lite 26.4.4 的签名算法**, 快来试试吧！现在我们支持 1180, 1233, 1240 三款最主流的 Tiktok app 了。
* 最新版本的 web 签名我们也快搞定了，敬请期待！


## English Version

We stably support both **android/ios** platform and *mostly version* of the TikTok api including the latest **X-Argus**, **X-Ladon**, **X-Gorgon**, **X-Khronos**, **X-Tyhon** as well as some other core algorithms. 

**Profitability is important for us, but finding long-term partners is even more important**. So for demonstrating our technical capability, all of our Apis is free now! You can contact us by gmail or telegram to apply for test key(10 USDT) of our server. Each test key is available for 4 days, and support 1 QPS. For paying users, we can **provide customized services**, no mater what QPS you need we can provide.

We promise:
* We will permanently support both Android/iOS platform. If you are also interested in the web platform, you can tell us, and we can support it soon. Please believe in our technical strength.
* We will continue to follow up with the latest version of the TikTok client, and the delay will never exceed 1 month.
* Currently we will focus on TikTok, if this method can continue to be profitable, then we will also try to expand other applications;

Please note:
* Due to personal safety reasons, we temporarily do not undertake the reverse capability of APPs in China's local area, so although it is easy for us to crack Douyin, we will not provide cracking services for it, including other apps such as Kuaishou, Meituan, etc;
* We are short of money, but we prefer our lives, so we don’t chat. At the same time, if we suspect that you are a security classmate of the relevant company, we will stop cooperation immediately, and we will not give any tips and feedback for free users;
* We are short of money, but we have a bottom line, we don't pay attention to what you do, but if we find that you have done some bottom line problems such as child pornography, we will stop the service immediately, whether you are a paying user or not;
* Recommend using telegram to communicate with us;
* We will provide a complete demo (dual-platform device registration and activation) and api introduction documents to demonstrate how to use this service, so please read the relevant documents carefully. If you really encounter unknown problems, please contact us directly;

Thinking of this for a while, our slogan is: Reverse For (Financial) Free!


## 中文版本

我们提供 TikTok（抖音海外版）**双平台**（Android/iOS）**最新**的核心风控算法——*5神算法*，以及其它一些关键的**加密加签算法**，稳定支持绝大部分版本。

**盈利对我们来说很重要，但寻求到长期合作伙伴更重要**。所以为了体现我们的技术实力，当前整个服务免费对外提供。大家可以通过 gmail 或者 tg 联系我们申请测试 key(10 USDT)，此 key 允许大家每隔 1 秒调用一次我们的服务，有效期为 4 天。后续可以为付费用户提供定制化服务，QPS 这块绝对不用担心。

我们承诺：
* 我们会永久支持 Android/iOS 双平台，如果大家对 web 平台也感兴趣的话，可以告知我们，我们很快也可以支持起来，请相信我们的技术实力；
* 我们会持续跟进最新版本的 TikTok 客户端，延迟时间绝对不会高于 1 个月；
* 当前我们会专注在 TikTok 上，如果这条路可以持续盈利，那么我们也会尝试扩展其他应用；

需要注意：
* 因为人身安全的原因，我们暂时不承接针对中国本土区域 APP 的逆向能力，所以虽然攻破抖音对我们来说易如反掌，但我们不会提供针对抖音的破解服务，包括快手、美团等；
* 我们缺钱，但更惜命，所以不闲聊，同时如果我们怀疑你是相关公司的安全人员，那么会立即停止合作，且对于免费用户我们不会给出任何提示和反馈；
* 我们缺钱，但有底线，我们并不关注你做了什么，但如果发现你拿去做了一些诸如儿童色情之类的底线问题，我们会立即停止服务，无论你是否为付费用户；
* 推荐使用 telegram 同我们沟通，效率更高；
* 我们会提供完整 demo(双平台的设备注册与激活) 和 api 介绍文档演示如何使用此服务，所以请一定认真阅读相关文档，如果真的遇到未知问题，请直接联系我们;

暂时就想到了这些，我们的口号是： Reverse For (financial) Free!