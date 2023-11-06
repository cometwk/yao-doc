# 表格自定义处理器

<blockquote>

通过指定 API 处理器，在不绑定数据模型的情况下，在数据表格中使用其他的数据源。

</blockquote>

## 为 API 指定处理器

在描述数据表格时，在 apis 字段，声明 API 关联的处理器，例如：

```json
{
  "name": "表格自定义处理器",
  "version": "1.0.0",
  "decription": "自定义处理器",
  "apis": {
    "search": { "process": "flows.customize.search" },
    "find": { "process": "flows.customize.find" },
    "save": { "process": "flows.customize.save" },
    "delete": { "process": "flows.customize.delete" },
    "insert": { "process": "flows.customize.insert" },
    "delete-where": { "process": "flows.customize.delete_where" },
    "delete-in": { "process": "flows.customize.delete_in" },
    "update-where": { "process": "flows.customize.update_where" },
    "update-in": { "process": "flows.customize.update_id" },
    "quicksave": { "process": "flows.customize.quicksave" },
    "setting": { "process": "flows.customize.setting" }
  },
  "columns": {}
}
```

<Notice type="warning">
  注意：关联的处理器的输入输出需与原API接口保持一致，否则可能导致表格界面异常。
</Notice>

## 示例: 对接 Github 仓库

### 仓库列表查询处理器

编写一个处理器 `search.flow.json` ，从 GitHub API 读取仓库信息数据，放置到应用 `flows/github/` 目录。

<Detail title="查看源码">

```json
{
  "label": "查询代码仓库",
  "version": "1.0.0",
  "description": "查询代码仓库",
  "nodes": [
    {
      "name": "Host",
      "process": "xiang.helper.StrConcat",
      "args": [
        "https://api.github.com/orgs/",
        "{{$in.0.wheres.0.column.value}}",
        "/repos"
      ]
    },
    {
      "name": "结果",
      "process": "xiang.network.Get",
      "args": [
        "{{$res.Host}}",
        {},
        { "Accept": "application/vnd.github.v3+json" }
      ]
    }
  ],
  "output": {
    "data": "{{$res.结果.data}}",
    "total": 1000
  }
}
```

</Detail>

**运行数据流调试:**

```bash
yao run flows.github.search '::{"org":"yaoapp"}'
```

### 仓库详情查询处理器

编写一个处理器 `find.flow.json` ，从 GitHub API 读取指定仓库信息数据，放置到应用 `flows/github/` 目录。

<Detail title="查看源码">

```json
{
  "label": "查询仓库详情",
  "version": "1.0.0",
  "description": "查询仓库详情",
  "nodes": [
    {
      "name": "Host",
      "process": "xiang.helper.StrConcat",
      "args": ["https://api.github.com/repositories/", "{{$in.0}}"]
    },
    {
      "name": "结果",
      "process": "xiang.network.Get",
      "args": [
        "{{$res.Host}}",
        {},
        { "Accept": "application/vnd.github.v3+json" }
      ]
    }
  ],
  "output": "{{$res.结果.data}}"
}
```

</Detail>

**运行数据流调试:**

```bash
yao run flows.github.find 449255223
```

### 描述表格呈现

将数据表格的 API 指定为自定义处理器，同时关闭创建、分页、编辑功能。

编写 `github.tab.json` 放置在应用 `tables` 目录，在 `apis` 中 指定 `search` 和 `find` 处理器。

<Detail title="查看源码">

```json
{
  "name": "GitHub",
  "version": "1.0.0",
  "decription": "GitHub",
  "apis": {
    "search": {
      "process": "flows.customize.search",
      "default": [
        {
          "wheres": [{ "column": "org", "value": "yaoapp" }]
        },
        1,
        100
      ]
    },
    "find": { "process": "flows.customize.find" }
  },
  "columns": {
    "ID": {
      "label": "ID",
      "view": { "type": "label", "props": { "value": ":id" } },
      "edit": {
        "type": "input",
        "props": { "value": ":id", "hidden": true }
      }
    },
    "名称": {
      "label": "名称",
      "view": { "type": "label", "props": { "value": ":full_name" } },
      "edit": {
        "type": "input",
        "props": { "value": ":full_name", "hidden": true }
      }
    },
    "所有者": {
      "label": "所有者",
      "view": { "type": "label", "props": { "value": ":owner.login" } },
      "edit": {
        "type": "input",
        "props": { "value": ":owner.login", "hidden": true }
      }
    }
  },
  "filters": {
    "组织名称": {
      "label": "组织名称",
      "bind": "where.org.eq",
      "input": { "type": "input", "props": { "placeholder": "请输入组织名称" } }
    }
  },
  "list": {
    "primary": "id",
    "layout": {
      "columns": [
        { "name": "ID", "width": 80 },
        { "name": "名称", "width": 100 },
        { "name": "所有者", "width": 100 }
      ],
      "filters": [{ "name": "组织名称" }]
    },
    "actions": {},
    "option": {
      "operation": {
        "hideEdit": true,
        "unfold": true,
        "width": 100,
        "items": []
      }
    }
  },
  "edit": {
    "primary": "id",
    "layout": {
      "fieldset": [
        {
          "columns": [
            { "name": "名称", "width": 12 },
            { "name": "所有者", "width": 12 }
          ]
        }
      ]
    },
    "actions": { "cancel": {}, "save": {}, "delete": {} }
  }
}
```

</Detail>

**运行表格处理器调试:**

```bash
yao run xiang.table.Search github '::{"org":"yaoapp"}' 1 10
yao run xiang.table.Find github 449255223 '::{}'
```

**使用管理界面调试:**

1. `yao start` 启动服务
2. 打开浏览器访问 `http://127.0.0.1:5099/xiang/table/github`
3. 打开浏览器控制台，查看 API 接口返回值。

<Div style={{ display: "flex", justifyContent: "space-between" }}>
  <Link
    type="prev"
    title="表格数据预处理"
    link="c.高级特性/e.表格数据预处理"
  ></Link>
  <Link
    type="next"
    title="使用会话数据"
    link="c.高级特性/g.使用会话数据"
  ></Link>
</Div>
