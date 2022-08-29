# Change Log

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