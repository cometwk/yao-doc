# Table

```nomnoml render
[Foo] -> [Bar]
```
xxx

## DSL

```ts
export declare namespace Table {
  interface DSL {
    id?: string               // WidgetId (比如demo.pet), 在 xui 换成了 model ，一个意思
    name?: string
    action?: ActionDSL        // 后端 Action 
    layout?: {                // LayoutDSL : 前端页面
      primary?: string        // 类似 prumary key 的字段名, 比如 uuid 
      header?: HeaderLayoutDSL  // 布局分三部分 
      filter?: FilterLayoutDSL 
      table?: ViewLayoutDSL 
      config?: Record<string, any> 
    }
    fields?: {                // FieldsDSL:    后端字段 
      filter?: Field.Filters 
      table?: Field.Columns 
    }
    config?: Record<string, any> 
    // cProps: field.CloudProps
    // compute: compute.Computable
    // mapping: mapping.Mapping
  }
}
```

```ts
  interface HeaderLayoutDSL {
    preset?: {              // PresetHeaderDSL
      batch?: {             // BatchPresetDSL
        columns?: Component.InstanceDSL[]
        deletable?: boolean 
      }
      import?: { // ImportPresetDSL
        name?: string 
        actions?: Component.Actions 
      }
    }
    actions: Component.ActionDSL[]
  }
  interface FilterLayoutDSL {
    actions?: Component.Actions 
    columns?: Component.Instances 
  }
  interface ViewLayoutDSL {
    props?: Component.PropsDSL          // 额外属性 ???
    columns?: Component.Instances       // Field.Columns 和  Component.Instances 的区别
    operation: { // OperationTableDSL
      width?: number 
      fold?: boolean                    // 风格选择：menu or list
      hide?: boolean 
      actions: Component.Actions        // 前端动作
    }
  }
```

-  Field.Columns 和  Component.Instances 的区别
  - Field.Columns 数据相关的定义，如db字段名，bind变量名 等
  - Component.Instances 前端界面相关的定义，如宽度, 标题等

## 属性

- name: 表格名称
- layout.primary: 主键
- layout.header?: Header
- layout.filter?: Filter
- layout.table.props?: Antd TableProps（非必填）
- layout.table.columns: 字段描述（`Array<BaseColumn>`）
- layout.table.operation: 数据项操作
  - width?: 操作栏宽度
  - hide?: 是否隐藏
  - fold?: 是否折叠
  - actions: Actions
- fields.filter: `Fields`
- fields.table: `Fields`

### Header

页面顶部的一些设置。

```ts
interface Header {
  preset: {
    batch?: {
      columns: Array<Common.WideColumn>;
      deletable: boolean;
    };
    import?: {
      api: {
        setting: string;
        mapping: string;
        preview: string;
        import: string;
        mapping_setting_model: string;
        preview_setting_model: string;
      };
      operation: Array<any>;
    };
  };
  actions?: Array<{
    title: string;
    icon: string;
    props: {
      type: string;
      payload: any;
    };
  }>;
}
```

### Filter

表格的过滤器设置以及表格整体的相关的一些操作（仅支持`Common.historyPush`和`Common.openModal`）。

```ts
interface Filter {
  columns: Array<Common.WideColumn>;
  actions?: Actions;
}

interface WideColumn {
  name: string;
  width: number;
}
```

### Section

```ts
interface BaseColumn {
  name: string;
  width?: number;
}
```

tabs 会被渲染成支持切换 Tab 栏。

## 示例

```json
{
  "name": "::Pet Admin",

  "action": {
    "bind": { "model": "pet", "option": { "withs": { "doctor": {} } } },

    "before:search": "scripts.pet.BeforeSearch",
    "search": { "process": "scripts.pet.Search", "default": [null, 1, 15] },
    "after:search": "scripts.pet.AfterSearch",

    "find": { "guard": "-" },
    "get": { "guard": "bearer-jwt,scripts.pet.Guard" },

    "save": {},
    "delete": {}
  },

  "layout": {
    "primary": "id",

    "header": {
      "preset": {
        "batch": {
          "columns": [
            { "name": "名称", "width": 12 },
            { "name": "消费金额", "width": 12 },
            { "name": "入院状态", "width": 12 }
          ],
          "deletable": true
        },
        "import": {
          "name": "pet",
          "operation": [{ "title": "跳转", "link": "https://baidu.com" }]
        }
      }
    },

    "filter": {
      "columns": [
        { "name": "名称", "width": 4 },
        { "name": "状态", "width": 4 }
      ],
      "actions": [
        {
          "title": "添加宠物",
          "icon": "icon-plus",
          "width": 3,
          "action": {
            "Common.openModal": {
              "width": 640,
              "Form": { "type": "edit", "model": "pet" }
            }
          }
        }
      ]
    },

    "table": {
      "columns": [
        { "name": "名称" },
        { "name": "消费金额" },
        { "name": "入院状态" }
      ],
      "operation": {
        "fold": false,
        "width": 255,
        "actions": [
          {
            "title": "查看",
            "icon": "icon-eye",
            "action": {
              "Common.openModal": {
                "width": 640,
                "Form": { "type": "view", "model": "pet" }
              }
            }
          },
          {
            "title": "编辑",
            "icon": "icon-edit-2",
            "action": {
              "Common.openModal": {
                "Form": { "type": "edit", "model": "pet" }
              }
            }
          },
          {
            "title": "治愈",
            "icon": "icon-check",
            "action": {
              "Table.save": { "id": ":id", "status": "cured" }
            },
            "style": "success",
            "confirm": { "title": "提示", "desc": "确认变更为治愈状态？" }
          },
          {
            "title": "查看详情",
            "icon": "icon-book-open",
            "action": {
              "Common.historyPush": {
                "pathname": "/x/Form/pet/:id/edit"
              }
            }
          },
          {
            "title": "返回上一页",
            "icon": "icon-arrow-left",
            "action": { "Common.historyBack": {} }
          },
          {
            "title": "删除",
            "icon": "icon-trash-2",
            "action": { "Table.delete": {} },
            "style": "danger",
            "confirm": {
              "title": "提示",
              "desc": "确认删除，删除后数据无法恢复？"
            }
          }
        ]
      }
    }
  },

  "fields": {
    "filter": {
      "名称": {
        "bind": "where.name.like",
        "edit": {
          "type": "Input",
          "props": { "placeholder": "请输入宠物名称" }
        }
      },
      "状态": {
        "bind": "where.status.in",
        "edit": {
          "type": "Select",
          "props": {
            "xProps": {
              "$remote": {
                "process": "models.pet.Get",
                "query": { "select": ["id", "name"] }
              }
            }
          }
        }
      }
    },

    "table": {
      "名称": {
        "bind": "name",
        "view": { "bind": "cost", "type": "Text", "props": {} },
        "edit": {
          "type": "Input",
          "bind": "cost",
          "props": { "placeholder": "请输入宠物名称 {{id}}" }
        }
      },
      "入院状态": {
        "bind": "status",
        "view": {
          "type": "Tag",
          "props": {
            "xProps": {
              "$remote": {
                "process": "models.pet.Get",
                "query": { "select": ["id", "name"] }
              }
            },
            "pure": true
          }
        },
        "edit": {
          "type": "Select",
          "props": {
            "xProps": {
              "$remote": {
                "process": "models.pet.Get",
                "query": { "select": ["id", "name"] }
              }
            }
          }
        }
      },
      "状态": {
        "bind": "mode",
        "view": {
          "type": "Switch",
          "props": {
            "checkedValue": "enabled",
            "unCheckedValue": "disabled",
            "checkedChildren": "开启",
            "unCheckedChildren": "关闭"
          }
        }
      },
      "消费金额": {
        "bind": "cost",
        "view": { "type": "Text", "props": {} },
        "edit": { "type": "Input", "props": {} }
      }
    }
  }
}
```
