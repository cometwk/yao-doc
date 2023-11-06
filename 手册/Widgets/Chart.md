# Chart 图表界面

<blockquote>
  Chart Widget 用于图表界面制作。 Chart DSL 文件放在 charts 目录中, 文件扩展名为
  .chart.json。
</blockquote>

**约定**

1. 示例中约定应用根目录为 `/data/app`, 实际编写时需替换为应用根目录。
2. 使用 `<>` 标识自行替换的内容。 例如: `icon-<图标名称>`, 实际编写时应替换为: `icon-foo`, `icon-bar` ...

**命名**

DSL 文件命名:

1. 由 **小写字母**, **下划线 “\_”**, **横杠 "-"** 组成,
2. 必须由 **小写字母** 开头,
3. Widget ID 为文件名称(不含扩展名), 如包含多级目录用 **"."** 替代 **"\/"**

| DSL 文件                                       | Widget ID            |
| ---------------------------------------------- | -------------------- |
| /data/app/charts/dashboard.chart.json          | `dashboard`          |
| /data/app/charts/user/dashboard.chart.json     | `user.dashboard`     |
| /data/app/charts/user/pet/dashboard.chart.json | `user.pet.dashboard` |

**路由**

默认:

`http://<IP|域名>:<YAO_PORT>/<管理后台路由前缀>/x/Chart/<Widget ID>`

Query 参数:

`http://<IP|域名>:<YAO_PORT>/<管理后台路由前缀>/x/Chart/<Widget ID>?<URLQuery Params>`

<Detail title="查看图表示例 /data/app/charts/dashboard.chart.json">

```json
{
  "name": "dashboard"
}
```

</Detail>

## Chart DSL

| 字段   | 类型   | 必填项 | 默认值 | 示例                       | 说明                                                                |
| ------ | ------ | ------ | ------ | -------------------------- | ------------------------------------------------------------------- |
| name   | String | 是     |        | `Pet Admin`                | 图表名称, 支持多语言                                                |
| action | Object | 是     |        | [查看详情](#action-object) | 图表数据交互。用于指定统计数据读取处理器，设置数据 Hook，绑定模型等 |
| layout | Object |        |        | [查看详情](#layout-object) | 图表界面布局。字段、筛选器等                                        |
| fields | Object |        |        | [查看详情](#fields-object) | 图表字段定义。指定图表字段, 图表筛选器字段定义                      |
| config | Object |        |        | [查看详情](#config-object) | 图表界面配置项。图表满屏显示等配置                                  |

### action Object

图表数据交互。用于指定表检索、保存等操作的处理器，设置数据 Hook，绑定模型等

| 字段        | 类型   | 必填项 | 默认值 | 示例                                 | 说明                                                                        |
| ----------- | ------ | ------ | ------ | ------------------------------------ | --------------------------------------------------------------------------- |
| setting     | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。返回图表页面配置                                                |
| data        | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定数据图表分析结果处理器，返回图表数据                        |
| before:data | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表 |
| after:data  | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之后运行，输入关联处理器返回结果，返回处理后的结果  |

#### action.关联处理器 Object

使用关联处理器指定图表数据读取、写入逻辑。

| 字段    | 类型   | 必填项 | 默认值     | 示例                | 说明                                    |
| ------- | ------ | ------ | ---------- | ------------------- | --------------------------------------- |
| guard   | String |        | bearer-jwt | `scripts.guard.Pet` | 数据接口鉴权方式                        |
| process | String |        |            | `flows.pet.stat`    | 关联处理器名称                          |
| default | Array  |        |            | `[null]`            | 关联处理器默认值，null 表示不设定默认值 |

#### Before Hook

在关联处理器之前运行，一般用于处理参数表数据。

```jsonc
{
  "name": "::Pet Chart",
  "action": {
    "before:data": "scripts.stat.BeforeData",
    "data": {
      "process": "scripts.stat.Data",
      "default": ["2022-09-20"]
    },
    "after:data": "scripts.stat.AfterData"
  }
}
```

/data/app/scripts/stat.js Hook 脚本

```javascript
/**
 * 在关联处理器 search 之前运行
 * @param query 查询参数
 * @param page 当前页面
 * @param pagesize 每页显示记录数
 */
function BeforeData(query) {
  return [query];
}
```

#### After Hook

在关联处理器之后运行，一般用于处理结果集数据。

```jsonc
{
  "name": "::Pet Chart",
  "action": {
    "before:data": "scripts.stat.BeforeData",
    "data": {
      "process": "scripts.stat.Data",
      "default": ["2022-09-20"]
    },
    "after:data": "scripts.stat.AfterData"
  }
}
```

/data/app/scripts/stat.js Hook 脚本

```javascript
/**
 * 在关联处理器 search 之后运行
 * @param result 处理器运行结果
 */
function AfterData(result) {
  return result;
}
```

### layout Object

图表界面布局。显示字段、筛选器、批量编辑等

| 字段      | 类型   | 必填项 | 默认值 | 示例                                | 说明                                       |
| --------- | ------ | ------ | ------ | ----------------------------------- | ------------------------------------------ |
| primary   | String | 是     |        | `user_id`                           | 数据主键                                   |
| operation | Object | 是     |        | [查看详情](#layoutoperation-object) | 图表界面头部布局。设置批量操作、导入配置等 |
| filter    | Object | 是     |        | [查看详情](#layoutfilter-object)    | 图表筛选器。设置筛选条件和右上角操作按钮等 |
| chart     | Object | 是     |        | [查看详情](#layoutchart-object)     | 图表布局。设置显示，行操作按钮等           |

#### layout.operation Object

图表界面头部布局。设置批量操作、导入配置等

| 字段    | 类型  | 必填项 | 默认值 | 示例 | 说明           |
| ------- | ----- | ------ | ------ | ---- | -------------- |
| actions | Array |        |        |      | 自定义操作按钮 |

```jsonc
{
  // 自定义操作按钮
  "actions": [
    {
      "title": "页面跳转", // 按钮名称
      "icon": "icon-airplay", // 按钮图标, 可用图标 https://feathericons.com/

      // 按钮响应操作 KEY: 执行动作, VALUE: 参数表
      "action": {
        "History.push": { "payload": "/404" }
      }
    },
    {
      "title": "云函数",
      "icon": "icon-cloud",
      "action": {
        // 调用 /data/app/services/foo.js 中定义的 function Bar(...args){} 方法
        "Service.foo": { "method": "Bar", "args": ["foo", "bar"] }
      }
    },
    {
      "title": "Studio 方法",
      "icon": "icon-layers",
      "action": {
        // 调用 /data/app/studio/hello.js 中定义的 function World(...args){} 方法
        // **仅开发模式下有效**
        "Studio.hello": { "method": "World", "args": ["hello", "world"] }
      }
    }
  ]
}
```

**可用自定义操作 actions[*].action**

| KEY 执行动作   | VALUE 参数                                     | 说明                                    |
| -------------- | ---------------------------------------------- | --------------------------------------- |
| History.push   | `{ "payload": "<路由地址>"}`                   | 跳转到指定路由地址                      |
| Service.<名称> | `{ "method": "<函数名>", "args": [<参数表>] }` | 调用云函数                              |
| Studio.<名称>  | `{ "method": "<函数名>", "args": [<参数表>] }` | 调用 Studio 云函数 **仅开发模式下有效** |
| ....           | ...                                            | ...                                     |

#### layout.filter Object

图表筛选器。设置筛选条件和右上角操作按钮等

| 字段    | 类型  | 必填项 | 默认值 | 示例 | 说明                                            |
| ------- | ----- | ------ | ------ | ---- | ----------------------------------------------- |
| columns | Array |        |        |      | 筛选条件, 在 fields.filter 中定义的筛选条件字段 |

```jsonc
{
  // 支持筛选的字段清单
  "columns": [
    { "name": "名称", "width": 4 }, // name: fields.filter.<KEY>; width: 字段宽度, 24 栅格
    { "name": "状态", "width": 4 }
  ]
}
```

#### layout.chart Object

图表布局。设置显示，行操作按钮等

| 字段    | 类型  | 必填项 | 默认值 | 示例 | 说明     |
| ------- | ----- | ------ | ------ | ---- | -------- |
| columns | Array | 是     |        |      | 图表定义 |

```jsonc
{
  "columns": [
    { "name": "宠物数量", "width": 6 }, // name: fields.chart 中定义的字段名称; width: 字段宽度, 24栅格
    { "name": "宠物类型", "width": 6 },
    { "name": "收入_折线图", "width": 24 }
  ]
}
```

### fields Object

图表字段定义。指定图表字段, 图表筛选器字段定义

| 字段   | 类型   | 必填项 | 默认值 | 示例                             | 说明               |
| ------ | ------ | ------ | ------ | -------------------------------- | ------------------ |
| filter | Object | 是     |        | [查看详情](#fieldsfilter-object) | 图表筛选器字段定义 |
| chart  | Object | 是     |        | [查看详情](#fieldschart-object)  | 图表字段定义       |

#### fields.filter Object

图表筛选器字段定义

KEY: 筛选器字段名称, VALUE: 字段定义

```jsonc
{
  "医生": {
    "bind": "where.doctor_id.eq", // query 名称, 例: /api/__yao/chart/pet/search?where.doctor_id.eq=xxx

    // 用户输入组件
    "edit": {
      "type": "Select", // 组件名称, 可用组件参考文档 https://yaoapps.com/components

      // 组件参数表
      "props": {
        "placeholder": "请选择医生",
        "xProps": {
          // 在字段名称前加 $ 前缀, 并指定处理器，将自动将处理器解析为 API
          "$remote": {
            "process": "scripts.doctor.SelectOption",
            "query": { "limit": 200 }
          }
        }
      }
    }
  }
}
```

#### fields.chart Object

图表字段定义

KEY: 图表字段名称, VALUE: 字段定义

```jsonc
{
  "收入": {
    "bind": "income", // 绑定API接口返回字段名称

    // 字段数据呈现组件
    "view": {
      "type": "NumberChart", // 组件名称, 可用组件参考文档 https://yaoapps.com/components
      "link": "/x/Table/pet", // 链接地址

      // 数据数值计算
      // 参数表:
      //   $C(row) 当前行数据,
      //   $C(value) 当前行当前字段数值,
      //   $C(props) 当前组件 props,
      //   $C(type) 当前组件 type,
      //   $C(id) 当前 Widget ID
      //   'hello' 字符串常量
      //   1024 整形常量
      //   0.618 浮点型常量
      "compute": {
        "process": "Concat", // 处理器名称
        "args": ["$C(row.name)", "-", "$C(row.status)"]
      },

      "props": {
        "chartHeight": 150,
        "prefix": "¥",
        "decimals": 2,
        "nameKey": "date",
        "valueKey": "value"
      }
    }
  },
  "支出": {
    "bind": "cost",
    "link": "/x/Table/pet",
    "view": {
      "type": "NumberChart",
      "props": {
        "chartHeight": 150,
        "color": "red",
        "prefix": "¥",
        "decimals": 2,
        "nameKey": "date",
        "valueKey": "value"
      }
    }
  }
}
```

[内建 Compute 处理器](../处理器/Compute.mdx)

### config Object

图表界面配置项。图表满屏显示等配置

| 字段 | 类型    | 必填项 | 默认值 | 示例    | 说明             |
| ---- | ------- | ------ | ------ | ------- | ---------------- |
| full | Boolean | 否     | `true` | `false` | 是否满屏显示图表 |

## API

Chart Widget API

| 请求方式 | 路由                                            | 鉴权               | query        | payload | 说明                                                            |
| -------- | ----------------------------------------------- | ------------------ | ------------ | ------- | --------------------------------------------------------------- |
| `GET`    | `/api/__yao/chart/:id/setting`                  | `关联处理器中指定` |              |         | 获取图表配置信息                                                |
| `GET`    | `/api/__yao/chart/:id/component/:xpath/:method` | `关联处理器中指定` |              |         | 返回 `fields.chart\|filter.<key>.props.$xxx` 绑定处理器运行结果 |
| `GET`    | `/api/__yao/chart/:id/data`                     | `关联处理器中指定` | Query String |         | 按条件查询统计数据, 返回各个图表统计结果                        |

## 处理器

Chart Widget 处理器

| 处理器            | 参数表                             | 返回值               | 说明                                         |
| ----------------- | ---------------------------------- | -------------------- | -------------------------------------------- |
| yao.chart.Setting | `[<Widget ID>]`                    | 返回图表配置         | 返回图表 DSL 信息                            |
| yao.chart.Xgen    | `[<Widget ID>]`                    | 返回图表配置         | 返回图表配置信息, 用于 XGEN 界面引擎页面渲染 |
| yao.chart.Data    | `[<Widget ID>, ...<自定义参数表>]` | 返回各个图表统计结果 | 调用关联处理器，查询图表统计结果             |
