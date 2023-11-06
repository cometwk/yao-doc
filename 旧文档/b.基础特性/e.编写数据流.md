# 编写数据流

<blockquote>
  <p>
    数据流用来编排处理器的调用逻辑，支持使用 JavaScirpt
    对查询节点数据处理，适用于较为复杂的业务逻辑。
  </p>
  <p>
    数据流可以作为处理器使用，命名空间为
    <strong>flows.&lt;处理器名称&gt;</strong>；查询节点可以引用除自身以外的其他数据流。
  </p>
  <p>
    本章节介绍的编排方法也可用于数据看板、分析图表和数据大屏。
  </p>

</blockquote>

## 数据流描述

使用数据流实现添加一组测试数据。

编写数据流描述文件， `fake.flow.json`，`user.flow.json`，`pet.flow.json`，并放置在应用的 `flows` 目录中。

**描述文件内容:**

<Detail title="查看源码">

fake.flow.json:

```json
{
  "label": "添加测试数据",
  "version": "1.0.0",
  "description": "添加测试数据",
  "nodes": [
    { "name": "用户", "process": "flows.user" },
    { "name": "宠物", "process": "flows.pet" }
  ],
  "output": "DONE"
}
```

user.flow.json:

```json
{
  "label": "用户测试数据",
  "version": "1.0.0",
  "description": "用户测试数据初始化",
  "nodes": [
    {
      "name": "清空默认管理员",
      "process": "models.xiang.user.DestroyWhere",
      "args": [{ "wheres": [{ "column": "status", "value": "enabled" }] }]
    },
    {
      "name": "添加新的管理员",
      "process": "models.xiang.user.EachSave",
      "args": [
        [
          {
            "name": "管理员",
            "type": "admin",
            "email": "yao@iqka.com",
            "password": "A123456p+",
            "key": "8304925176",
            "secret": "XMTdNRVigbgUiAPdiJCfaWgWcz2PaQXw",
            "status": "enabled"
          }
        ]
      ]
    }
  ],
  "output": "{{$res.添加新的管理员}}"
}
```

<Notice type="success">
  提示：<strong>xiang.user</strong> 为内建数据模型，数据表名称为
  <strong>xiang_user</strong>, 用于存放系统管理员账号。 <a href="#">查看数据模型API文档</a>
</Notice>

pet.flow.json:

```json
{
  "label": "添加宠物数据",
  "version": "1.0.0",
  "description": "添加宠物数据",
  "nodes": [
    {
      "name": "添加宠物数据",
      "process": "models.pet.Inset",
      "args": [
        ["sn", "name", "type", "desc"],
        [
          ["400001", "球球", "狗", "新成员"],
          ["400002", "旺财", "狗", "新成员"]
        ]
      ]
    }
  ],
  "output": "{{$res.添加宠物数据}}"
}
```

</Detail>

**运行数据流**

```bash
yao run flows.fake
```

## 上下文数据引用

- 可在全局使用 `{{$in}}` 变量访问调用时的传入参数;
- 可在全局使用 `{{$res}}` 变量访问各点返回值；
- 可在节点使用 `{{$out}}` 变量访问处理器返回值； `outs` 用于字段声明当前节点的返回值, 如不声明返回处理器的运行结果。
- `output` 字段用于声明数据流的输出结果, 如不声明返回所有节点的运行结果。

| 变量       | 类型               | 说明                                                                                                                             | 使用范围                                   | 示例                                                          |
| ---------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------- |
| `{{$in}}`  | array<any\>        | 作为处理器被调用时传入的参数表, 支持使用数组下标访问指定参数, 例如： `{{$in.0}}` 第 1 个参数, `{{$in.1}}` 第 2 个参数,           | `nodes[*].args`, `nodes[*].outs`, `output` | `{{$in}}`, `{{$in.0}}`,`{{$in.0.name}}`                       |
| `{{$res}}` | \[key:string\]:any | 查询节点返回值(`nodes[*].outs`) 映射表, 支持使用查询节点名称访问特定查询节点返回值。例如 `{{$res.node1.0}}` node1 的第一返回值。 | `nodes[*].args`, `nodes[*].outs`, `output` | `{{$res}}`, `{{$res.node1.0.name}}`, `{{$res.node2.manu_id}}` |
| `{{$out}}` | any                | 查询节点的处理器(`process`)返回值，支持使用 `.` 访问 Object /Array 数值                                                          | `nodes[*].outs`                            | `{{out}}`, `{{out.name}}`, `{{out.0}}`                        |

<Notice type="success">
  提示：如果参数表只有一个参数，且数据类型为映射表 [key:string]:any
  ，则可以通过键 <strong>&#123;&#123;$key&#125;&#125;</strong> 访问输入数据。
</Notice>

使用数据流查询一组数据。

编写数据流描述文件 `latest.flow.json`，并放置在应用的 `flows` 目录中。

**描述文件内容:**

<Detail title="查看源码">

```json
{
  "label": "查询最新数据",
  "version": "1.0.0",
  "description": "查询系统最新数据",
  "nodes": [
    {
      "name": "宠物",
      "process": "models.pet.Get",
      "args": [
        {
          "select": ["id", "name", "kind", "created_at"],
          "wheres": [{ "column": "kind", "value": "{{$in.0}}" }],
          "orders": [{ "column": "created_at", "option": "desc" }],
          "limit": 10
        }
      ]
    },
    {
      "name": "用户",
      "process": "models.xiang.user.Get",
      "args": [
        {
          "select": ["id", "name", "created_at"],
          "wheres": [{ "column": "status", "value": "enabled" }],
          "orders": [{ "column": "created_at", "option": "desc" }],
          "limit": 1
        }
      ],
      "outs": ["{{$out.0.id}}", "{{$out.0.name}}", "{{$out.0.created_at}}"]
    },
    {
      "name": "打印数据",
      "process": "xiang.sys.Print",
      "args": ["{{$res.宠物}}", "{{$res.用户}}"]
    }
  ],
  "output": {
    "节点返回值": "{{$res}}",
    "参数表": "{{$in}}",
    "宠物列表": "{{$res.宠物}}",
    "用户": "{{$res.用户}}"
  }
}
```

</Detail>

**运行数据流**

```bash
yao run flows.latest 猫
```

扩展阅读:

<Extend
  title="数据流中使用JS"
  desc="了解如何使用JS脚本，对数据流节点数据处理。"
  link="c.高级特性/a.数据流使用JS"
></Extend>

## 推荐阅读

接下来，建议学习以下章节:

<Extend
  title="查询数据"
  desc="了解如何在数据流中使用数据模型处理器和Query DSL 查询数据。"
  link="b.基础特性/f.查询数据"
></Extend>

<Div style={{ display: "flex", justifyContent: "space-between" }}>
  <Link type="prev" title="使用处理器" link="b.基础特性/d.使用处理器"></Link>
  <Link type="next" title="查询数据" link="b.基础特性/f.查询数据"></Link>
</Div>
