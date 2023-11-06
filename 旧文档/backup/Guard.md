# Guard

<Detail title="查看源码">

```json
{
  "name": "User API",
  "version": "1.0.0",
  "description": "User API",
  "group": "user",
  "guard": "bearer-jwt",
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
      "path": "/login",
      "method": "POST",
      "guard": "-",
      "process": "flows.login.password",
      "in": [":payload"],
      "out": {
        "status": 200,
        "type": "application/json"
      }
    },
    {
      "path": "/inspect",
      "method": "GET",
      "process": "session.Get",
      "in": ["user"],
      "out": {
        "status": 200,
        "type": "application/json"
      }
    }
  ]
}
```

</Detail>

查看 [代码示例](https://github.com/YaoApp/demo-crm/blob/master/apis/user.http.json)

在 API 接口中增加 guard，用来过滤一些不满足条件的请求，类似于 PHP 框架的中间件，使请求进来先进入 guard 验证数据逻辑，或者权限

## 处理器清单

系统自带 guard 处理器

| 处理器     | 说明     | 文档 |
| ---------- | -------- | ---- |
| bearer-jwt | 登录验证 | -    |

## 命名规范

guard 定义在 api 中的`guard`属性中 ，每一个 api 可以单独定义，也可以定义在整个路由组中，使用“,"分隔多个 guard，请求时会逐一进入判断，取消 guard 的话只要使用”-“，系统就不会判断

### 在`apis`目录中定义

| 字段        | 类型                 | 说明                                                                         | 必填项 |
| ----------- | -------------------- | ---------------------------------------------------------------------------- | ------ |
| name        | String               | API 呈现名称，用于开发平台呈现                                               | 是     |
| version     | String               | 版本号，用于依赖关系校验和开发平台呈现                                       | 是     |
| description | String               | API 介绍，用于开发平台呈现                                                   | 否     |
| group       | String               | API 分组名称，访问时作为 API 路由前缀目录。 `/api/<group>/<path>`            | 是     |
| guard       | String               | API 全局中间件，多个用 "," 分割。除特别声明，组内所有 API 都将使用全局中间件 | 否     |
| paths       | Array\<Object Path\> | API 列表。具体查看 `Object Path` 数据结构                                    | 是     |

### 定义在路由组中的代码示例

```json
{
  "name": "User API",
  "version": "1.0.0",
  "description": "User API",
  "group": "user",
  "guard": "bearer-jwt",
  "paths": [
    {
      "path": "/info",
      "method": "GET",
      "guard": "-",
      "process": "xiang.user.info",
      "in": [":query"],
      "out": {
        "status": 200,
        "type": "application/json"
      }
    }
  ]
}
```

### 定义在单独接口中的 guard

```json
{
  "name": "User API",
  "version": "1.0.0",
  "description": "User API",
  "group": "user",
  "paths": [
    {
      "path": "/info",
      "method": "GET",
      "guard": "bearer-jwt",
      "process": "xiang.user.info",
      "in": [":query"],
      "out": {
        "status": 200,
        "type": "application/json"
      }
    }
  ]
}
```

### 定义在 table 数据表格中的 guard

```json
{
  "apis": {
    "search": {
      "process": "models.service.Paginate",
      "guard": "bearer-jwt",
      "default": [{}, null, 15]
    },
    "find": {
      "guard": "bearer-jwt",
      "process": "models.service.Find"
    }
  }
}
```

### 自定义 guard

#### 编写`apis/test.http.json`

```json
{
  "name": "测试guard",
  "version": "1.0.0",
  "description": "测试guard",
  "guard": "scripts.test.Guard",
  "group": "test",
  "paths": [
    {
      "path": "/info",
      "method": "GET",
      "process": "scripts.test.Info",
      "in": [],
      "out": {
        "status": 200,
        "type": "application/json"
      }
    }
  ]
}
```

#### 新建`scripts/test.js`

```javascript
function Info(path, params, query, payload, headers) {
  if (!payload.id) {
    throw new Exception("id不能为空", 400);
  }
  console.log([path, params, query, payload, headers]);

  return;
}
```

#### 参数说明

| 字段    | 说明              | 必填项 |
| ------- | ----------------- | ------ |
| path    | 获取请求路径 path | 是     |
| params  | 获取请求的参数    | 是     |
| query   | 获取 query 参数   | 是     |
| payload | 获取 post 的参数  | 是     |
| headers | 获取 headers 头   | 是     |

<Div style={{ display: "flex", justifyContent: "space-between" }}>
  <Link type="prev" title="API" link="手册/Widgets/API"></Link>
  <Link type="next" title="Table" link="手册/Widgets/Flow"></Link>
</Div>
