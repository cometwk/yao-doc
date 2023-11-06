# Flows 处理器

<Detail title="查看源码">

```json
{
  "label": "Password Login",
  "version": "1.0.0",
  "description": "Password Login",
  "nodes": [
    {
      "name": "Validate Captcha",
      "process": "xiang.helper.CaptchaValidate",
      "args": ["{{$captcha.id}}", "{{$captcha.code}}"]
    },
    {
      "name": "User",
      "process": "models.user.Get",
      "args": [
        {
          "select": ["id", "mobile", "password"],
          "wheres": [{ "column": "mobile", "value": "?:$mobile" }],
          "limit": 1
        }
      ]
    },
    {
      "name": "Validate Passwor",
      "process": "xiang.helper.PasswordValidate",
      "args": ["{{$password}}", "{{$res.User.0.password}}"]
    },
    {
      "name": "Response",
      "process": "flows.login.Token",
      "args": ["{{$res.User.0.id}}"]
    }
  ],
  "output": "{{$res.Response}}"
}
```

</Detail>

查看 [代码示例](https://github.com/YaoApp/demo-crm/blob/master/flows/login/password.flow.json)

数据流(`Flow`)用来编排数据查询逻辑，支持使用 JavaScript 脚本处理各查询节点结果，可以作为处理 (`process`) 来使用，引用方式为 `flows.<数据流名称>` 。

## 命名规范

数据流描述文件是以 **小写英文字母** + `.flow.json` 扩展名命名的 JSON 文本文件, `<name>.flow.json`;
结果处理脚本文件是以 `数据流名称` + `.` + `脚本名称` + `.js` 扩展名，命名的 JavaScript 脚本文件 `<name>.<script>.js` 。

| 文件夹 (相对数据流根目录) | 文件名         | 数据流名称           | 脚本名称 | Process (在 API /Flow 中引用) |
| ------------------------- | -------------- | -------------------- | -------- | ----------------------------- |
| /                         | name.flow.json | `name`               |          | `flows.name`                  |
| /                         | name.count.js  | `name`               | `count`  | -                             |
| /group                    | name.flow.json | `group.name`         |          | `flows.group.name`            |
| /group                    | name.count.js  | `gorup.name`         | `count`  | -                             |
| /group1/group2            | name.flow.json | `group1.group2.name` |          | `flows.group1.group2.name`    |
| /group1/group2            | name.count.js  | `group1.group2.name` | `count`  | -                             |

## 文档结构

数据流编排文档，由基础信息、查询节点和输出结果构成。

```json
{
  "label": "最新信息",
  "version": "1.0.0",
  "description": "最新信息",
  "nodes": [],
  "output": {}
}
```

| 字段        | 类型                | 说明                                   | 必填项 |
| ----------- | ------------------- | -------------------------------------- | ------ |
| label       | String              | 数据流呈现名称，用于开发平台呈现       | 是     |
| version     | String              | 版本号，用于依赖关系校验和开发平台呈现 | 是     |
| description | String              | 数据流介绍，用于开发平台呈现           | 否     |
| nodes       | Array<Object Node\> | 查询节点                               | 是     |
| output      | Object              | 输出结果定义                           | 是     |

## 查询节点 `nodes`

```json
{
  "nodes": [
    {
      "name": "manus",
      "process": "models.manu.get",
      "args": [
        {
          "select": ["id", "name", "short_name"],
          "limit": 20,
          "orders": [{ "column": "created_at", "option": "desc" }],
          "wheres": [
            { "column": "status", "value": "enabled" },
            { "column": "name", "value": "{{$in.0}}", "op": "like" }
          ]
        }
      ],
      "script": "rank",
      "outs": ["{{$out.manus}}", "{{$out.manu_ids}}"]
    }
  ]
}
```

一个数据流编排(`Flow`)可以有多个查询节点, 每个查询节点，可以调用一个处理器(`process`), 可以指定结果处理脚本和返回值，在查询节点用可以引用上下文信息。
`Object Node` 数据结构

| 字段    | 类型           | 说明                                                                                      | 必填项 |
| ------- | -------------- | ----------------------------------------------------------------------------------------- | ------ |
| name    | String         | 查询节点名称                                                                              | 是     |
| process | String         | 调用处理器 `process`                                                                      | 是     |
| args    | Array<Any\>    | 处理器参数表.可以引用输入输出或上下文数据                                                 | 是     |
| script  | String         | 结果处理 JS 脚本                                                                          | 否     |
| outs    | Array<String\> | 查询节点结果输出.使用 `{{$out}}` 引用处理器返回结果。如不设置，返回值等于处理器返回结果。 | 否     |
| next    | Object Next    | 当查询结果符合设定条件时跳转至指定查询节点(**尚未实现**)                                  | 否     |

## 输出结果 `output`

```json
{
  "output": {
    "foo": "{{$in}}",
    "bar": {
      "node1": "{{$res.node1.0}}",
      "node2": "{{$res.node2.0}}",
      "node3": "{{$res.node3}}"
    },
    "data": "{{$res}}",
    "ping": "pong"
  }
}
```

可以根据业务需要，自由定义数据流(`Flow`)的输出结果。 可以使用 `{{$in}}` 引用数据流(`Flow`)调用时传入的参数、使用 `{{$res}}` 引用各个查询节点返回值。

## 3 上下文数据引用

数据流(`Flow`)可以在全局引用传参(`{{$in}}`)和 各查询节点返回值 `{{$res}}`。查询节点内 `outs` 数组中，可以引用处理器 (`process`) 的返回值 `{{out}}`。

```json
{
  "label": "最新信息",
  "version": "1.0.0",
  "description": "最新信息",
  "nodes": [
    {
      "name": "manus",
      "process": "models.manu.get",
      "args": [
        {
          "select": ["id", "name", "short_name"],
          "limit": 20,
          "orders": [{ "column": "created_at", "option": "desc" }],
          "wheres": [
            { "column": "status", "value": "enabled" },
            { "column": "name", "value": "{{$in.0}}", "op": "like" }
          ]
        }
      ],
      "script": "rank",
      "outs": ["{{$out.manus}}", "{{$out.manu_ids}}"]
    },
    {
      "name": "github",
      "process": "plugins.user.github",
      "args": [
        "{{$res.users.0}}",
        "{{$res.manus}}",
        "{{$in.0}}",
        "{{$in.1}}",
        "{{$in.2}}",
        "{{hello(:$res.users, 'id', 0.618, 10)}}",
        "foo",
        1
      ]
    }
  ],
  "output": {
    "params": "{{$in}}",
    "data": {
      "manus": "{{$res.manus.0}}",
      "github": "{{$res.github}}"
    }
  }
}
```

### 变量

| 变量       | 类型               | 说明                                                                                                                             | 使用范围                                   | 示例                                                          |
| ---------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------- |
| `{{$in}}`  | Array<Any\>        | 数据流调用时传入的参数表, 支持使用数组下标访问指定参数, 例如： `{{$in.0}}` 第 1 个参数, `{{$in.1}}` 第 2 个参数,                 | `nodes[n].args`, `nodes[n].outs`, `output` | `{{$in}}`, `{{$in.0}}`,`{{$in.0.name}}`                       |
| `{{$res}}` | \[key:String\]:Any | 查询节点返回值(`nodes[n].outs`) 映射表, 支持使用查询节点名称访问特定查询节点返回值。例如 `{{$res.node1.0}}` node1 的第一返回值。 | `nodes[n].args`, `nodes[n].outs`, `output` | `{{$res}}`, `{{$res.node1.0.name}}`, `{{$res.node2.manu_id}}` |
| `{{out}}`  | Any                | 查询节点的处理器(`process`)返回值，支持使用 `.` 应用 Object /Array 数值                                                          | `nodes[n].outs`                            | `{{out}}`, `{{out.name}}`, `{{out.0}}`                        |

### Helper 函数

可以在 `nodes[n].args`, `nodes[n].outs`, `output` 中使用 `Helper` 函数。调用方法为 `{{method(args...)}}` 参数表支持使用变量 写法为 `:$res.node1`, 字符串使用单引号 `'`，例如: `{{hello(:$res.users, 'id', 0.618, 10)}}`

Helper 函数表

| 函数    | 参数表                       | 返回值                   | 示例                          |
| ------- | ---------------------------- | ------------------------ | ----------------------------- |
| `pluck` | `row: Array`, `name: String` | `Array` 指定字段数值集合 | `{{pluck(:$res.user, 'id')}}` |

查询节点支持使用 JavaScript 脚本对处理器(`process`)返回值处理，`main()` 函数传入数据流(`Flow`)参数表、当前查询节点 process 返回值和查询节点返回值映射表。返回值可以使用 `$out` 变量引用。

### 参数表

| 参数    | 类型               | 说明                                                |
| ------- | ------------------ | --------------------------------------------------- |
| args[0] | Array<Any\>        | 数据流调用时传入的参数表, 即 `{{$in}}`              |
| args[1] | Any                | 当前查询节点处理器(`process`)返回值， 即 `{{$out}}` |
| args[2] | \[key:String\]:Any | 查询节点返回值(nodes[n].outs) 映射表, 即 `{{$res}}` |

### 返回值

处理脚本成功运行，`{{$out}}` 变量将更新为脚本返回值数值。

## 外部引用

数据流(`Flow`) 可以作为处理，在其他数据流(`Flow`)或服务接口(`API`)中调用。处理器引用方式为 `flows.数据流名称`

### 在其他数据流(Flow)中调用

```json
{
  "nodes": [
    {
      "name": "github",
      "process": "flows.github",
      "args": ["{{$in.1}}", "{{$in.2}}", "foo", 1],
      "script": "count",
      "outs": ["$out.args", "$out.plugin"]
    }
  ]
}
```

### 在服务接口(API)中调用

```json
{
  "path": "/latest/:day",
  "method": "GET",
  "process": "flows.latest",
  "in": ["$param.day"],
  "out": {
    "status": 200,
    "type": "application/json"
  }
}
```

#### 示例一

新建`models/category.mod.json`写入以下代码:

<Detail title="查看源码">

```json
{
  "name": "物料分类",
  "table": {
    "name": "category",
    "comment": "物料分类"
  },
  "columns": [
    {
      "label": "ID",
      "name": "id",
      "type": "ID",
      "comment": "ID",
      "primary": true
    },
    {
      "label": "父级id",
      "name": "parent_id",
      "type": "integer",
      "nullable": true
    },
    {
      "label": "分类名称",
      "name": "name",
      "type": "string",
      "length": 128,
      "index": true
    }
  ],
  "option": {
    "timestamps": true,
    "soft_deletes": true
  },
  "values": [
    {
      "id": 1,
      "parent_id": null,
      "name": "一级分类"
    },
    {
      "id": 2,
      "parent_id": 1,
      "name": "二级分类"
    }
  ]
}
```

</Detail>

执行命令 `yao migrate -n category`在数据库中可以看到生成了对应的数据表和数据

编写`flows/category.flow.json`写入以下代码:

<Detail title="查看源码">

```json
{
  "label": "类目树",
  "version": "1.0.0",
  "description": "类目树",
  "nodes": [
    {
      "name": "类目",
      "engine": "xiang",
      "query": {
        "select": ["id", "name", "name as label", "id as value", "parent_id"],
        "wheres": [{ ":deleted_at": "删除", "=": null }],
        "from": "category",
        "limit": 1000
      }
    },
    {
      "name": "类目树",
      "process": "xiang.helper.ArrayTree",
      "args": ["{{$res.类目}}", { "parent": "parent_id" }]
    }
  ],
  "output": "{{$res.类目树}}"
}
```

</Detail>

执行`yao run flows.category`可以看到控制台有以下输出:

```json
[
  {
    "children": [
      {
        "children": [],
        "id": 2,
        "label": "二级分类",
        "name": "二级分类",
        "parent_id": 1,
        "value": 2
      }
    ],
    "id": 1,
    "label": "一级分类",
    "name": "一级分类",
    "parent_id": null,
    "value": 1
  }
]
```

#### 示例二

<Detail title="查看源码">

```json
{
  "label": "最新信息",
  "version": "1.0.0",
  "description": "最新信息",
  "nodes": [
    {
      "name": "manus",
      "process": "models.manu.get",
      "args": [
        {
          "select": ["id", "name", "short_name"],
          "limit": 20,
          "orders": [{ "column": "created_at", "option": "desc" }],
          "wheres": [
            { "column": "status", "value": "enabled" },
            { "column": "name", "value": "{{$in.0}}", "op": "like" }
          ]
        }
      ],
      "script": "rank",
      "outs": ["{{$out.manus}}", "{{$out.manu_ids}}"]
    },
    {
      "name": "users",
      "process": "models.user.paginate",
      "args": [
        {
          "select": ["id", "name", "extra", "resume"],
          "withs": {
            "manu": { "query": { "select": ["name", "short_name"] } },
            "addresses": {
              "query": { "select": ["province", "city", "location"] }
            }
          },
          "orders": [{ "column": "created_at", "option": "desc" }],
          "wheres": [
            { "column": "status", "value": "enabled" },
            { "column": "manu_id", "value": "{{$res.manus.1}}", "op": "in" }
          ]
        },
        1,
        20
      ],
      "outs": ["{{$out.data}}"]
    },
    {
      "name": "github",
      "process": "plugins.user.github",
      "args": [
        "{{$res.users.0}}",
        "{{$res.manus}}",
        "{{$in.0}}",
        "{{$in.1}}",
        "{{$in.2}}",
        "{{pluck(:$res.users, 'id', 0.618, 10)}}",
        "foo",
        1
      ]
    },
    {
      "name": "count",
      "script": "count"
    }
  ],
  "output": {
    "params": "{{$in}}",
    "data": {
      "manus": "{{$res.manus.0}}",
      "users": "{{$res.users.0}}",
      "count": "{{$res.count}}"
    }
  }
}
```

</Detail>

<Div style={{ display: "flex", justifyContent: "space-between" }}>
  <Link type="prev" title="API" link="手册/Widgets/API"></Link>
  <Link type="next" title="Table" link="手册/Widgets/Table"></Link>
</Div>
