# 描述界面

<blockquote>
  编写 JSON 页面描述，将其放置在 `tables`
  目录中，即可实现一套数据列表、数据展示和数据编辑的界面。
</blockquote>

通过类似的方式，还可以描述分析图表界面 (`charts`目录)、 数据看板界面 (
`kanban` 目录) 和 数据大屏界面 (`screens` 目录) 。

对于特殊页面，可以编写 HTML
页面，放置在 `ui` 目录，可作为独立界面展示，亦可通过 `iframe` 嵌入管理系统。

## 数据表格

编写一个数据表格描述文件 pet.tab.json，放置在应用的 tables 目录中。

**描述文件内容:**

<Detail title="查看源码">

```json
{
  "name": "宠物",
  "version": "1.0.0",
  "decription": "宠物管理表格",
  "bind": { "model": "pet" },
  "apis": {},
  "columns": {
    "ID": {
      "label": "ID",
      "view": { "type": "label", "props": { "value": ":id" } }
    },
    "编号": {
      "label": "编号",
      "view": { "type": "label", "props": { "value": ":sn" } },
      "edit": { "type": "input", "props": { "value": ":sn" } }
    },
    "名称": {
      "label": "名称",
      "view": { "type": "label", "props": { "value": ":name" } },
      "edit": { "type": "input", "props": { "value": ":name" } }
    },
    "类型": {
      "label": "类型",
      "view": { "type": "label", "props": { "value": ":kind" } },
      "edit": {
        "type": "select",
        "props": {
          "value": ":kind",
          "options": [
            { "label": "猫", "value": "猫" },
            { "label": "狗", "value": "狗" }
          ]
        }
      }
    },
    "介绍": {
      "label": "介绍",
      "view": { "type": "label", "props": { "value": ":desc" } },
      "edit": { "type": "textArea", "props": { "value": ":desc", "rows": 4 } }
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
        { "name": "编号", "width": 100 },
        { "name": "名称", "width": 200 },
        { "name": "类型" }
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
          "columns": [
            { "name": "编号", "width": 8 },
            { "name": "名称", "width": 8 },
            { "name": "类型", "width": 8 },
            { "name": "介绍", "width": 24 }
          ]
        }
      ]
    },
    "actions": { "cancel": {}, "save": {}, "delete": {} }
  }
}
```

</Detail>

**应用目录结构:**

```bash
├── apis        # 用于存放接口描述文件
│   └── pet.http.json
├── models        # 用于存放数据模型描述文件
│   └── pet.mod.json
├── tables        # 用于存放数据表格描述文件
│   └── pet.tab.json
├── db
└── ui
└── app.json
```

**访问表格界面:**

页面路由: `/xiang/table/<Table Name>`

1. 打开浏览器, 访问 `https://127.0.0.1:5099/xiang/login/admin`，

2. 输入默认用户名: `xiang@iqka.com`， 密码: `A123456p+`

3. 成功登录后在地址栏输入 `https://127.0.0.1:5099/xiang/table/pet`

4. 建议将 `/xiang/table/pet` 路由添加为菜单项。

<Notice type="warning">
  注意：由于该项目诞生之初主要是为了提高团队内部生产力，在约定俗成的写法描述下，并没有做细粒度的抛错处理，所以开发者可能会在编写
  JSON 调试界面的过程当中遇到界面为空的情况。处置方式请查阅组件文档。
</Notice>

Yao 将根据数据模型中定义的字段类型，自动生成组件关联。如在 `columns`中重新声明，将覆盖默认关联组件。数据模型与数据表格不耦合，如不设置数据模型绑定，可以通过指定处理器的方式，指定列表，详情的数据读取逻辑，以及保存、删除等操作的处理逻辑。

一个模型可以与多张表格绑定，可以共享字段关联的组件描述，不必为每张表格都重写一遍；将字段描述放置在`libs` 目录，通过 `@` 引入，详情查阅数据表格 API 文档。

扩展阅读:

<Extend
  title="数据表格"
  desc="了解数据表格组件、筛选器、批量管理、文件导入等功能描述方式。"
  link="f.参考手册/g.数据表格"
></Extend>

<Extend
  title="组件"
  desc="用于数据展示、数据录入及图表组件列表"
  link="https://yaoapps.com/components"
></Extend>

## 数据看板

编写一个数据看板描述文件 pet.kan.json，放置在应用的 kanban 目录中。

**描述文件内容:**

<Detail title="查看源码">

```json
{
  "label": "宠物统计",
  "version": "1.0.0",
  "description": "宠物统计",
  "nodes": [
    {
      "name": "类型汇总",
      "engine": "xiang",
      "query": {
        "select": [":COUNT(id) as 数量", "kind as 类型"],
        "groups": "类型",
        "from": "$pet"
      }
    }
  ],
  "output": {
    "data": {
      "宠物类型分布": "{{$res.类型汇总}}"
    }
  },
  "page": {
    "primary": "kind",
    "layout": {
      "filters": [],
      "charts": [
        {
          "name": "宠物类型分布",
          "width": 24,
          "type": "bar",
          "props": {
            "height": 240,
            "x_key": "类型",
            "axisLabel": {
              "interval": 0,
              "rotate": 45,
              "textStyle": { "fontSize": 10 }
            },
            "tooltip": {
              "textStyle": { "color": "#a2a5b9", "fontSize": 12 },
              "backgroundColor": "#232326",
              "borderRadius": 6
            },
            "series": [
              {
                "name": "数量",
                "type": "bar",
                "colorBy": "data",
                "splitLine": { "show": false },
                "label": { "show": true, "position": "top" },
                "axisLabel": { "show": true }
              }
            ]
          }
        }
      ]
    }
  }
}
```

</Detail>

**应用目录结构:**

```bash
├── apis        # 用于存放接口描述文件
│   └── pet.http.json
├── models        # 用于存放数据模型描述文件
│   └── pet.mod.json
├── tables        # 用于存放数据表格描述文件
│   └── pet.tab.json
├── kanban        # 用于存放数据看板描述文件
│   └── pet.kan.json
├── db
└── ui
└── app.json
```

**访问看板界面:**

页面路由: `/xiang/kanban/<Kanban Name>`

1. 在地址栏输入 `https://127.0.0.1:5099/xiang/kanban/pet`

2. 建议将 `/xiang/kanban/pet` 路由添加为菜单项。

扩展阅读:

<Extend
  title="数据看板"
  desc="了解数据看板相关组件，处理器、API接口输入输出等描述方式。"
  link="f.参考手册/h.分析图表"
></Extend>

<Extend
  title="编写数据流"
  desc="了解如何使用数据流，编排数据查询逻辑。"
  link="b.基础特性/e.编写数据流"
></Extend>

<Extend
  title="查询数据"
  desc="了解如何在数据流中使用数据模型处理器和Query DSL 查询数据。"
  link="b.基础特性/f.查询数据"
></Extend>

## 分析图表

通常情况下，数据分析需要用户输入时间日期等参数，根据时间范围检索。数据分析图表组件，在数据看板描述基础上，通过 `filters` 设定查询条件。

编写一个数据分析描述文件 pet.cha.json，放置在应用的 charts 目录中。

**描述文件内容:**

<Detail title="查看源码">

```json
{
  "label": "宠物统计",
  "version": "1.0.0",
  "description": "宠物统计",
  "nodes": [
    {
      "name": "类型汇总",
      "engine": "xiang",
      "query": {
        "select": [":COUNT(id) as 数量", "kind as 类型"],
        "wheres": [{ ":kind": "宠物类型", "in": "$kinds" }],
        "groups": "类型",
        "from": "$pet"
      }
    }
  ],
  "output": {
    "data": {
      "宠物类型分布": "{{$res.类型汇总}}"
    },
    "query": "{{$in}}"
  },
  "apis": {
    "data": { "default": [{ "kinds": ["猫", "狗"] }] }
  },
  "filters": {
    "类型": {
      "label": "类型",
      "bind": "kinds",
      "input": {
        "type": "select",
        "props": {
          "mode": "multiple",
          "options": [
            { "label": "猫", "value": "猫" },
            { "label": "狗", "value": "狗" }
          ]
        }
      }
    }
  },
  "page": {
    "primary": "kind",
    "layout": {
      "filters": [{ "name": "类型" }],
      "charts": [
        {
          "name": "宠物类型分布",
          "width": 24,
          "type": "bar",
          "props": {
            "height": 240,
            "x_key": "类型",
            "axisLabel": {
              "interval": 0,
              "rotate": 45,
              "textStyle": { "fontSize": 10 }
            },
            "tooltip": {
              "textStyle": { "color": "#a2a5b9", "fontSize": 12 },
              "backgroundColor": "#232326",
              "borderRadius": 6
            },
            "series": [
              {
                "name": "数量",
                "type": "bar",
                "colorBy": "data",
                "splitLine": { "show": false },
                "label": { "show": true, "position": "top" },
                "axisLabel": { "show": true }
              }
            ]
          }
        }
      ]
    }
  }
}
```

</Detail>

**应用目录结构:**

```bash
├── apis        # 用于存放接口描述文件
│   └── pet.http.json
├── models        # 用于存放数据模型描述文件
│   └── pet.mod.json
├── tables        # 用于存放数据表格描述文件
│   └── pet.tab.json
├── kanban        # 用于存放数据看板描述文件
│   └── pet.kan.json
├── charts        # 用于存放数据分析描述文件
│   └── pet.cha.json
├── db
└── ui
└── app.json
```

**访问看:**

页面路由: `/xiang/chart/<Chart Name>`

1. 在地址栏输入 `https://127.0.0.1:5099/xiang/chart/pet`

2. 建议将 `/xiang/chart/pet` 路由添加为菜单项。

扩展阅读:

<Extend
  title="分析图表"
  desc="了解分析图表相关组件，处理器、API接口输入输出等描述方式。"
  link="d.API参考/h1.分析图表"
></Extend>

## 数据大屏

数据大屏常用于投影到大屏设备，全屏显示相关图表。大屏配置项同 Chart，区别是，大屏没有筛选栏，且大屏多出顶部指标栏，以及大屏的布局为 grid 布局，且纵向排布，需同时设定 width 和 height，width 为 24 栅格，height 为 12 栅格。对于较为复杂的大屏页面，推荐通过 [HTML 页面](#html-页面)实现。

编写一个数据大屏描述文件 pet.scr.json，放置在应用的 screens 目录中，在数据看板中，可以添加大屏幕连接。

<Detail title="查看源码">

```json
{
  "label": "宠物统计",
  "version": "1.0.0",
  "description": "宠物统计",
  "nodes": [
    {
      "name": "类型汇总",
      "engine": "xiang",
      "query": {
        "select": [":COUNT(id) as 数量", "kind as 类型"],
        "groups": "类型",
        "from": "$pet"
      }
    }
  ],
  "output": {
    "data": {
      "宠物类型分布": "{{$res.类型汇总}}"
    }
  },
  "page": {
    "primary": "kind",
    "layout": {
      "filters": [],
      "charts": [
        {
          "name": "宠物类型分布",
          "width": 4,
          "height": 4,
          "type": "bar",
          "props": {
            "x_key": "类型",
            "axisLabel": {
              "interval": 0,
              "rotate": 45,
              "textStyle": { "fontSize": 10 }
            },
            "tooltip": {
              "textStyle": { "color": "#a2a5b9", "fontSize": 12 },
              "backgroundColor": "#232326",
              "borderRadius": 6
            },
            "series": [
              {
                "name": "数量",
                "type": "bar",
                "colorBy": "data",
                "splitLine": { "show": false },
                "label": { "show": true, "position": "top" },
                "axisLabel": { "show": true }
              }
            ]
          }
        }
      ]
    }
  }
}
```

</Detail>

在数据看板中添加大屏链接:

`pet.kan.json`

```json
{
  ...
  "page": {
    "option": {
      "request_interval": 60,
      "screen": "/screen/pet"
    }
  }
  ...
}
```

**应用目录结构:**

```bash
├── apis        # 用于存放接口描述文件
│   └── pet.http.json
├── models        # 用于存放数据模型描述文件
│   └── pet.mod.json
├── tables        # 用于存放数据表格描述文件
│   └── pet.tab.json
├── kanban        # 用于存放数据看板描述文件
│   └── pet.kan.json
├── charts        # 用于存放数据分析描述文件
│   └── pet.cha.json
├── screens        # 用于存放数据大屏描述文件
│   └── pet.scr.json
├── db
└── ui
└── app.json
```

**访问大屏界面:**

页面路由: `/xiang/screen/<Screen Name>`

1. 在地址栏输入 `https://127.0.0.1:5099/xiang/screen/pet`

2. 建议通过看板 `option` 配置，添加数据大屏的链接。

<Extend
  title="数据大屏"
  desc="了解分析图表相关组件，处理器、API接口输入输出等描述方式。"
  link="d.API参考/h3.数据大屏"
></Extend>

## HTML 页面

Yao 内置了一个 HTTP Server，将 HTML 页面, CSS, JS 等文件，放置到 `ui` 目录，即可直接访问。使用这种方式，可以使用任意前端技术，结合内建 API，完全重构管理系统，亦可通过 `iframe` 组件或 `extend` 组件，集成到内置的管理系统中。

编写一个 HTML 页面 index.html，放置在应用的 ui 目录中。

```html
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Yao App Engine</title>
  </head>
  <body class="overscroll-none">
    It works!
  </body>
</html>
```

**应用目录结构:**

```bash
├── apis        # 用于存放接口描述文件
│   └── pet.http.json
├── models        # 用于存放数据模型描述文件
│   └── pet.mod.json
├── tables        # 用于存放数据表格描述文件
│   └── pet.tab.json
├── kanban        # 用于存放数据看板描述文件
│   └── pet.kan.json
├── charts        # 用于存放数据分析描述文件
│   └── pet.cha.json
├── screens        # 用于存放数据大屏描述文件
│   └── pet.scr.json
├── db
└── ui
│   └── index.html # 自定义页面
└── app.json
```

**访问页面:**

在地址栏输入 `https://127.0.0.1:5099/index.html` 即可
