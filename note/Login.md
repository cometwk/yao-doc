# Login

## DSL

### 定义

文件放在 logins 目录中, 文件扩展名为 `.login.json` 。

| DSL 文件                 | Widget ID |
| ------------------------ | --------- |
| /logins/admin.login.json | `admin`   |
| /logins/user.login.json  | `user`    |

**管理员登录界面描述文件固定为 admin.login.json, 用户登录界面描述固定为 user.login.json。**

### 格式

```ts
// widgets/login/types.go
declare namespace Login {
  interface DSL {
    id?: string;
    name?: string;
    action?: ActionDSL;
    layout?: LayoutDSL;
    thirdPartyLogin?: ThirdPartyLoginDSL[];
  }
  interface ActionDSL {
    process?: string;
    args?: any[]; // 由于 Go 中使用了 interface{}，这里使用 any[] 表示一个任意类型数组
  }
  interface LayoutDSL {
    entry?: string;
    captcha?: string;
    cover?: string;
    slogan?: string;
    site?: string;
  }
  interface ThirdPartyLoginDSL {
    title?: string;
    href?: string;
    icon?: string;
    blank?: boolean;
  }
}

declare var login: Login.DSL;
```

> 字段


| 字段   | 类型   | 必填项 | 默认值 | 示例         | 说明                                                 |
| ------ | ------ | ------ | ------ | ------------ | ---------------------------------------------------- |
| name   | String | 是     |        | `User Login` | 登录界面名称, 支持多语言                             |
| layout | Object | 是     |        |              | 页面布局定义。设置登录界面封面、登录后跳转路由地址等 |
| action | Object | 是     |        |              | 用户登录逻辑处理器                                   |


`Widget ID` 特别说明 
- `Widget ID` : 通用字段, 描述某个类型下的唯一ID，即局部 ID。
- ID取值规则: 例如 `/logins/x/y/admin.login.json`, 此时 id = `x.y.admin` 
- 当然，`x.y.admin` 在此场景下不适用。按上面的定义， 其值只有 `admin` or `user`


> layout Object

| 字段   | 类型   | 必填项 | 默认值 | 示例                                  | 说明                                                                                                                                   |
| ------ | ------ | ------ | ------ | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| entry  | String | 是     |        | `/x/Table/pet`                        | 成功登录后，转向此地址。**注意: 不含管理后台路由前缀**                                                                                 |
| cover  | String |        |        | `/assets/images/login/cover.svg`      | 登录界面封面图片, 图片相对地址。可将图片放到应用公开目录 `public` ，例如: `/public/images/cover.png`, 填写的地址为 `/images/cover.png` |
| slogan | String |        |        | `Make Your Dream With Yao App Engine` | 登录界面广告语，支持多语言                                                                                                             |
| site   | String |        |        | `https://yaoapps.com`                 | 登录界面封面图片下方链接地址                                                                                                           |

> action Object

| 字段    | 类型            | 必填项 | 默认值 | 示例              | 说明                                                          |
| ------- | --------------- | ------ | ------ | ----------------- | ------------------------------------------------------------- |
| process | String          | 是     |        | `yao.login.Admin` | 处理器名称                                                    |
| args    | Array\<String\> | 是     |        | `[":paylod"]`     | 处理器参数表, 与 API `in` 编写方法一致, 接收登录 API 请求数据 |

### 示例

管理员登录示例 `/logins/admin.login.json`

```json
{
  "name": "::Admin Login",
  "action": { "process": "yao.login.Admin", "args": [":payload"] },
  "layout": {
    "entry": "/x/Chart/dashboard",
    "cover": "/assets/images/login/cover.svg",
    "slogan": "::Make Your Dream With Yao App Engine",
    "site": "https://yaoapps.com?from=admin-login"
  }
}
```


用户登录示例 `/logins/user.login.json`

```json
{
  "name": "::User Login",
  "action": { "process": "scripts.user.Login", "args": [":payload"] },
  "layout": {
    "entry": "/x/Table/pet",
    "cover": "/assets/images/login/cover.svg",
    "slogan": "::Make Your Dream With Yao App Engine",
    "site": "https://yaoapps.com?from=user-login"
  }
}
```

## 前端

> 路由

- 管理员登录: `http://<IP|域名>:<YAO_PORT>/<管理后台路由前缀>/login/admin`
- 用户登录: `http://<IP|域名>:<YAO_PORT>/<管理后台路由前缀>/login/user`


**处理器返回值数据结构约定:**

<Detail title="查看返回值示例">

```json
{
  "expires_at": 1667055608,
  "menus": [
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
  ],
  "studio": {
    "expires_at": 1667055608,
    "port": 5077,
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
  },
  "token": "h_UmRPqVgnLEpl3W03D07tblWbpS1oC5uTtFOLbvlKc",
  "user": {
    "email": "xiang@iqka.com",
    "extra": { "sex": "男" },
    "id": 1,
    "mobile": null,
    "name": "管理员",
    "status": "enabled",
    "type": "admin"
  }
}
```

| 字段       | 类型   | 必填项 | 说明                                                     |
| ---------- | ------ | ------ | -------------------------------------------------------- |
| expires_at | Int    | 是     | 会话过期时间                                             |
| menus      | Array  | 是     | 应用菜单 [menu Object](App.mdx)                          |
| studio     | Object |        | Studio JWT, 可通过管理员登录处理器获取 `yao.login.Admin` |
| token      | String | 是     | JWT                                                      |
| user       | Object | 是     | 用户资料摘要信息                                         |


**自定义登录脚本示例:**

登录脚本示例 `/scirpts/user.js`

```javascript
/**
 * 自定义用户登录逻辑
 * @param {*} payload
 */
function Login(payload) {
  log.Trace("[user] Login %s", payload.email);

  if ("<登录信息校验失败>") {
    throw new Exception("登录失败", 403);
  }

  return {
    menus: "<应用菜单>",
    expires_at: "<会话过期时间>",
    token: "<JWT>",
    user: "<用户信息>",
  };
}
```


## API

```http
widgets.login(4)

POST /api/__yao/login/admin process: yao.login.Admin
GET  /api/__yao/login/admin/captcha process: yao.utils.Captcha

POST /api/__yao/login/user process: scripts.user.Login
GET  /api/__yao/login/user/captcha process: yao.utils.Captcha
```

| 请求方式 | 路由                           | 鉴权 | Payload                                                                                                                                                        | 说明                   |
| -------- | ------------------------------ | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| `GET`    | `/api/__yao/login/:id/captcha` | `-`  |                                                                                                                                                                | 获取用户登录图形验证码 |
| `POST`   | `/api/__yao/login/:id`         | `-`  | `{"email": "xiang@iqka.com","password": "A123456p+", "captcha": {"id": "XtuV3ZufGzhtJoxoGfhn", "code": "41804"}, "sid": "9YJhcWQxPt-V-G1aGsx021667052000536"}` | 提交用户登录           |

## 处理器

| 处理器          | 参数表                 | 返回值       | 说明                                                                                       |
| --------------- | ---------------------- | ------------ | ------------------------------------------------------------------------------------------ |
| yao.login.Admin | `[<用户登录表单数据>]` | 返回登录信息 | 查询 `xiang.user` 模型( `xiang_user` 数据表), 检查用户邮箱密码，验证用户登录并返回登录信息 |

[查阅处理器手册](../处理器/Login.md)

**登录逻辑编排常用处理器**

| 处理器                     | 参数表                               | 返回值     | 说明                                           |
| -------------------------- | ------------------------------------ | ---------- | ---------------------------------------------- |
| yao.utils.Captcha          |                                      | 图形验证码 | 返回图形验证码 [查看手册](../处理器/Utils.mdx) |
| yao.utils.CaptchaValidate  | `["<验证码ID>", "<验证码>"]`         |            | 图形验证码校验 [查看手册](../处理器/Utils.mdx) |
| yao.utils.PasswordValidate | `["<明文密码>", "<密文密码>"]`       |            | 密码校验 [查看手册](../处理器/Utils.mdx)       |
| yao.utils.JwtMake          | `["用户ID", "<用户数据>", "<选项>"]` |            | 生成 JWT [查看手册](../处理器/Utils.mdx)       |
| yao.utils.JwtValidate      | `["<Token>"]`                        |            | JWT 校验 [查看手册](../处理器/Utils.mdx)       |
