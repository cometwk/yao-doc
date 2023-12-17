# Table 表格界面

<blockquote>
  Table Widget 用于列表界面制作。 Table DSL 文件放在 tables 目录中, 文件扩展名为
  .tab.json。
</blockquote>

**约定**

1. 示例中约定应用根目录为 `/data/app`, 实际编写时需替换为应用根目录。
2. 使用 `<>` 标识自行替换的内容。 例如: `icon-<图标名称>`, 实际编写时应替换为: `icon-foo`, `icon-bar` ...

**命名**

DSL 文件命名:

1. 由 **小写字母**, **下划线 “\_”**, **横杠 "-"** 组成,
2. 必须由 **小写字母** 开头,
3. Widget ID 为文件名称(不含扩展名), 如包含多级目录用 **"."** 替代 **"\/"**

| DSL 文件                                 | Widget ID        |
| ---------------------------------------- | ---------------- |
| /data/app/tables/user.tab.json           | `user`           |
| /data/app/tables/user/tasks.tab.json     | `user.tasks`     |
| /data/app/tables/user/stat/list.tab.json | `user.stat.list` |

**路由**

默认:

`http://<IP|域名>:<YAO_PORT>/<管理后台路由前缀>/x/Table/<Widget ID>`

Query 参数:

`http://<IP|域名>:<YAO_PORT>/<管理后台路由前缀>/x/Table/<Widget ID>?<URLQuery Params>`

<Detail title="查看表格示例 /data/app/tables/pet.tab.json">

```json
{
  "name": "pet"
}
```

</Detail>

```nomnoml render
[结构|
  [dsl]-:>[config]
  [dsl]-:>[fields]
  [dsl]-:>[filters]
  [dsl]-:>[header]
  [dsl]-:>[table]
  [dsl]-:>[<label> name]
]
```

```nomnoml render
[DSL|
  [DSL]-:>[<label> id]
  [DSL]-:>[<label> name]
  [DSL]-:>[config]
  [DSL]-:>[action]
  [DSL]-:>[layout]
  [DSL]-:>[fields]

  [action]-:>[ActionDSL]
  [layout]-:>[LayoutDSL]
  [fields]-:>[FieldsDSL]
  [config]-:>[<label> {}]
]
```


## Table DSL

| 字段   | 类型   | 必填项 | 默认值 | 示例                       | 说明                                                                          |
| ------ | ------ | ------ | ------ | -------------------------- | ----------------------------------------------------------------------------- |
| name   | String | 是     |        | `Pet Admin`                | 表格名称, 支持多语言                                                          |
| action | Object | 是     |        | [查看详情](#action-object) | 表格数据交互。用于指定列表检索、保存等操作的处理器，设置数据 Hook，绑定模型等 |
| layout | Object |        |        | [查看详情](#layout-object) | 表格界面布局。显示字段、筛选器、批量编辑等                                    |
| fields | Object |        |        | [查看详情](#fields-object) | 表格字段定义。指定表格列字段, 表格筛选器字段定义                              |
| config | Object |        |        | [查看详情](#config-object) | 表格界面配置项。表格满屏显示等配置                                            |

### action Object

表格数据交互。用于指定列表检索、保存等操作的处理器，设置数据 Hook，绑定模型等

| 字段                | 类型   | 必填项 | 默认值 | 示例                                 | 说明                                                                         |
| ------------------- | ------ | ------ | ------ | ------------------------------------ | ---------------------------------------------------------------------------- |
| bind                | Object |        |        | [查看详情](#actionbind-object)       | 绑定 model 或 table。 根据关联 Widget ID 设定表格关联处理器和界面呈现默认值  |
| setting             | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。返回表格页面配置                                                 |
| search              | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定列表数据搜索处理器和默认参数, 返回带有分页信息和数据记录数组 |
| get                 | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定列表数据搜索处理器和默认参数, 返回数据记录数组               |
| find                | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定按主键查询单条数据处理器和默认参数, 返回单条数据记录         |
| save                | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定保存单条数据处理器                                           |
| create              | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定新建单条数据处理器                                           |
| update              | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定按主键更新单条数据处理器                                     |
| delete              | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定按主键删除单条数据处理器                                     |
| insert              | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定插入多条数据处理器                                           |
| update-in           | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定按一组主键，更新多条数据处理器                               |
| update-where        | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定按查询条件，更新多条数据处理器                               |
| delete-in           | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定按一组主键，删除多条数据处理器                               |
| delete-where        | Object |        |        | [查看详情](#action关联处理器-object) | 关联处理器。指定按查询条件，删除多条数据处理器                               |
| before:search       | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表  |
| before:get          | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表  |
| before:find         | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表  |
| before:save         | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表  |
| before:create       | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表  |
| before:update       | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表  |
| before:delete       | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表  |
| before:insert       | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表  |
| before:update-in    | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表  |
| before:update-where | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表  |
| before:delete-in    | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表  |
| before:delete-where | String |        |        | [查看详情](#before-hook)             | Before Hook。在关联处理器之前运行，输入用户输入的参数表，返回处理后的参数表  |
| after:search        | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之后运行，输入关联处理器返回结果，返回处理后的结果   |
| after:get           | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果   |
| after:find          | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果   |
| after:save          | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果   |
| after:create        | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果   |
| after:update        | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果   |
| after:delete        | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果   |
| after:insert        | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果   |
| after:update-in     | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果   |
| after:update-where  | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果   |
| after:delete-in     | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果   |
| after:delete-where  | String |        |        | [查看详情](#after-hook)              | After Hook。在关联处理器之前运行，输入关联处理器返回结果，返回处理后的结果   |

#### action.bind Object

绑定 model 或 table。 根据关联 Widget ID 设定表格关联处理器和界面呈现默认值

| 字段   | 类型   | 必填项 | 默认值 | 示例             | 说明                                                      |
| ------ | ------ | ------ | ------ | ---------------- | --------------------------------------------------------- |
| model  | String |        |        | `pet`            | 绑定数据模型。 Model Widget ID                            |
| table  | String |        |        | `doctor`         | 绑定表格。 Table Widget ID                                |
| option | Object |        |        | `{"form":"pet"}` | 指定 Form Widget ID 关联表单, **bind.model 不为空时有效** |

##### 绑定模型

```jsonc
{
  "name": "::Bind Model",
  "action": {
    "bind": {
      "model": "pet",
      "option": { "form": "pet" } //
    },

    // 自定义关联处理器
    "search": {
      "guard": "-", // 鉴权方式
      "process": "scripts.pet.Search", // 调用处理器
      "default": [null, 1, 5] // 默认参数表
    }
  }
}
```

关联处理器默认值:

| 关联处理器   | guard      | process                          | default              |
| ------------ | ---------- | -------------------------------- | -------------------- |
| search       | bearer-jwt | `models.<Widget ID>.Paginate`    | `[null, null, null]` |
| get          | bearer-jwt | `models.<Widget ID>.Get`         | `[null]`             |
| find         | bearer-jwt | `models.<Widget ID>.Find`        | `[null, null]`       |
| save         | bearer-jwt | `models.<Widget ID>.Save`        | `[null]`             |
| create       | bearer-jwt | `models.<Widget ID>.Create`      | `[null]`             |
| update       | bearer-jwt | `models.<Widget ID>.Update`      | `[null, null]`       |
| delete       | bearer-jwt | `models.<Widget ID>.Delete`      | `[null]`             |
| insert       | bearer-jwt | `models.<Widget ID>.Insert`      | `[null, null]`       |
| update-in    | bearer-jwt | `models.<Widget ID>.UpdateWhere` | `[null, null]`       |
| update-where | bearer-jwt | `models.<Widget ID>.UpdateWhere` | `[null, null]`       |
| delete-in    | bearer-jwt | `models.<Widget ID>.DeleteWhere` | `[null]`             |
| delete-where | bearer-jwt | `models.<Widget ID>.DeleteWhere` | `[null]`             |

数据表字段类型与表格字段定义 fields 映射表:

https://github.com/YaoApp/yao/blob/main/yao/fields/model.trans.json

同时绑定表单:

如果将 `bind.option.form` 指定为 Form Widget ID, 表格将增加新增、查看、编辑功能。

##### 绑定表格

```jsonc
{
  "name": "::Pet Admin Bind Table",
  "action": {
    "bind": { "table": "bind.pet" },
    "search": {
      "guard": "-",
      "process": "scripts.pet.Search",
      "default": [null, 1, 2]
    }
  }
}
```

复制指定 Table Widget ID 的表格, 在次表格基础上微调，创建一张新的表格。

#### action.关联处理器 Object

使用关联处理器指定表格数据读取、写入逻辑。

| 字段    | 类型   | 必填项 | 默认值     | 示例                | 说明                                    |
| ------- | ------ | ------ | ---------- | ------------------- | --------------------------------------- |
| guard   | String |        | bearer-jwt | `scripts.guard.Pet` | 数据接口鉴权方式                        |
| process | String |        |            | `flows.pet.search`  | 关联处理器名称                          |
| default | Array  |        |            | `[null, 1, 2]`      | 关联处理器默认值，null 表示不设定默认值 |

#### Before Hook

在关联处理器之前运行，一般用于处理参数表数据。

```jsonc
{
  "name": "::Pet Admin Bind Table",
  "action": {
    "bind": { "model": "pet" },
    "before:search": "scripts.pet.BeforeSearch" // 设定 Hook 处理器
  }
}
```

/data/app/scripts/pet.js Hook 脚本

```javascript
/**
 * 在关联处理器 search 之前运行
 * @param query 查询参数
 * @param page 当前页面
 * @param pagesize 每页显示记录数
 */
function BeforeSearch(query, page, pagesize) {
  return [query, page, pagesize];
}

/**
 * 在关联处理器 get 之前运行
 * @param query 查询参数
 */
function BeforeGet(query) {
  return [query];
}

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

/**
 * 在关联处理器 insert 之前运行
 * @param columns 字段清单 ["id", "name", "status"...]
 * @param values 与字段对应的数值列表 [[1, "foo", "enabled"], [2, "bar", "disabled"]]
 */
function BeforeInsert(columns, values) {
  return [columns, values];
}

/**
 * 在关联处理器 update-in 之前运行
 * @param ids 主键列表
 * @param payload 更新字段
 */
function BeforeUpdateIn(ids, payload) {
  return [ids, payload];
}

/**
 * 在关联处理器 update-where 之前运行
 * @param query 查询条件
 * @param payload 更新字段
 */
function BeforeUpdateWhere(query, payload) {
  return [query, payload];
}

/**
 * 在关联处理器 delete-in 之前运行
 * @param ids 主键列表
 */
function BeforeDeleteIn(ids) {
  return [ids];
}

/**
 * 在关联处理器 delete-where 之前运行
 * @param query 查询条件
 */
function BeforeDeleteWhere(query) {
  return [query];
}
```

#### After Hook

在关联处理器之后运行，一般用于处理结果集数据。

```jsonc
{
  "name": "::Pet Admin Bind Table",
  "action": {
    "bind": { "model": "pet" },
    "after:search": "scripts.pet.AfterSearch" // 设定 Hook 处理器
  }
}
```

/data/app/scripts/pet.js Hook 脚本

```javascript
/**
 * 在关联处理器 search 之后运行
 * @param result 处理器运行结果
 */
function AfterSearch(result) {
  return result;
}

/**
 * 在关联处理器 get 之后运行
 * @param result 处理器运行结果
 */
function AfterGet(result) {
  return result;
}

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

/**
 * 在关联处理器 insert 之后运行
 * @param result 处理器运行结果
 */
function AfterInsert(result) {
  return result;
}

/**
 * 在关联处理器 update-in 之后运行
 * @param result 处理器运行结果
 */
function AfterUpdateIn(result) {
  return result;
}

/**
 * 在关联处理器 update-where 之后运行
 * @param result 处理器运行结果
 */
function AfterUpdateWhere(result) {
  return result;
}

/**
 * 在关联处理器 delete-in 之后运行
 * @param result 处理器运行结果
 */
function AfterDeleteIn(result) {
  return result;
}

/**
 * 在关联处理器 delete-where 之后运行
 * @param result 处理器运行结果
 */
function AfterDeleteWhere(result) {
  return result;
}
```

### layout Object

表格界面布局。显示字段、筛选器、批量编辑等

| 字段    | 类型   | 必填项 | 默认值 | 示例                             | 说明                                       |
| ------- | ------ | ------ | ------ | -------------------------------- | ------------------------------------------ |
| primary | String | 是     |        | `user_id`                        | 数据主键                                   |
| header  | Object | 是     |        | [查看详情](#layoutheader-object) | 表格界面头部布局。设置批量操作、导入配置等 |
| filter  | Object | 是     |        | [查看详情](#layoutfilter-object) | 表格筛选器。设置筛选条件和右上角操作按钮等 |
| table   | Object | 是     |        | [查看详情](#layouttable-object)  | 表格布局。设置显示列，行操作按钮等         |

#### layout.header Object

表格界面头部布局。设置批量操作、导入配置等

| 字段    | 类型   | 必填项 | 默认值 | 示例 | 说明                 |
| ------- | ------ | ------ | ------ | ---- | -------------------- |
| preset  | Object | 是     |        |      | 批量操作、导入配置等 |
| actions | Array  |        |        |      | 自定义操作按钮       |

```jsonc
{
  "preset": {
    // 批量操作设定
    "batch": {
      // 可批量操作的字段
      "columns": [
        { "name": "名称", "width": 12 }, // name: fields.table 中定义的字段名称; width: 字段宽度, 24 栅格
        { "name": "消费金额", "width": 12 },
        { "name": "入院状态", "width": 12 }
      ],
      "deletable": true // 批量删除按钮
    },

    // 关联数据导入项
    "import": {
      "name": "pet", // Import Widget ID
      "actions": [
        {
          "title": "跳转",
          "icon": "icon-airplay", // 按钮图标, 可用图标 https://feathericons.com/

          // 按钮响应操作 KEY: 执行动作, VALUE: 参数表
          "action": {
            "History.push": { "payload": "/404" }
          }
        }
      ] // 数据导入界面操作按钮链接
    }
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

表格筛选器。设置筛选条件和右上角操作按钮等

| 字段    | 类型  | 必填项 | 默认值 | 示例 | 说明                                            |
| ------- | ----- | ------ | ------ | ---- | ----------------------------------------------- |
| columns | Array |        |        |      | 筛选条件, 在 fields.filter 中定义的筛选条件字段 |
| actions | Array |        |        |      | 自定义操作按钮(界面右上方)                      |

```jsonc
{
  // 支持筛选的字段清单
  "columns": [
    { "name": "名称", "width": 4 }, // name: fields.filter 中定义的字段名称; width: 字段宽度, 24 栅格
    { "name": "状态", "width": 4 }
  ],

  // 自定义操作按钮
  "actions": [
    {
      "title": "添加宠物", // 按钮名称
      "icon": "icon-plus", // 按钮图标, 可用图标 https://feathericons.com/
      "width": 3, // 操作按钮宽度, 24 栅格

      // 按钮响应操作 KEY: 执行动作, VALUE: 参数表
      "action": {
        "Common.openModal": {
          "width": 640,
          "Form": { "type": "edit", "model": "pet" }
        }
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

| KEY 执行动作     | VALUE 参数                                                                                           | 说明                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Common.openModal | `{"width":<窗体宽度>, "Form": { "type":"<表单呈现方式 edit \| view>", "model":"<Form Widget ID>"} }` | 打开表单模态窗                          |
| Service.<名称>   | `{ "method": "<函数名>", "args": [<参数表>] }`                                                       | 调用云函数                              |
| Studio.<名称>    | `{ "method": "<函数名>", "args": [<参数表>] }`                                                       | 调用 Studio 云函数 **仅开发模式下有效** |
| ....             | ...                                                                                                  | ...                                     |

#### layout.table Object

表格布局。设置显示列，行操作按钮等

| 字段      | 类型   | 必填项 | 默认值 | 示例 | 说明             |
| --------- | ------ | ------ | ------ | ---- | ---------------- |
| columns   | Array  | 是     |        |      | 表格列定义       |
| operation | Object |        |        |      | 表格行操作区定义 |

operation Object

| 字段    | 类型    | 必填项 | 默认值  | 示例  | 说明                  |
| ------- | ------- | ------ | ------- | ----- | --------------------- |
| fold    | bool    |        | `false` |       | 是否隐藏行操作区      |
| width   | Integer |        |         | `200` | 行操作区宽度(单位 px) |
| actions | Array   |        |         |       | 自定义行操作按钮      |

```jsonc
{
  "columns": [
    { "name": "名称", "width": 200 }, // name: fields.table 中定义的字段名称; width: 字段宽度, 单位 px
    { "name": "消费金额" },
    { "name": "入院状态" }
  ],
  "operation": {
    "fold": false,
    "width": 255,

    // 行操作按钮
    "actions": [
      {
        "title": "查看", // 按钮名称
        "icon": "icon-eye", // 按钮图标, 可用图标 https://feathericons.com/

        // 按钮响应操作 KEY: 执行动作, VALUE: 参数表
        "action": {
          "Common.openModal": {
            "width": 640,
            "Form": { "type": "view", "model": "pet" }
          }
        }
      },
      {
        "title": "治愈 {{name}}", // 使用 {{<字段名称>}} 引用表单数据
        "icon": "icon-check",
        "action": {
          "Table.save": { "id": ":id", "status": "cured" }
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
}
```

**可用自定义操作 actions[*].action**

| KEY 执行动作     | VALUE 参数                                                                                           | 说明                                    |
| ---------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Common.openModal | `{"width":<窗体宽度>, "Form": { "type":"<表单呈现方式 edit \| view>", "model":"<Form Widget ID>"} }` | 打开表单模态窗                          |
| Table.Save       | `{ "id": ":id", "status": "cured" }`                                                                 | 保存当前行数据                          |
| Table.Delete     | `{ "id": ":id"}`                                                                                     | 删除当前行数据                          |
| Service.<名称>   | `{ "method": "<函数名>", "args": [<参数表>] }`                                                       | 调用云函数                              |
| Studio.<名称>    | `{ "method": "<函数名>", "args": [<参数表>] }`                                                       | 调用 Studio 云函数 **仅开发模式下有效** |
| ....             | ...                                                                                                  | ...                                     |

### fields Object

表格字段定义。指定表格列字段, 表格筛选器字段定义

| 字段   | 类型   | 必填项 | 默认值 | 示例                             | 说明               |
| ------ | ------ | ------ | ------ | -------------------------------- | ------------------ |
| filter | Object | 是     |        | [查看详情](#fieldsfilter-object) | 表格筛选器字段定义 |
| table  | Object | 是     |        | [查看详情](#fieldstable-object)  | 表格列字段定义     |

#### fields.filter Object

表格筛选器字段定义

KEY: 筛选器字段名称, VALUE: 字段定义

```jsonc
{
  "医生": {
    "bind": "where.doctor_id.eq", // query 名称, 例: /api/__yao/table/pet/search?where.doctor_id.eq=xxx

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

#### fields.table Object

表格列字段定义

KEY: 表格列字段名称, VALUE: 字段定义

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
    "view": { "type": "Text" },
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

在 edit.props 和 view.props 中使用动态数据

...

[内建 Compute 处理器](../处理器/Compute.mdx)

### config Object

表格界面配置项。表格满屏显示等配置

| 字段 | 类型    | 必填项 | 默认值 | 示例    | 说明             |
| ---- | ------- | ------ | ------ | ------- | ---------------- |
| full | Boolean | 否     | `true` | `false` | 是否满屏显示表格 |

## API

Table Widget API

| 请求方式 | 路由                                            | 鉴权               | query                                   | payload                                                                                | 说明                                                                |
| -------- | ----------------------------------------------- | ------------------ | --------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `GET`    | `/api/__yao/table/:id/setting`                  | `关联处理器中指定` |                                         |                                                                                        | 获取表格配置信息                                                    |
| `GET`    | `/api/__yao/table/:id/component/:xpath/:method` | `JWT`              |                                         |                                                                                        | 返回 `fields.table\|filter.<key>.props.$xxx` 绑定处理器运行结果     |
| `GET`    | `/api/__yao/table/:id/search`                   | `关联处理器中指定` | [URL Query Params](../Widgets/API.mdx)  |                                                                                        | 按条件查询，返回带有分页信息和记录数组                              |
| `GET`    | `/api/__yao/table/:id/get`                      | `关联处理器中指定` | [URL Query Params](../Widgets/API.mdx)  |                                                                                        | 按条件查询，返回记录数组                                            |
| `GET`    | `/api/__yao/table/:id/find/:primary`            | `关联处理器中指定` | [URL Query Params](../Widgets/API.mdx)  |                                                                                        | 按主键查询单条记录，返回单条记录                                    |
| `GET`    | `/api/__yao/table/:id/download/:field`          | `JWT`              | `{"name":"<file name>", "token":"JWT"}` |                                                                                        | 文件下载 返回 `{"content":"<文件内容>", "type":"<文件 Mime Type>"}` |
| `POST`   | `/api/__yao/table/:id/upload/:xpath/:method`    | `JWT`              |                                         | `{"file":"<file content>"}`                                                            | 文件上传 `fields.table.<key>.props.$api`                            |
| `POST`   | `/api/__yao/table/:id/save`                     | `关联处理器中指定` |                                         | `{"<field>":"<value>"}`                                                                | 保存单条记录，如 payload 中包含主键则更新，否则创建                 |
| `POST`   | `/api/__yao/table/:id/create`                   | `关联处理器中指定` |                                         | `{"<field>":"<value>"}`                                                                | 创建一条记录                                                        |
| `POST`   | `/api/__yao/table/:id/insert`                   | `关联处理器中指定` |                                         | `{"columns":["f1", "f2">", "values":[["<f1_v1>", "<f2_v1>"],["<f1_v2>", "<f2_v2>"]]]}` | 创建多条一条记录                                                    |
| `POST`   | `/api/__yao/table/:id/update/:primary`          | `关联处理器中指定` |                                         | `{"<field>":"<value>"}`                                                                | 更新指定主键的记录                                                  |
| `POST`   | `/api/__yao/table/:id/update/where`             | `关联处理器中指定` | [URL Query Params](../Widgets/API.mdx)  | `{"<field>":"<value>"}`                                                                | 更新符合查询条件记录                                                |
| `POST`   | `/api/__yao/table/:id/update/in`                | `关联处理器中指定` | `ids=1,2,3,4`                           | `{"<field>":"<value>"}`                                                                | 按主键批量更新记录                                                  |
| `POST`   | `/api/__yao/table/:id/delete/:primary`          | `关联处理器中指定` |                                         | `{"<field>":"<value>"}`                                                                | 删除指定主键的记录                                                  |
| `POST`   | `/api/__yao/table/:id/delete/where`             | `关联处理器中指定` | [URL Query Params](../Widgets/API.mdx)  |                                                                                        | 查询符合查询条件记录                                                |
| `POST`   | `/api/__yao/table/:id/delete/in`                | `关联处理器中指定` | `ids=1,2,3,4`                           |                                                                                        | 按主键批量删除记录                                                  |

## 处理器

Table Widget 处理器

| 处理器                | 参数表                                                  | 返回值                     | 说明                                                           |
| --------------------- | ------------------------------------------------------- | -------------------------- | -------------------------------------------------------------- |
| yao.table.Setting     | `[<Widget ID>]`                                         | 返回表格配置               | 返回表格 DSL 信息                                              |
| yao.table.Xgen        | `[<Widget ID>]`                                         | 返回表格配置               | 返回表格配置信息, 用于 XGEN 界面引擎页面渲染                   |
| yao.table.Search      | `[<Widget ID>, <查询参数>, <当前页码>, <每页显示记录>]` | 返回带有分页信息和记录数组 | 调用关联处理器，查询表格数据列表                               |
| yao.table.Get         | `[<Widget ID>, <查询参数>]`                             | 返回记录数组               | 调用关联处理器，查询表格数据列表                               |
| yao.table.Find        | `[<Widget ID>, <主键>,<查询参数>]`                      | 返回记录                   | 调用关联处理器，按主键查询表格数据详情                         |
| yao.table.Save        | `[<Widget ID>, <记录>]`                                 | 主键                       | 调用关联处理器，保存一条数据记录，参数包含主键则更新，否则创建 |
| yao.table.Create      | `[<Widget ID>, <记录>]`                                 | 主键                       | 调用关联处理器，创建数据记录                                   |
| yao.table.Delete      | `[<Widget ID>, <主键>]`                                 | 返回记录                   | 调用关联处理器，按主键删除记录                                 |
| yao.table.Insert      | `[<Widget ID>, <字段名称数组>, <二维记录值数组>]`       | 主键                       | 调用关联处理器，插入多条记录                                   |
| yao.table.Update      | `[<Widget ID>, <主键>,<记录>]`                          | 返回更新行                 | 调用关联处理器，更新单条记录                                   |
| yao.table.UpdateWhere | `[<Widget ID>, <查询参数>,<记录>]`                      | 返回更新行                 | 调用关联处理器，更新符合查询条件记录                           |
| yao.table.UpdateIn    | `[<Widget ID>, <主键数组>,<记录>]`                      | 返回更新行                 | 调用关联处理器，更新指定主键的数据记录                         |
| yao.table.DeleteWhere | `[<Widget ID>, <查询参数>]`                             | 返回更新行                 | 调用关联处理器，删除符合查询条件记录                           |
| yao.table.DeleteIn    | `[<Widget ID>, <主键数组>]`                             | 返回更新行                 | 调用关联处理器，删除指定主键的数据记录                         |
| yao.table.Export      | `[<Widget ID>, <查询参数>, <每批次处理数量>]`           | 返回 Excel 文件名称        | 调用关联处理器，导出 Excel 文件, 保存到 `/data/app/data` 目录  |
