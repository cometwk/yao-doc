# 使用会话数据

<blockquote>
  <p>
    可以使用 <strong>session.*</strong>,<strong>Captcha</strong>,
    <strong>PasswordValidate</strong>
    <strong>JwtMake</strong>,<strong>JwtValidate</strong>等处理器，实现自定义用户登录、用户身份鉴权。
  </p>
  <p>可以在数据流、JS编写的处理器和数据表格中使用登录时候，设置的会话数据。</p>
</blockquote>

## 账号密码登录

**账号密码登录流程：**

1. 用户在登录页面，填写账号名称、验证码和密码，点击按钮提交到指定 API。

2. API 接收账号名和密码信息，转交指定的处理器，校验密码，签发 JWT 令牌。

**处理器密码校验逻辑：**

1.  调用 **CaptchaValidate** 处理器，校验验证码。

2.  调用数据模型处理器，通过账号名称查询用户数据记录，获得加密存储的密码信息。

3.  调用 **PasswordValidate** 处理器，校验用户填写密码是否正确。

4.  签发 JWT 令牌，设定会话信息。

### 第一步: 用户数据模型

编写 `user.tab.json` 放置在应用 `tables` 目录。

<Detail title="查看源码">

```json
{
  "name": "用户",
  "table": { "name": "user", "comment": "用户表" },
  "columns": [
    { "label": "ID", "name": "id", "type": "ID", "comment": "ID" },
    {
      "label": "供应商",
      "name": "supplier_id",
      "type": "bigInteger",
      "index": true,
      "comment": "所属供应商ID"
    },
    {
      "label": "邮箱",
      "name": "email",
      "type": "string",
      "index": true,
      "comment": "用户邮箱地址",
      "validations": [
        {
          "method": "typeof",
          "args": ["string"],
          "message": "{{input}}类型错误, {{label}}应该为字符串"
        },
        {
          "method": "email",
          "args": [],
          "message": "{{input}}不是邮箱地址"
        }
      ]
    },
    {
      "label": "登录密码",
      "name": "password",
      "type": "string",
      "crypt": "PASSWORD",
      "index": true,
      "nullable": true,
      "validations": [
        {
          "method": "typeof",
          "args": ["string"],
          "message": "{{input}}类型错误, {{label}}应该为字符串"
        },
        {
          "method": "minLength",
          "args": [8],
          "message": "{{label}}不能少于8位。"
        }
      ]
    },
    {
      "label": "姓名",
      "name": "name",
      "type": "string",
      "index": true,
      "comment": "用户姓名"
    }
  ],
  "values": [
    {
      "id": 1,
      "supplier_id": 1,
      "name": "张无忌",
      "email": "zhang@yaoapps.com",
      "password": "5MCIXQYrR"
    },
    {
      "id": 2,
      "supplier_id": 1,
      "name": "李光富",
      "email": "li@yaoapps.com",
      "password": "VHP79MBKf"
    },
    {
      "id": 3,
      "supplier_id": 2,
      "name": "李木婷",
      "email": "mu@yaoapps.com",
      "password": "Ert6a1Ub8"
    },
    {
      "id": 4,
      "supplier_id": 2,
      "name": "赵长青",
      "email": "zhao@yaoapps.com",
      "password": "7CDcn4pcU"
    }
  ]
}
```

</Detail>

**创建数据表 & 添加默认用户:**

```bash
yao migrate -n user
```

### 第二步: 登录处理器

编写 `password.flow.json` 和 `token.flow.json` 放置在应用 `flows/login/` 目录。 分别实现密码校验逻辑和签发 JWT 令牌逻辑。

<Detail title="查看源码">

password.flow.json:

```json
{
  "label": "用户账号密码登录",
  "version": "1.0.0",
  "description": "用户账号密码登录",
  "nodes": [
    {
      "name": "验证码校验",
      "process": "xiang.helper.CaptchaValidate",
      "args": ["{{$captcha.id}}", "{{$captcha.code}}"]
    },
    {
      "name": "用户",
      "process": "models.user.Get",
      "args": [
        {
          "select": ["id", "email", "password", "supplier_id", "name"],
          "wheres": [{ "column": "email", "value": "?:$mobile" }],
          "limit": 1
        }
      ]
    },
    {
      "name": "密码校验",
      "process": "xiang.helper.PasswordValidate",
      "args": ["{{$password}}", "{{$res.用户.0.password}}"]
    },
    {
      "name": "签发JWT",
      "process": "flows.login.Token",
      "args": ["{{$res.用户.0}}"]
    }
  ],
  "output": "{{$res.签发JWT}}"
}
```

token.flow.json:

```json
{
  "label": "Token",
  "version": "1.0.0",
  "description": "签发JWT & 设置会话数据",
  "nodes": [
    {
      "name": "SID",
      "process": "session.start"
    },
    {
      "name": "JWT",
      "process": "xiang.helper.JWTMake",
      "args": [
        "{{$in.0.id}}",
        {},
        {
          "timeout": 3600,
          "sid": "{{$res.SID}}"
        }
      ]
    },
    {
      "name": "设置会话数据",
      "process": "session.set",
      "args": ["user", "{{$in.0}}", 3600]
    },
    {
      "name": "设置会话用户ID",
      "process": "session.set",
      "args": ["user_id", "{{$in.0.id}}", 3600]
    }
  ],
  "output": {
    "sid": "{{$res.SID}}",
    "user": "{{$res.用户.0}}",
    "token": "{{$res.JWT.token}}",
    "expires_at": "{{$res.JWT.expires_at}}",
    "menus": [{ "注释": "根据应用逻辑，读取用户对应的菜单列表" }]
  }
}
```

</Detail>

<Notice type="success">
  技巧：将<strong>密码校验</strong>和<strong>签发令牌</strong>
  拆分为两个处理器，签发令牌处理器可以在OAuth第三方登录、短信验证码登录等场景下复用。
</Notice>

**运行处理器调试:**

<Notice type="success">
  技巧: 为便于调试，可在登录逻辑调试成功后，添加验证码校验节点。
</Notice>

<Notice type="warning">
  注意：由于一些历史原因, yao 内建的登录界面登录提交信息中，用户字段名称固定为
  <strong>mobile</strong>, 在后续的版本中将允许在应用描述文件中定义。
</Notice>

```bash
yao run flows.login.password '::{"mobile":"zhang@yaoapps.com", "password": "5MCIXQYrR"}'
```

### 第三步: 登录 API

编写接口描述文件 `user.http.json`，添加 `/captcha` 和 `/login/password` 两个接口，分别用于验证码图片和用户名密码登录接口，放置在应用的 `api` 目录中。

描述文件内容:

<Detail title="查看源码">

```json
{
  "name": "用户",
  "version": "1.0.0",
  "description": "用户接口",
  "guard": "bearer-jwt",
  "group": "user",
  "paths": [
    {
      "path": "/captcha",
      "method": "GET",
      "guard": "-",
      "process": "xiang.helper.Captcha",
      "in": [":query"],
      "out": {
        "status": 200,
        "type": "application/json"
      }
    },
    {
      "path": "/login/password",
      "method": "POST",
      "guard": "-",
      "process": "flows.login.password",
      "query": [":payload"],
      "out": {
        "status": 200,
        "type": "application/json"
      }
    }
  ]
}
```

</Detail>

**接口调试:**

启动服务:

```bash
yao start
```

读取验证码接口:

```bash
curl http://127.0.0.1:5099/xiang/api/user/captcha
```

<Notice type="success">
  技巧：设置环境变量开启 debug mode , 发起请求后，可以在服务日志中查看验证码 id
  和 code, 用于调试。
</Notice>

登录接口:

```bash
curl -X POST http://127.0.0.1:5099/xiang/api/user/login/password \
    -H 'Content-Type: application/json' \
    -d '{"mobile":"zhang@yaoapps.com", "password": "5MCIXQYrR", "captcha":{"id":1024, "code":"xv98"}}'
```

### 第四步: 应用描述

编辑 `app.json` 设置用户登录 API。登录界面路由为 `/xiang/login/user/:is` , `is` 为自定义变量，随登录表单一并提交给登录接口，用来识别用户来源，一般用于多租户系统。

```json
{
  "name": "象传应用",
  "short": "象传",
  "description": "象传应用后台",
  "option": {
    "nav_user": "xiang.user",
    "nav_menu": "menu",
    "hide_user": true,
    "hide_menu": true,
    "login": {
      "password": {
        "captcha": "/api/xiang/user/captcha",
        "login": "/api/user/login/password"
      }
    }
  }
}
```

## 使用会话数据

用户成功登录设定的会话数据，可以在数据流, JS 脚本和数据表格中使用。

### 在数据流中使用

编写 `inspect.flow.json` 放置在应用 `flows/user/` 目录。

```json
{
  "label": "当前用户信息",
  "version": "1.0.0",
  "description": "当前用户信息",
  "nodes": [
    {
      "name": "会话",
      "process": "session.Get",
      "args": ["user"]
    }
  ],
  "output": "{{$res.会话}}"
}
```

**运行调试:**

启动服务，开启调试模式:

```bash
yao start --debug
```

新建一个命令控制台:

<Notice type="warning">
  注意：启用 run@ 命令，需开启<strong>调试模式</strong>或将环境变量
  <strong>XIANG_REMOTE_RUN</strong>
  设置为IP白名单。 例如： XIANG_REMOTE_RUN=127.0.0.1
</Notice>

```bash
yao run@127.0.0.1:5099 login
yao run@127.0.0.1:5099 flows.user.inspect
```

### 在 JS 脚本中使用

编写 `user.js` 放置在应用 `scripts` 目录。

```javascript
function Inspect() {
  return Process("session.Get", "user");
}
```

```bash
yao run@127.0.0.1:5099 login
yao run@127.0.0.1:5099 scripts.user.Inspect
```

### 在数据表格中使用

可直接在数据表格 `apis.*.default` 中引用会话变量， 修改 [表格数据预处理](e.表格数据预处理.mdx) 章节的用户管理表格，限定仅查看当前用户所属供应商的数据。

<Detail title="查看源码">

```json
{
  "name": "用户",
  "version": "1.0.0",
  "decription": "用户管理表格",
  "bind": {
    "model": "user",
    "withs": { "supplier": { "select": ["id", "name"] } }
  },
  "hooks": {
    "before:search": "scripts.user.SearchFilter"
  },
  "apis": {
    "search": {
      "default": [
        {
          "withs": { "supplier": { "select": ["id", "name"] } },
          "wheres": [
            { "column": "supplier_id", "value": "{{$user.supplier_id}}" }
          ],
          "orders": [{ "column": "updated_at", "options": "desc" }]
        },
        1,
        10
      ]
    }
  },
  "columns": {
    "ID": {
      "label": "ID",
      "view": { "type": "label", "props": { "value": ":id" } }
    },
    "所属供应商": {
      "label": "供应商",
      "view": { "type": "label", "props": { "value": ":supplier.name" } },
      "edit": {
        "type": "select",
        "props": {
          "value": ":supplier_id",
          "allowClear": true,
          "remote": {
            "api": "/api/xiang/table/supplier/select",
            "query": { "select": ["id", "name"] }
          }
        }
      }
    }
  },
  "filters": {
    "关键词": {
      "label": "关键词",
      "bind": "where.name.match",
      "input": { "type": "input", "props": { "placeholder": "请输入关键词" } }
    },
    "所属供应商": {
      "label": "供应商",
      "bind": "where.supplier.name.match",
      "input": { "type": "input", "props": { "placeholder": "请输入供应商" } }
    }
  },
  "list": {
    "primary": "id",
    "layout": {
      "columns": [
        { "name": "ID", "width": 80 },
        { "name": "名称", "width": 100 },
        { "name": "所属供应商", "width": 200 }
      ],
      "filters": [{ "name": "关键词" }, { "name": "所属供应商" }]
    },
    "actions": { "pagination": { "props": { "showTotal": true } } },
    "option": {}
  },
  "edit": {
    "primary": "id",
    "layout": {
      "fieldset": [
        {
          "columns": [
            { "name": "名称", "width": 12 },
            { "name": "所属供应商", "width": 12 }
          ]
        }
      ]
    },
    "actions": { "cancel": {}, "save": {}, "delete": {} }
  }
}
```

</Detail>

<Div style={{ display: "flex", justifyContent: "space-between" }}>
  <Link
    type="prev"
    title="表格自定义处理器"
    link="c.高级特性/f.表格自定义处理器"
  ></Link>
  <Link
    type="next"
    title="复用JSON描述"
    link="c.高级特性/h.复用JSON描述"
  ></Link>
</Div>
