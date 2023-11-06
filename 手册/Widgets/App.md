# App 应用

<blockquote>
  App Widget 用于描述应用的基本信息。 每个应用只有一个，名称固定为 app.json
  放置在应用的根目录。
</blockquote>

**约定**

1. 示例中约定应用根目录为 `/data/app`, 实际编写时需替换为应用根目录。
2. 使用 `<>` 标识自行替换的内容。 例如: `icon-<图标名称>`, 实际编写时应替换为: `icon-foo`, `icon-bar` ...
3. DSL 字段大小写敏感, 例如 `adminRoot` 与 `adminroot` 不同

<Detail title="查看示例 /data/app/app.json">

```json
{
  "xgen": "1.0",
  "name": "::Demo Application",
  "short": "::Demo",
  "description": "::Another yao application",
  "version": "0.10.2",
  "menu": { "process": "flows.app.menu", "args": ["demo"] },
  "setup": "scripts.demo.Data",
  "adminRoot": "admin",
  "optional": {
    "hideNotification": true,
    "hideSetting": false
  }
}
```

</Detail>

## App DSL

| 字段        | 类型   | 必填项 | 默认值  | 示例                                                | 说明                                                                                                                                                                                                                                                       |
| ----------- | ------ | ------ | ------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| xgen        | Enum   |        | `0.9`   | `1.0`                                               | XGen 界面引擎版本, 推荐使用 `1.0` 版，旧版已停止维护                                                                                                                                                                                                       |
| name        | String | 是     |         | `Demo Application`                                  | 应用名称, 支持多语言。                                                                                                                                                                                                                                     |
| version     | String |        | `1.0.0` | `1.3.6`                                             | 应用版本号，建议遵循 [Semantic Versioning 标准](https://semver.org/lang/zh-CN/)                                                                                                                                                                            |
| short       | String |        |         | `Demo`                                              | 应用简称, 支持多语言。                                                                                                                                                                                                                                     |
| description | String |        |         | `Another yao application`                           | 应用介绍, 支持多语言。                                                                                                                                                                                                                                     |
| adminRoot   | String |        | `yao`   | `admin`                                             | 管理后台路由前缀。例如 `admin` 管理后台入口路由为 `http://<服务器IP或域名>:<YAO_PORT>/admin/`                                                                                                                                                              |
| menu        | Object |        |         | `{ "process": "flows.app.menu", "args": ["demo"] }` | 管理后台菜单读取处理器. `menu.process` String 处理器名称, `menu.args` []Any 处理器参数表                                                                                                                                                                   |
| setup       | String |        |         | `scripts.demo.Data`                                 | 应用首次安装后运行的处理器名称， 一般可以用来建立初始化数据；处理器第一个参数为应用配置信息。 支持使用 `studio` 命名空间，调用 studio 脚本函数；例如: `studio.build.CreateModels`, 安装后调用 `/data/app/studio/build.js` 中定义的 `CreateModels()` 方法。 |
| optional    | Object |        | `{}`    | `{"hideNotification": true, "hideSetting": false}`  | 应用可选配置项。                                                                                                                                                                                                                                           |

### menu Object

| 字段    | 类型         | 必填项 | 默认值 | 示例             | 说明         |
| ------- | ------------ | ------ | ------ | ---------------- | ------------ |
| process | String       | 是     |        | `flows.app.menu` | 处理器名称   |
| args    | Array\<Any\> |        | `[]`   | `["demo"]`       | 处理器参数表 |

**处理器返回值数据结构约定:**

<Detail title="查看返回值示例">

```json
[
  {
    "blocks": 0,
    "icon": "icon-activity",
    "name": "图表",
    "path": "/x/Chart/dashboard",
    "visible_menu": 0
  },
  {
    "blocks": 0,
    "icon": "icon-book",
    "name": "表格",
    "path": "/x/Table/pet",
    "visible_menu": 1,
    "children": [
      {
        "blocks": 0,
        "icon": "icon-book",
        "name": "宠物列表",
        "path": "/x/Table/pet",
        "visible_menu": 1
      },
      {
        "blocks": 0,
        "icon": "icon-book",
        "name": "用户列表",
        "path": "/x/Table/user",
        "visible_menu": 1
      }
    ]
  }
]
```

</Detail>

| 字段         | 类型    | 必填项 | 说明                                                                                         |
| ------------ | ------- | ------ | -------------------------------------------------------------------------------------------- |
| name         | String  | 是     | 菜单名称                                                                                     |
| icon         | String  | 是     | 菜单图标，一级菜单有效. 命名为 `icon-<图标名称>`， [查看可用图标](https://feathericons.com/) |
| path         | String  | 是     | 菜单路由地址，**不含管理后台路由前缀**                                                       |
| blocks       | Integer | 是     | 是否显示为图标, 二级菜单有效 `0` 文字, `1` 图标                                              |
| visible_menu | Integer | 是     | 二级菜单默认显示方式, `1` 打开， `0` 关闭                                                    |
| children     | Array   | 是     | 二级菜单列表                                                                                 |

### optional Object

| 字段             | 类型    | 必填项 | 默认值  | 示例   | 说明                                          |
| ---------------- | ------- | ------ | ------- | ------ | --------------------------------------------- |
| hideNotification | Boolean |        | `true`  | `true` | 隐藏系统通知面板。 **字段名大小写敏感**       |
| hideSetting      | Boolean |        | `false` | `true` | 隐藏导航栏下方配置菜单。 **字段名大小写敏感** |

## API

| 请求方式 | 路由                           | 鉴权         | Payload                                                             | 说明                                                                                                                        |
| -------- | ------------------------------ | ------------ | ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `GET`    | `/api/__yao/app/setting`       | `-`          |                                                                     | 返回应用配置信息                                                                                                            |
| `POST`   | `/api/__yao/app/setting`       | `-`          | `{"sid":"<会话ID>", "lang":"zh-cn", "time": "2022-10-10 22:00:10"}` | 上报浏览环境, 返回应用配置信息                                                                                              |
| `GET`    | `/api/__yao/app/icons/:name`   | `-`          |                                                                     | 返回应用图标数据, `:name` 为图标文件名，例如 `app.ico`, `app.icns`, `app.png`                                               |
| `GET`    | `/api/__yao/app/menu`          | `bearer-jwt` |                                                                     | 返回应用菜单                                                                                                                |
| `POST`   | `/api/__yao/app/service/:name` | `bearer-jwt` | `{"method":"<函数名称>", "args":[<参数表...>]}`                     | 调用云函数, `:name` 为 Service ID. 例如 `/data/services/test.js` ID 为 `test`, `/data/services/foo/bar.js` ID 为 `foo.bar`, |

## 处理器

| 处理器          | 参数表           | 返回值           | 说明                                                      |
| --------------- | ---------------- | ---------------- | --------------------------------------------------------- |
| yao.app.setting |                  | 返回应用配置信息 | 读取应用配置                                              |
| yao.app.menu    |                  | 返回菜单         | 读取应用菜单                                              |
| yao.app.icons   | `[<图标文件名>]` | 返回图标文件数据 | 读取图标文件目录下文件数据 `/data/app/icons/<图标文件名>` |

[查看处理器手册](../处理器/App.mdx)

## 应用图标

应用图标放置在 `icons` 目录，文件约定为:

| 文件名   | 绝对路径                   | 说明          |
| -------- | -------------------------- | ------------- |
| app.png  | `/data/app/icons/app.png`  | PNG 格式图标  |
| app.ico  | `/data/app/icons/app.ico`  | ICON 格式图标 |
| app.icns | `/data/app/icons/app.icns` | ICNS 格式图标 |
