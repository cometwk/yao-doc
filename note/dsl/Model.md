# 数据模型

## 概述

Yao 可以读取数据模型定义，实现数据迁移、元数据原子操作、元数据输入校验和元数据管理后台。元数据原子操作方法被映射为处理器(`process`)，支持模型间数据关系映射，可在数据流（`Flow`）和接口(`API`)中访问查询。如采用`golang`语言开发业务插件(`Plugin`)，可以使用 Package `Gou` 访问模型的各个方法, 后续将提供 `NodeJS` 等语言 SDK。一个数据模型对应数据库中的一张数据表, 通过 JSON 文件描述数据表结构，放置在`models` 目录中。使用 `yao migrate` 命令创建/更新数据表结构设计。

[简单示例](model/simple.json ':include :type=code')

查看 [完整示例](#完整示例)

## 处理器列表

[简单示例](model/process.md ':include')

## 命名规范

数据模型描述文件是以 **小写英文字母** 命名的 JSON 文本文件 `<name>.mod.json`

| 文件夹 (相对应用模型根目录) | 文件名        | 模型名称             | Process (在 API /Flow 中引用)         |
| --------------------------- | ------------- | -------------------- | ------------------------------------- |
| /                           | name.mod.json | `name`               | `models.name.<process>`               |
| /group/                     | name.mod.json | `gorup.name`         | `models.gorup.name.<process>`         |
| /group1/group2/             | name.mod.json | `gorup1.gorup2.name` | `models.gorup1.group2.name.<process>` |

## 文档结构

```typescript
interface DSL {
  name?: string; // 元数据名称
  connector?: string; // 数据库 sqlite or mysql
  table?: Table; // 数据表选项
  columns?: Column[]; // 字段定义
  indexes?: Index[]; // 索引定义
  relations?: Record<string, Relation>; // 映射关系定义
  values?: Record<string, any>[]; // 初始数值
  option?: Option; // 元数据配置
}
```

| 字段      | 类型                  | 说明         | 必填项 |
| --------- | --------------------- | ------------ | ------ |
| name      | String                | 模型中文名称 | 是     |
| table     | Object                | 数据表定义   | 是     |
| columns   | Array\<Object\>       | 字段定义     | 是     |
| indexes   | Array\<Object\>       | 索引定义     | 是     |
| relations | \[key:String\]:Object | 关系映射     | 否     |
| values    | Array\<Object\>       | 默认数据     | 否     |
| option    | Object                | 配置选型     | 否     |

## `table`

```ts
// Table the model mapping table in DB
interface Table {
  name?: string; // 若未设置, 根据model.name 自动产生. 例如 model.name= name.space.user, 则, 表名: name_space_user
  prefix?: string; // optional, the table prefix
  comment?: string;
  engine?: string; // InnoDB,MyISAM ( MySQL Only )
  collation?: string;
  charset?: string;
  primarykeys?: string[];
}
```

定义模型存储在数据库中的数据表名称、注释等信息。
支持 `MySQL`, `PostgreSQL`、`SQLite`等 `Xun Database` 或第三方提供驱动的数据库。

```json
{
  "table": {
    "name": "user",
    "comment": "用户表",
    "engine": "InnoDB"
  }
}
```

| 字段    | 类型   | 说明                                              | 必填项 |
| ------- | ------ | ------------------------------------------------- | ------ |
| name    | String | 数据表名称                                        | 是     |
| comment | String | 数据表注释中文名                                  | 否     |
| engine  | String | 数据表引擎（MySQL ONLY) 许可值 `InnoDB`, `MyISAM` | 否     |

## `columns` 字段

一个模型可以包含多个字段定义，每个字段定义包含 `label`、`name`、`type`、 `validations` 等信息。

**示例**

[columns.json](model/columns.json ':include :type=code')

**说明**

[字段说明](model/columns.md ':include')

### 字段类型

[field_type.md](model/field_type.md ':include')

### 字段校验

一个字段可以包含多条校验规则，每条校验规则可以选用 `min`,`max`, `pattern`, `typeof` 等校验方法。

```json
{
  "columns": [
    {
      "label": "手机号",
      "name": "mobile",
      "type": "string",
      "length": 50,
      "comment": "手机号",
      "index": true,
      "crypt": "AES",
      "validations": [
        {
          "method": "typeof",
          "args": ["string"],
          "message": "{{input}}类型错误, {{label}}应该为字符串"
        },
        {
          "method": "pattern",
          "args": ["^1[3-9]\\d{9}$"],
          "message": "{{input}}格式错误"
        }
      ]
    }
  ]
}
```

**校验规则定义**

| 字段    | 类型                            | 说明                                                                                                                                                  | 必填项 |
| ------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| method  | String                          | 校验方法名称，可选值 `typeof`, `pattern` 等                                                                                                           | 是     |
| args    | Array\<String\|Integer\|Float\> | 校验方法参数，例如 `[20]`, `["^1[3-9]\\d{9}$"]`                                                                                                       | 否     |
| message | String                          | 如校验不通过，返回的错误提示。支持使用 `{{<name>}}` 引用字段信息, 如`{{label}}`将被替换为字段 `label`中定义的数值; `{{input}}` 被替换为用户输入数值。 | 否     |

**校验方法**

[校验方法](model/validate.md ':include')

### 加密方式

当前支持 `AES` 和 `PASSWORD` 两种字段数值加密存储算法，其中 `AES` 仅支持 MySQL 数据库。

| 加密算法   | 说明                               | 是否可逆 |
| ---------- | ---------------------------------- | -------- |
| `AES`      | AES 加密，需设定 `XIANG_DB_AESKEY` | 是       |
| `PASSWORD` | PASSWORD HASH 加密                 | 否       |

### 保留字

以下名称不能用于字段名称。

| 保留字           | 说明                         |
| ---------------- | ---------------------------- |
| created_at       | 用于记录创建时间戳           |
| updated_at       | 用于记录更新时间戳           |
| deleted_at       | 用于记录软删除标记           |
| \_\_restore_data | 用于软删除时备份唯一字段数值 |

## `indexes` 索引

一个数据模型，可以包含多个索引。对于单一索引，推荐在字段定义时，使用 `index` 、 `unique` 和 `primary` 修饰符定义，对于复合索引或全文检索索引，在 `indexes` 中定义。

```json
{
  "indexes": [
    {
      "comment": "厂商用户",
      "name": "manu_id_mobile_unique",
      "columns": ["manu_id", "mobile"],
      "type": "unique"
    },
    {
      "comment": "简历全文检索",
      "name": "resume_fulltext",
      "columns": ["resume"],
      "type": "fulltext"
    }
  ]
}
```

| 字段    | 类型            | 说明                                                                                 | 必填项 |
| ------- | --------------- | ------------------------------------------------------------------------------------ | ------ |
| name    | String          | 索引名称。**命名规范为 字段 1\_字段 2\_字段 n\_索引类型**                            | 是     |
| type    | String          | 索引类型 许可值 `index` 索引, `unique` 唯一索引, `primary` 主键, `fulltext` 全文检索 | 是     |
| columns | Array\<String\> | 关联字段名称列表（顺序有关) `["字段 1","字段 2"]` 与 `["字段 2","字段 1"]` 不同      | 是     |
| comment | String          | 索引注释                                                                             | 否     |

## `relations` 关联

数据模型支持一对一、一对多两种关系映射，可以通过定义映射关系将多个数据模型关联，查询时使用`with`参数即可同时返回关联模型数据。

| 映射关系名称 | 关系   | 说明                           |
| ------------ | ------ | ------------------------------ |
| `hasOne`     | 一对一 | 模型 A 与模型 B 通过一对一关联 |
| `hasMany`    | 一对多 | 模型 A 与模型 B 通过一对多关联 |

关联关系使用 `[key:String]:Object Relation` 数据结构定义 ( `{"关联名称1":{}, "关联名称2":{}}`, 关联名称为 **小写英文字母** )

在模型文件 `user.json` 中定义

<Detail title="查看源码">

```json
{
  "relations": {
    "manu": {
      "type": "hasOne",
      "model": "manu",
      "key": "id",
      "foreign": "manu_id",
      "query": { "select": ["name", "short_name", "type"] }
    },
    "addresses": {
      "type": "hasMany",
      "model": "address",
      "key": "user_id",
      "foreign": "id",
      "query": {
        "select": ["province", "city", "location", "status"],
        "pagesize": 20
      }
    },
    "mother": {
      "type": "hasOneThrough",
      "links": [
        {
          "type": "hasOne",
          "model": "friends",
          "key": "user_id",
          "foreign": "user.id",
          "query": {
            "select": ["status", "type", "friend_id"],
            "wheres": [
              {
                "column": "type",
                "value": "monther"
              }
            ]
          }
        },
        {
          "type": "hasOne",
          "model": "user",
          "key": "id",
          "foreign": "user_mother_friends.friend_id",
          "query": {
            "select": ["name", "id", "status", "type", "secret", "extra"],
            "withs": {
              "manu": {},
              "roles": {},
              "address": {}
            }
          }
        }
      ]
    },
    "roles": {
      "type": "hasManyThrough",
      "links": [
        {
          "type": "hasMany",
          "model": "user_roles",
          "key": "user_id",
          "foreign": "id",
          "query": {
            "select": ["status"],
            "pagesize": 20
          }
        },
        {
          "type": "hasOne",
          "model": "role",
          "key": "id",
          "foreign": "role_id",
          "query": {
            "select": ["name", "label", "permission"]
          }
        }
      ]
    }
  }
}
```

</Detail>

**`Object Relation`**

| 字段    | 类型                     | 说明                                                                             | 必填项 |
| ------- | ------------------------ | -------------------------------------------------------------------------------- | ------ |
| type    | String                   | 关系类型 许可值 `hasOne`, `hasOneThrough` , `hasMany` , `hasManyThrough`         | 是     |
| key     | String                   | 关联模型的关联字段名称                                                           | 否     |
| model   | String                   | 关联模型名称                                                                     | 否     |
| foreign | String                   | 当前模型的关联字段名称                                                           | 否     |
| query   | Object QueryParam        | 关系查询参数默认值。如在查询时未指定关联查询参数，则替使用在模型中定义的查询参数 | 否     |
| links   | Array\<Object Relation\> | `hasOneThrough` 或 `hasManyThrough` 多表关联关系定义                             | 否     |

#### `hasOne` 一对一

[hasOne.md](model/hasOne.md ':include')

#### `hasMany` 一对多

数据模型 `user` 数据表结构如下:

| 字段    | 类型       | 说明        |
| ------- | ---------- | ----------- |
| id      | ID         | 用户 ID     |
| manu_id | bigInteger | 所属厂商 ID |
| name    | string     | 姓名        |

数据模型 `address` 数据表结构如下:

| 字段     | 类型       | 说明                          |
| -------- | ---------- | ----------------------------- |
| id       | ID         | 地址 ID                       |
| user_id  | bigInteger | 所属用户 ID (关联 `user.id` ) |
| location | string     | 详细地址                      |

对于类似一个用户有多个通信地址的业务场景，可以通过建立一对多的映射关系来实现。

在模型文件 `user.json` 中定义

```json
{
  "name": "用户",
  "relations": {
    "addresses": {
      "type": "hasMany",
      "model": "address",
      "key": "user_id",
      "foreign": "id",
      "query": {
        "select": ["location"],
        "limit": 20
      }
    }
  }
}
```

**说明**

1.将关系映射类型指定为 `hasMany`

2.将关联模型 `model` 设置为 `address`

3.将关联模型 `key` 设置为 `user_id`, 即：`address.user_id` 引擎处理时，自动关联 `address` 表的 `user_id` 字段。

4.将 `foreign` 设置为 `id`, 即: `user.id` 引擎处理时，将 `user.id` 和 `address.user_id` 关联

5.可以在 `query` 字段中，设置默认的查询条件，如指定读取的字段等。对于 `hasMany` 建议设置默认 `limit` 约束返回数据条目

对于 `hasMany` 类型关系映射，引擎将分两次查询。首次查询出主模型以及关联的 ID 列表，第二次根据 ID 列表，查询关联数据信息。

第一次查询：

```sql
SELECT `user`.* FROM `user` AS `user`
```

引擎处理结果，并读取 `user`.`id`

第二次查询:

```sql
SELECT  `address`.`user_id`, `address`.`location` FROM `address` AS `address`
  WHERE `address`.`user_id` IN (<user.id...>)
```

引擎处理结果，关联用户地址信息

**访问**

在调用 `process` 查询时，传入 `with` 参数，即可同时取得 `addresses` 的关联信息

```bash
GET  /api/user/find/1?with=addresses
```

## `option` 杂项

在 `option` 中设定模型配置参数

```json
{
  "name": "地址",
  "option": {
    "timestamps": true,
    "soft_deletes": true
  }
}
```

| 选项         | 类型 | 说明                                                                                                                                  |
| ------------ | ---- | ------------------------------------------------------------------------------------------------------------------------------------- |
| timestamps   | Bool | 为 true 时， 自动创建 `created_at`、`updated_at` 字段，并在插入和更新数据时，标记对应操作时间                                         |
| soft_deletes | Bool | 为 true 时， 自动创建 `deleted_at` 和 `__restore_data` 字段，数据删除时，备份唯一字段数据，并标记操作时间，查询时忽略已标记删除的数据 |

## `QueryParam` 查询参数 

在模型关联关系定义和调用处理器时，通过 Object `QueryParam` 描述查询条件。

```json
{
  "select": ["id", "name", "mobile", "status"],
  "withs": {
    "manu": {
      "query": {
        "select": ["name", "short_name", "status"]
      }
    },
    "addresses": {}
  },
  "wheres": [
    { "column": "status", "value": "enabled" },
    { "rel": "manu", "column": "status", "value": "enabled" },
    {
      "wheres": [
        { "column": "name", "value": "%张三%", "op": "like" },
        {
          "method": "orwhere",
          "column": "name",
          "value": "%李四%",
          "op": "like"
        }
      ]
    }
  ],
  "orders": [
    { "column": "id", "option": "desc" },
    { "rel": "manu", "column": "name" }
  ],
  "limit": 2
}
```

应用引擎将以上查询条件解析为如下 SQL :

```SQL
SELECT
  `user`.`id`,`user`.`name`,`user`.`mobile`,`user`.`status`,
  `user_manu`.`name` AS `user_manu_name`,
  `user_manu`.`short_name` AS `user_manu_short_name` ,
  `user_manu`.`status` AS `user_manu_status`
FROM `user` AS `user`
LEFT JOIN `manu` AS `user_manu` ON `user_manu`.`id` = `user`.`manu_id`
WHERE  `user`.`status` = 'enabled'
AND `user_manu`.`status` = 'enabled'
AND (
   `user`.`name` like '%张三%' OR `user`.`name` like '%李四%'
)
ORDER BY `user`.`id` desc, `user_manu`.`name` asc
LIMIT 2
```

### 数据结构

**`QueryParam`**

| 字段     | 类型                       | 说明             | 必填项 |
| -------- | -------------------------- | ---------------- | ------ |
| select   | Array\<String\>            | 选择字段清单     | 否     |
| wheres   | Array\<Object Where\>      | 查询条件         | 否     |
| orders   | Array\<Object Order\>      | 排序条件         | 否     |
| limit    | Integer                    | 返回记录条目     | 否     |
| page     | Integer                    | 当前页码         | 否     |
| pagesize | Integer                    | 每页显示记录数量 | 否     |
| withs    | `[key:String]:Object With` | 读取关联模型     | 否     |

**`Object Where`**

| 字段   | 类型                  | 说明                                       | 必填项 |
| ------ | --------------------- | ------------------------------------------ | ------ |
| rel    | String                | 如按关联模型的字段查询，则填写关联模型名称 | 否     |
| column | String                | 字段名称                                   | 否     |
| method | String                | 查询方法 `where`,`orwhere`                 | 否     |
| op     | String                | 匹配关系 `eq`,`like`,`in`,`gt` 等          | 否     |
| value  | Any                   | 匹配数值                                   | 否     |
| wheres | Array\<Object Where\> | 分组查询                                   | 否     |

| 查询方法 | 说明                                  |
| -------- | ------------------------------------- |
| where    | WHERE 字段 = 数值, WHERE 字段 >= 数值 |
| orwhere  | ... OR WHERE 字段 = 数值              |

| 匹配关系 | 说明                             |
| -------- | -------------------------------- |
| eq       | 默认值 等于 WHERE 字段 = 数值    |
| like     | 匹配 WHERE 字段 like 数值        |
| gt       | 大于 WHERE 字段 > 数值           |
| ge       | 大于等于 WHERE 字段 >= 数值      |
| lt       | 小于 WHERE 字段 < 数值           |
| le       | 小于等于 WHERE 字段 <= 数值      |
| null     | 为空 WHERE 字段 IS NULL          |
| notnull  | 不为空 WHERE 字段 IS NOT NULL    |
| in       | 列表包含 WHERE 字段 IN (数值...) |

**`Object Order`**

| 字段   | 类型   | 说明                                       | 必填项 |
| ------ | ------ | ------------------------------------------ | ------ |
| rel    | String | 如按关联模型的字段排序，则填写关联模型名称 | 否     |
| column | String | 字段名称                                   | 否     |
| option | String | 排序方式，默认为 asc desc, asc             | 否     |

**`Object With`**

| 字段  | 类型              | 说明         | 必填项 |
| ----- | ----------------- | ------------ | ------ |
| name  | String            | 关联关系名称 | 否     |
| query | Object QueryParam | 查询参数     | 否     |

## 完整示例

[完整示例](model/full.json ':include :type=code')
