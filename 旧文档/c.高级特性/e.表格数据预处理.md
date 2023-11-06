# 表格数据预处理

<blockquote>
  <p>
    通过修改<strong>默认值描述</strong>，指定表格预制API查询条件；
  </p>
  <p>
    通过设置
    <strong>Hooks</strong>处理器，实现对表格查询的输入和输出数据预处理。
  </p>
</blockquote>

## 数据表格 RESTFul API

数据表格提供了一组 RESTFul API, 数据管理界面调用这些 API，实现数据表单增删改查等功能交互。

| API          | 请求方式 | 路由                                       | 说明                                         |
| ------------ | -------- | ------------------------------------------ | -------------------------------------------- |
| search       | `GET`    | `/api/xiang/table/<表格名称>/search`       | 按条件查询, 分页。                           |
| select       | `GET`    | `/api/xiang/table/<表格名称>/select`       | 列表查询，返回 select 组件约定的数据格式。   |
| find         | `GET`    | `/api/xiang/table/<表格名称>/find/:id`     | 按主键查询单条记录。                         |
| save         | `POST`   | `/api/xiang/table/<表格名称>/save`         | 保存单条记录，存在主键更新，不存在主键创建。 |
| delete       | `POST`   | `/api/xiang/table/<表格名称>/delete/:id`   | 按主键删除单条记录。                         |
| insert       | `POST`   | `/api/xiang/table/<表格名称>/insert`       | 批量新增记录。                               |
| delete-where | `POST`   | `/api/xiang/table/<表格名称>/delete/where` | 批量删除符合条件的记录。                     |
| delete-in    | `POST`   | `/api/xiang/table/<表格名称>/delete/in`    | 批量删除指定一组主键的的数据记录。           |
| update-where | `POST`   | `/api/xiang/table/<表格名称>/update/where` | 批量更新符合条件的记录。                     |
| update-in    | `POST`   | `/api/xiang/table/<表格名称>/update/in`    | 批量更新指定一组主键的的数据记录。           |
| quicksave    | `POST`   | `/api/xiang/table/<表格名称>/quicksave`    | 保存多条记录，存在主键更新，不存在主键创建。 |
| setting      | `GET`    | `/api/xiang/table/<表格名称>/setting`      | 读取数据表格配置信息, 用于前端界面渲染       |

## 设置默认查询条件

在编写表格 JSON 描述时，通过在 `bind` 或 `apis` 中声明关联查询等查询参数， 指定各接口预制查询条件。

编写供应商 `supplier` 和用户 `user` 两个数据模型，一个用户对应一家供应商，一家供应商有多个用户。在查询用户时，同时返回所属供应商的信息，查询供应商时，同时返回该供应商的用户列表。

供应商模型 `supplier`:

<Detail title="查看源码">

| 字段 | 标签 |
| ---- | ---- |
| id   | ID   |
| name | 名称 |

数据示例：

| ID  | 名称           |
| --- | -------------- |
| 1   | 象传智慧       |
| 2   | Yao App Engine |

`supplier.mod.json`

```json
{
  "name": "供应商",
  "table": { "name": "supplier", "comment": "供应商表" },
  "columns": [
    { "label": "ID", "name": "id", "type": "ID", "comment": "ID" },
    {
      "label": "名称",
      "name": "name",
      "type": "string",
      "index": true,
      "comment": "供应商名称"
    }
  ],
  "relations": [
    {
      "name": "users",
      "type": "hasMany",
      "model": "user",
      "key": "supplier_id",
      "foreign": "id",
      "query": { "select": ["id", "name"] }
    }
  ],
  "values": [
    { "id": 1, "name": "象传智慧" },
    { "id": 2, "name": "Yao App Engine" }
  ]
}
```

</Detail>

用户模型 `user` :

<Detail title="查看源码">

| 字段        | 标签          |
| ----------- | ------------- |
| ID          | id            |
| supplier_id | 所属供应商 ID |
| name        | 姓名          |

数据示例：

| ID  | 供应商 | 名称   |
| --- | ------ | ------ |
| 1   | 1      | 张无忌 |
| 2   | 1      | 李光富 |
| 3   | 2      | 李木婷 |
| 4   | 2      | 赵长青 |

`user.mod.json`

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
      "comment": "供应商ID"
    },
    {
      "label": "姓名",
      "name": "name",
      "type": "string",
      "index": true,
      "comment": "用户姓名"
    }
  ],
  "relations": [
    {
      "name": "supplier",
      "type": "hasOne",
      "model": "supplier",
      "key": "id",
      "foreign": "supplier_id",
      "query": { "select": ["id", "name"] }
    }
  ],
  "values": [
    { "id": 1, "supplier_id": 1, "name": "张无忌" },
    { "id": 2, "supplier_id": 1, "name": "李光富" },
    { "id": 3, "supplier_id": 2, "name": "李木婷" },
    { "id": 4, "supplier_id": 2, "name": "赵长青" }
  ]
}
```

</Detail>

### bind 指定关联数据模型

查询用户数据时，同时在列表页展示供应商信息，在编辑用户时，通过选择框选择供应商。

编写 `user.tab.json` 和 `supplier.tab.json` 放置在应用 `tables` 目录，使用 `bind.withs` 声明关联数据模型。

<Detail title="查看源码">

user.tab.json:

```json
{
  "name": "用户",
  "version": "1.0.0",
  "decription": "用户管理表格",
  "bind": {
    "model": "user",
    "withs": { "supplier": { "select": ["id", "name"] } }
  },
  "apis": {},
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

supplier.tab.json:

```json
{
  "name": "供应商",
  "version": "1.0.0",
  "decription": "供应商管理表格",
  "bind": { "model": "supplier" },
  "apis": {},
  "columns": {
    "ID": {
      "label": "ID",
      "view": { "type": "label", "props": { "value": ":id" } }
    }
  },
  "filters": {
    "关键词": {
      "label": "关键词",
      "bind": "where.name.match",
      "input": { "type": "input", "props": { "placeholder": "请输入关键词" } }
    }
  },
  "list": {
    "primary": "id",
    "layout": {
      "columns": [
        { "name": "ID", "width": 80 },
        { "name": "名称", "width": 100 }
      ],
      "filters": [{ "name": "关键词" }]
    },
    "actions": { "pagination": { "props": { "showTotal": true } } },
    "option": {}
  },
  "edit": {
    "primary": "id",
    "layout": {
      "fieldset": [
        {
          "columns": [{ "name": "名称", "width": 24 }]
        }
      ]
    },
    "actions": { "cancel": {}, "save": {}, "delete": {} }
  }
}
```

</Detail>

**使用表格处理器调试:**

```bash
yao run xiang.table.Search user '::{"wheres":[{"rel":"supplier","column":"name", "value":"App", "op":"match"}]}' 1 2
yao run xiang.table.Find user 1 '::{}'
```

**使用管理界面调试:**

1. `yao start` 启动服务
2. 打开浏览器访问 `http://127.0.0.1:5099/xiang/table/user`
3. 打开浏览器控制台，查看 API 接口返回值。

<Notice type="warning">
  注意：由于该项目诞生之初主要是为了提高团队内部生产力，在约定俗成的写法描述下，并没有做细粒度的抛错处理，所以开发者可能会在编写
  JSON 调试界面的过程当中遇到界面为空的情况。处置方式请查阅组件文档。
</Notice>

### Search API 指定查询条件

用户列表页：默认显示 10 条数据，仅列出供应商 ID = 1 的用户，按更新时间倒叙排序。使用 `apis.search.default` 声明默认查询条件。

`apis.search.default` 数据结构为:

| 参数表                 | 类型              | 说明             |
| ---------------------- | ----------------- | ---------------- |
| apis.search.default[0] | Object QueryParam | 默认查询条件     |
| apis.search.default[1] | Integer           | 当前页码         |
| apis.search.default[2] | Integer           | 每页显示记录数量 |

修改 `user.tab.json` , 添加默认查询条件：

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
  "apis": {
    "search": {
      "default": [
        {
          "withs": { "supplier": { "select": ["id", "name"] } },
          "wheres": [{ "column": "supplier_id", "value": 1 }],
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

<Notice type="success">
  提示：apis.*.default 支持使用 &#123;&#123;xxx&#125;&#125;
  引用会话数据，根据会话数据限定查询范围。详情参考
  <a href="#">使用会话数据实现用户登录</a>
</Notice>

**使用表格处理器调试:**

```bash
yao run xiang.table.Search user '::{"wheres":[{"rel":"supplier","column":"name", "value":"App", "op":"match"}]}' 1 2
```

扩展阅读：

<Extend
  title="数据表格手册"
  desc="详细的数据表格使用手册, 了解更多使用方式。"
  link="f.参考手册/g.数据表格"
></Extend>

## 使用 Hooks

可以使用 Hooks 处理表格 API 输入输出数据。Hook 分为 `before` 和 `after` 两类， before hook，在 API 调用前运行，可以用来处理传入参数，after hook，在 API 调用后运行，可用来处理查询结果。

在描述数据表格时，在 `hooks` 字段，声明 **Hook 关联的处理器**，例如：

```json
{
  "name": "用户",
  "version": "1.0.0",
  "decription": "用户",
  "bind": { "model": "user" },
  "hooks": {
    "before:find": "flows.hooks.before_find",
    "after:find": "flows.hooks.after_find",
    "before:search": "flows.hooks.before_search",
    "after:search": "flows.hooks.after_search",
    "before:save": "flows.hooks.before_save",
    "after:save": "flows.hooks.after_save"
  },
  "apis": {},
  "columns": {}
}
```

### before hook

使用 Before Hook 锁定搜索条件，过滤掉 `search` API 越界输入。

修改 `user.tab.json` 将 `before:search` hook 指定为 `scripts.user.SearchFilter` 处理器。

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
          "wheres": [{ "column": "supplier_id", "value": 1 }],
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

使用 JS 编写处理器， `user.js`，并放置在应用的 `scripts` 目录中。

`before:search` 关联处理器的输入为 `search` API 接口的输入。

| 参数    | 说明                |
| ------- | ------------------- |
| args[0] | 查询条件 QueryParam |
| args[1] | 当前页码            |
| args[2] | 每页显示记录数据量  |

<Detail title="查看源码">

```javascript
function SearchFilter(param, page, pagesize) {
  var wheres = param.wheres || [];
  var newParam = {
    withs: { supplier: { select: ["id", "name"] } },
    wheres: [],
    orders: [{ column: "updated_at", options: "desc" }],
  };

  // 过滤查询条件
  for (var i in wheres) {
    var where = wheres[i] || {};
    if (where.column != supplier_id) {
      continue;
    }
    newParam.wheres.push({ column: "supplier_id", value: where.value || 1 });
  }

  return [newParam, page, pagesize];
}
```

</Detail>

**使用表格处理器调试:**

```bash
yao run xiang.table.Search user '::{}' 1 2
```

### after hook

使用 After Hook 处理表单提交数据，保存历史数据。

修改 `supplier.tab.json` 将 `after:save` hook 指定为 `flows.supplier.savelog` 处理器。

<Detail title="查看源码">

```json
{
  "name": "供应商",
  "version": "1.0.0",
  "decription": "供应商管理表格",
  "bind": { "model": "supplier" },
  "hooks": {
    "after:save": "flows.supplier.savelog"
  },
  "apis": {},
  "columns": {
    "ID": {
      "label": "ID",
      "view": { "type": "label", "props": { "value": ":id" } }
    }
  },
  "filters": {
    "关键词": {
      "label": "关键词",
      "bind": "where.name.match",
      "input": { "type": "input", "props": { "placeholder": "请输入关键词" } }
    }
  },
  "list": {
    "primary": "id",
    "layout": {
      "columns": [
        { "name": "ID", "width": 80 },
        { "name": "名称", "width": 100 }
      ],
      "filters": [{ "name": "关键词" }]
    },
    "actions": { "pagination": { "props": { "showTotal": true } } },
    "option": {}
  },
  "edit": {
    "primary": "id",
    "layout": {
      "fieldset": [
        {
          "columns": [{ "name": "名称", "width": 24 }]
        }
      ]
    },
    "actions": { "cancel": {}, "save": {}, "delete": {} }
  }
}
```

</Detail>

创建 `models.supplier.history` 数据模型，用于保存历史数据。

编写数据模型文件 `history.mod.json`，并放置在应用的 `models/supplier/` 目录中。

<Detail title="查看源码">

```json
{
  "name": "供应商历史记录",
  "table": { "name": "supplier", "comment": "供应商历史记录数据" },
  "columns": [
    { "label": "ID", "name": "id", "type": "ID", "comment": "ID" },
    {
      "label": "供应商ID",
      "name": "supplier_id",
      "type": "bigInteger",
      "index": true,
      "comment": "供应商ID"
    },
    {
      "label": "数据",
      "name": "data",
      "type": "json",
      "comment": "表单数据"
    }
  ],
  "option": { "timestamps": true }
}
```

</Detail>

创建 `flows.supplier.savelog` 数据流，实现历史数据保存逻辑。

编写数据流描述文件 `savelog.flow.json`，并放置在应用的 `flows/supplier/` 目录中。

`after:save` 关联处理器的输入为 `save` API 接口返回值和 POST 提交数据 `payload`。

| 参数    | 说明                                  |
| ------- | ------------------------------------- |
| args[0] | save API 绑定的处理器返回值 (数据 ID) |
| args[1] | save API payload                      |

<Detail title="查看源码">

```json
{
  "label": "保存历史数据记录",
  "version": "1.0.0",
  "description": "保存历史数据记录",
  "nodes": [
    {
      "name": "保存数据",
      "process": "models.supplier.history.Save",
      "args": [
        {
          "supplier_id": "{{$in.0}}",
          "data": "{{$in.1}}"
        }
      ]
    }
  ],
  "output": ["{{$in.0}}"]
}
```

</Detail>

**使用表格处理器调试:**

```bash
yao run xiang.table.Save supplier '::{"name":"新供应商"}'
```

### Hooks 一览表

| Hook          | 说明                     | 输入                          | 输出规范                                      |
| ------------- | ------------------------ | ----------------------------- | --------------------------------------------- |
| before:find   | 在 Find 处理器之前调用   | Find 接口传入数据             | 输出结果作为 Find 关联处理器输入参数          |
| after:find    | 在 Find 处理器之后调用   | Find 接口关联处理器执行结果   | 自定义(输出结果作为 Find 处理器的最终输出)    |
| before:search | 在 Search 处理器之前调用 | Search 接口传入数据           | 输出结果作为 Search 关联处理器输入参数        |
| after:search  | 在 Search 处理器之后调用 | Search 接口关联处理器执行结果 | 自定义 (输出结果作为 Search 处理器的最终输出) |
| before:save   | 在 Save 处理器之前调用   | Save 接口传入数据             | 输出结果作为 Save 关联处理器输入参数          |
| after:save    | 在 Save 处理器之后调用   | Save 接口关联处理器执行结果   | 自定义 (输出结果作为 Save 接口的最终输出)     |

<Div style={{ display: "flex", justifyContent: "space-between" }}>
  <Link
    type="prev"
    title="使用JS编写处理器"
    link="c.高级特性/d.使用JS编写处理器"
  ></Link>
  <Link
    type="next"
    title="表格自定义处理器"
    link="c.高级特性/f.表格自定义处理器"
  ></Link>
</Div>
