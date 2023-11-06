# Form 表单界面

<blockquote>
  Form Widget 用于详情界面制作。 Form DSL 文件放在 forms 目录中, 文件扩展名为
  .form.json。
</blockquote>

**约定**

1. 示例中约定应用根目录为 `/data/app`, 实际编写时需替换为应用根目录。
2. 使用 `<>` 标识自行替换的内容。 例如: `icon-<图标名称>`, 实际编写时应替换为: `icon-foo`, `icon-bar` ...

**命名**

DSL 文件命名:

1. 由 **小写字母**, **下划线 “\_”**, **横杠 "-"** 组成,
2. 必须由 **小写字母** 开头,
3. Widget ID 为文件名称(不含扩展名), 如包含多级目录用 **"."** 替代 **"\/"**

| DSL 文件                                     | Widget ID            |
| -------------------------------------------- | -------------------- |
| /data/app/forms/pet.form.json                | `pet`                |
| /data/app/forms/pet/doctor.form.json         | `pet.doctor`         |
| /data/app/forms/pet/inspect/status.form.json | `pet.inspect.status` |

**路由**

阅读模式:

`http://<IP|域名>:<YAO_PORT>/<管理后台路由前缀>/x/Form/<Widget ID>/view`

编辑模式:

`http://<IP|域名>:<YAO_PORT>/<管理后台路由前缀>/x/Form/<Widget ID>/edit`

<Detail title="查看表单示例 /data/app/forms/pet.chart.json">

```json
{
  "name": "pet"
}
```

</Detail>

## Form DSL

| 字段   | 类型   | 必填项 | 默认值 | 示例                       | 说明                                                                          |
| ------ | ------ | ------ | ------ | -------------------------- | ----------------------------------------------------------------------------- |
| name   | String | 是     |        | `Pet Admin`                | 表单名称, 支持多语言                                                          |
| action | Object | 是     |        | [查看详情](#action-object) | 表单数据交互。用于指定数据读取、保存等操作的处理器，设置数据 Hook，绑定模型等 |
| layout | Object |        |        | [查看详情](#layout-object) | 表单界面布局。                                                                |
| fields | Object |        |        | [查看详情](#fields-object) | 表单字段定义。指定表单字段定义                                                |
| config | Object |        |        | [查看详情](#config-object) | 表单界面配置项。表单满屏显示等配置                                            |

### action Object

表单数据交互。用于指定列表检索、保存等操作的处理器，设置数据 Hook，绑定模型等

| 字段          | 类型   | 必填项 | 默认值 | 示例                                 | 说明                                                                        |
| ------------- | ------ | ------ | ------ | ------------------------------------ | --------------------------------------------------------------------------- |
| bind          | Object |        |        | [查看详情](#actionbind-object)       | 绑定 model 或 form。 根据关联 Widget ID 设定表单关联处理器和界面呈现默认值  |
| setting       | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。返回表单页面配置                                                |
| find          | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定按主键查询单条数据处理器和默认参数, 返回单条数据记录        |
| save          | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定保存单条数据处理器                                          |
| create        | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定新建单条数据处理器                                          |
| update        | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定按主键更新单条数据处理器                                    |
| delete        | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定按主键删除单条数据处理器                                    |
| before:get    | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表 |
| before:find   | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表 |
| before:save   | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表 |
| before:create | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表 |
| before:update | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表 |
| before:delete | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表 |
| after:find    | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果  |
| after:save    | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果  |
| after:create  | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果  |
| after:update  | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果  |
| after:delete  | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果  |
| after:insert  | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果  |

#### action.bind Object

绑定 model 或 form。 根据关联 Widget ID 设定表单关联处理器和界面呈现默认值

| 字段   | 类型   | 必填项 | 默认值 | 示例     | 说明                           |
| ------ | ------ | ------ | ------ | -------- | ------------------------------ |
| model  | String |        |        | `pet`    | 绑定数据模型。 Model Widget ID |
| table  | String |        |        | `doctor` | 绑定表格。 Table Widget ID     |
| form   | String |        |        | `doctor` | 绑定表单。 Form Widget ID      |
| option | Object |        |        | `{}`     | 参数配置                       |

##### 绑定模型

```jsonc
{
  "name": "::Bind Model",
  "action": {
    "bind": { "model": "pet" },

    // 自定义关联处理器
    "find": {
      "guard": "-", // 鉴权方式
      "process": "scripts.pet.Find", // 调用处理器
      "default": [null, { "select": ["id", "name", "status"] }] // 默认参数表
    }
  }
}
```

关联处理器默认值:

| 关联处理器 | guard      | process                     | default        |
| ---------- | ---------- | --------------------------- | -------------- |
| find       | bearer-jwt | `models.<Widget ID>.Find`   | `[null, null]` |
| save       | bearer-jwt | `models.<Widget ID>.Save`   | `[null]`       |
| create     | bearer-jwt | `models.<Widget ID>.Create` | `[null]`       |
| update     | bearer-jwt | `models.<Widget ID>.Update` | `[null, null]` |
| delete     | bearer-jwt | `models.<Widget ID>.Delete` | `[null]`       |

数据表字段类型与表单字段定义 fields 映射表:

https://github.com/YaoApp/yao/blob/main/yao/fields/model.trans.json

##### 绑定表格

```jsonc
{
  "name": "::Pet Admin Bind Table",
  "action": {
    "bind": { "table": "pet" },
    "find": {
      "guard": "-",
      "process": "scripts.pet.Find",
      "default": [null, { "select": ["id", "name", "status"] }] // 默认参数表
    }
  }
}
```

复制指定 Table Widget ID 的 `action` 和 `fields`, 并自动生成表单布局 `layout`, 在次表单基础上微调，创建一张新的表单。

##### 绑定表单

```jsonc
{
  "name": "::Pet Admin Bind Form",
  "action": {
    "bind": { "form": "bind.pet" },
    "find": {
      "guard": "-",
      "process": "scripts.pet.Find",
      "default": [null, { "select": ["id", "name", "status"] }] // 默认参数表
    }
  }
}
```

复制指定 Form Widget ID 的表单, 在次表单基础上微调，创建一张新的表单。

#### action.关联处理器 Object

使用关联处理器指定表单数据读取、写入逻辑。

| 字段    | 类型   | 必填项 | 默认值     | 示例                               | 说明                                    |
| ------- | ------ | ------ | ---------- | ---------------------------------- | --------------------------------------- |
| guard   | String |        | bearer-jwt | `scripts.guard.Pet`                | 数据接口鉴权方式                        |
| process | String |        |            | `flows.pet.find`                   | 关联处理器名称                          |
| default | Array  |        |            | `[null, {"select":["id","name"]}]` | 关联处理器默认值，null 表示不设定默认值 |

#### Before Hook

在关联处理器之前运行，一般用于处理参数表数据。

```jsonc
{
  "name": "::Pet Admin Bind Form",
  "action": {
    "bind": { "model": "pet" },
    "before:find": "scripts.pet.BeforeFind" // 设定 Hook 处理器
  }
}
```

/data/app/scripts/pet.js Hook 脚本

```javascript
/**
 * 在关联处理器 find 之前运行
 * @param id 数据记录主键数值
 * @param query 查询参数
 */
function BeforeFind(id, query) {
  return [id, query];
}

/**
 * 在关联处理器 save 之前运行
 * @param payload 用户提交数据记录
 */
function BeforeSave(payload) {
  return [payload];
}

/**
 * 在关联处理器 create 之前运行
 * @param payload 用户提交数据记录
 */
function BeforeCreate(payload) {
  return [payload];
}

/**
 * 在关联处理器 update 之前运行
 * @param id 数据记录主键数值
 * @param payload 用户提交数据记录
 */
function BeforeUpdate(id, payload) {
  return [payload];
}

/**
 * 在关联处理器 delete 之前运行
 * @param id 数据记录主键数值
 * @param query 查询参数
 */
function BeforeDelete(id) {
  return [id];
}
```

#### After Hook

在关联处理器之后运行，一般用于处理结果集数据。

```jsonc
{
  "name": "::Pet Admin Bind Form",
  "action": {
    "bind": { "model": "pet" },
    "after:find": "scripts.pet.AfterFind" // 设定 Hook 处理器
  }
}
```

/data/app/scripts/pet.js Hook 脚本

```javascript
/**
 * 在关联处理器 find 之后运行
 * @param result 处理器运行结果
 */
function AfterFind(result) {
  return result;
}

/**
 * 在关联处理器 save 之后运行
 * @param result 处理器运行结果
 */
function AfterSave(result) {
  return result;
}

/**
 * 在关联处理器 create 之后运行
 * @param result 处理器运行结果
 */
function AfterCreate(result) {
  return result;
}

/**
 * 在关联处理器 update 之后运行
 * @param result 处理器运行结果
 */
function AfterUpdate(result) {
  return result;
}

/**
 * 在关联处理器 delete 之后运行
 * @param result 处理器运行结果
 */
function AfterDelete(result) {
  return result;
}
```

### layout Object

表单界面布局。显示字段、筛选器、批量编辑等

| 字段      | 类型   | 必填项 | 默认值 | 示例                                | 说明                           |
| --------- | ------ | ------ | ------ | ----------------------------------- | ------------------------------ |
| primary   | String | 是     |        | `user_id`                           | 数据主键                       |
| operation | Object | 是     |        | [查看详情](#layoutoperation-object) | 表单功能操作。设置表单操作按钮 |
| form      | Object | 是     |        | [查看详情](#layoutform-object)      | 表单布局。设置表单字段         |

#### layout.operation Object

表单功能操作。设置表单操作按钮

| 字段    | 类型   | 必填项 | 默认值 | 示例 | 说明           |
| ------- | ------ | ------ | ------ | ---- | -------------- |
| preset  | Object |        |        |      | 基础功能操作   |
| actions | Array  |        |        |      | 自定义操作按钮 |

```jsonc
{
  "preset": {
    // 保存按钮
    "save": {
      "back": true // back = true 操作后返回上一页
    },

    "back": {} // 返回上一页按钮
  },

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
      "title": "治愈 {{name}}", // 使用 {{<字段名称>}} 引用表单数据
      "icon": "icon-check",
      "action": {
        "Form.save": { "id": ":id", "status": "cured" }
      },
      "style": "success",
      "confirm": { "title": "提示", "desc": "确认变更为治愈状态？{{name}}" }
    },
    {
      "title": "云函数",
      "icon": "icon-cloud",
      "action": {
        // 调用 /data/app/services/foo.js 中定义的 function Bar(...args){} 方法, 使用 {{<字段名称>}} 引用表单数据
        "Service.foo": { "method": "Bar", "args": ["{{id}}", "{{name}}"] }
      }
    },
    {
      "title": "Studio 方法",
      "icon": "icon-layers",
      "action": {
        // 调用 /data/app/studio/hello.js 中定义的 function World(...args){} 方法, 使用 {{<字段名称>}} 引用表单数据
        // **仅开发模式下有效**
        "Studio.hello": { "method": "World", "args": ["{{id}}", "{{name}}"] }
      }
    }
  ]
}
```

**可用自定义操作 actions[*].action**

| KEY 执行动作   | VALUE 参数                                     | 说明                                    |
| -------------- | ---------------------------------------------- | --------------------------------------- |
| History.push   | `{ "payload": "<路由地址>"}`                   | 跳转到指定路由地址                      |
| From.Save      | `{ "id": ":id", "status": "cured" }`           | 保存表单数据                            |
| From.Delete    | `{ "id": ":id"}`                               | 删除表单数据                            |
| Service.<名称> | `{ "method": "<函数名>", "args": [<参数表>] }` | 调用云函数                              |
| Studio.<名称>  | `{ "method": "<函数名>", "args": [<参数表>] }` | 调用 Studio 云函数 **仅开发模式下有效** |
| ....           | ...                                            | ...                                     |

#### layout.form Object

表单布局。设置显示列，行操作按钮等

| 字段     | 类型   | 必填项 | 默认值                   | 示例 | 说明                                    |
| -------- | ------ | ------ | ------------------------ | ---- | --------------------------------------- |
| props    | Object |        |                          |      | 表单组件 props                          |
| sections | Array  |        |                          |      | 段落                                    |
| config   | Object |        | `{ "showAnchor": true }` |      | 表单配置项, showAnchor 是否显示段落锚点 |

```jsonc
{
  "props": {},
  "config": { "showAnchor": true },
  "sections": [
    {
      "title": "基础信息", // 段落标题
      "desc": "宠物的一些基本信息", // 段落描述

      // 字段列表 在 fields.form 中定义的字段
      "columns": [
        { "name": "表格", "width": 24 }, // name: fields.form.<KEY> ,  width 字段显示宽度, 24栅格
        {
          "width": 24,

          // 标签页:
          "tabs": [
            {
              "title": "Base", // 标签名称
              "columns": [
                { "name": "ID", "width": 12 }, // name: fields.form.<KEY> ,  width 字段显示宽度, 24栅格
                { "name": "名称", "width": 12 }
              ]
            },
            {
              "title": "More",
              "columns": [{ "name": "状态", "width": 12 }]
            }
          ]
        }
      ]
    },
    {
      "title": "基础信息",
      "desc": "宠物的一些基本信息",
      "columns": [
        { "name": "ID", "width": 12 },
        { "name": "名称", "width": 12 },
        { "name": "状态", "width": 12 }
      ]
    }
  ]
}
```

### fields Object

表单字段定义。指定表单字段

| 字段 | 类型   | 必填项 | 默认值 | 示例                           | 说明         |
| ---- | ------ | ------ | ------ | ------------------------------ | ------------ |
| form | Object | 是     |        | [查看详情](#fieldsform-object) | 表单字段定义 |

**fields.form Object**

表单列字段定义

KEY: 表单列字段名称, VALUE: 字段定义

```jsonc
{
  "名称": {
    "bind": "name", // 默认绑定API接口返回字段名称

    // 字段数据呈现组件
    "view": {
      "bind": "name_view", // 绑定字段名称，如不指定使用默认值
      "type": "Text", // 组件名称, 可用组件参考文档 https://yaoapps.com/components

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

      "props": {}
    },

    // 字段数据编辑组件 (点击字段后弹出的编辑器)
    "edit": {
      "bind": "name", // 绑定字段名称，如不指定使用默认值
      "type": "Input", // 组件名称, 可用组件参考文档 https://yaoapps.com/components

      // 数据数值计算 (简写)
      // 默认参数表: ["$C(value)", "$C(props)", "$C(type)", "$C(id)"]
      "compute": "scripts.pet.FormatName",
      "props": { "placeholder": "请输入宠物名称" }
    }
  },
  "医生": {
    "bind": "doctor_id",
    "edit": {
      "type": "Select",
      "props": {
        "placeholder": "请选择医生",
        "xProps": {
          // 在字段名称前加 $ 前缀, 指定处理器名称和参数，自动将处理器解析为 API
          "$remote": {
            "process": "scripts.doctor.SelectOption",
            "query": { "pet_type": "{{ type }}" }
          }
        }
      }
    }
  }
}
```

[内建 Compute 处理器](../处理器/Compute.mdx)

### config Object

表单界面配置项。表单满屏显示等配置

| 字段 | 类型    | 必填项 | 默认值 | 示例    | 说明             |
| ---- | ------- | ------ | ------ | ------- | ---------------- |
| full | Boolean | 否     | `true` | `false` | 是否满屏显示表单 |

## API

Form Widget API

| 请求方式 | 路由                                           | 鉴权               | query                                   | payload                     | 说明                                                                |
| -------- | ---------------------------------------------- | ------------------ | --------------------------------------- | --------------------------- | ------------------------------------------------------------------- |
| `GET`    | `/api/__yao/form/:id/setting`                  | `关联处理器中指定` |                                         |                             | 获取表单配置信息                                                    |
| `GET`    | `/api/__yao/form/:id/component/:xpath/:method` | `关联处理器中指定` |                                         |                             | 返回 `fields.form\|filter.<key>.props.$xxx` 绑定处理器运行结果      |
| `GET`    | `/api/__yao/form/:id/find/:primary`            | `关联处理器中指定` | [URL Query Params](../Widgets/API.mdx)  |                             | 按主键查询单条记录，返回单条记录                                    |
| `GET`    | `/api/__yao/form/:id/download/:field`          | `JWT`              | `{"name":"<file name>", "token":"JWT"}` |                             | 文件下载 返回 `{"content":"<文件内容>", "type":"<文件 Mime Type>"}` |
| `POST`   | `/api/__yao/form/:id/upload/:xpath/:method`    | `关联处理器中指定` |                                         | `{"file":"<file content>"}` | 文件上传 `fields.form.<key>.props.$api`                             |
| `POST`   | `/api/__yao/form/:id/save`                     | `关联处理器中指定` |                                         | `{"<field>":"<value>"}`     | 保存单条记录，如 payload 中包含主键则更新，否则创建                 |
| `POST`   | `/api/__yao/form/:id/create`                   | `关联处理器中指定` |                                         | `{"<field>":"<value>"}`     | 创建一条记录                                                        |
| `POST`   | `/api/__yao/form/:id/update/:primary`          | `关联处理器中指定` |                                         | `{"<field>":"<value>"}`     | 更新指定主键的记录                                                  |
| `POST`   | `/api/__yao/form/:id/delete/:primary`          | `关联处理器中指定` |                                         | `{"<field>":"<value>"}`     | 删除指定主键的记录                                                  |

## 处理器

Form Widget 处理器

| 处理器           | 参数表                             | 返回值       | 说明                                                           |
| ---------------- | ---------------------------------- | ------------ | -------------------------------------------------------------- |
| yao.form.Setting | `[<Widget ID>]`                    | 返回表单配置 | 返回表单 DSL 信息                                              |
| yao.form.Xgen    | `[<Widget ID>]`                    | 返回表单配置 | 返回表单配置信息, 用于 XGEN 界面引擎页面渲染                   |
| yao.form.Find    | `[<Widget ID>, <主键>,<查询参数>]` | 返回记录     | 调用关联处理器，按主键查询表单数据详情                         |
| yao.form.Save    | `[<Widget ID>, <记录>]`            | 主键         | 调用关联处理器，保存一条数据记录，参数包含主键则更新，否则创建 |
| yao.form.Create  | `[<Widget ID>, <记录>]`            | 主键         | 调用关联处理器，创建数据记录                                   |
| yao.form.Delete  | `[<Widget ID>, <主键>]`            | 返回记录     | 调用关联处理器，按主键删除记录                                 |
| yao.form.Update  | `[<Widget ID>, <主键>,<记录>]`     | 返回更新行   | 调用关联处理器，更新单条记录                                   |
