# 创建数据模型

<blockquote>
  一个数据模型对应数据库中的一张数据表, 通过 JSON 文件描述数据表结构，放置在
  models 目录中。使用 yao migrate 命令创建/更新数据表结构设计。
</blockquote>

## 数据模型描述

编写一个数据模型描述文件 `pet.mod.json`，并放置在应用的 `models` 目录中。

描述文件内容:

```json
{
  "name": "宠物模型",
  "table": { "name": "pet", "comment": "宠物模型" },
  "columns": [
    {
      "label": "ID",
      "name": "id",
      "type": "ID",
      "comment": "ID",
      "primary": true
    },
    {
      "label": "日期",
      "name": "day",
      "type": "datetime",
      "index": true
    },
    {
      "label": "名称",
      "name": "name",
      "type": "string",
      "length": 128,
      "index": true
    },
    {
      "label": "状态",
      "name": "status",
      "type": "enum",
      "default": "enabled",
      "option": ["enabled", "disabled"],
      "comment": "状态：enabled打开，disabled关闭",
      "index": true
    },
    {
      "label": "用户id",
      "name": "user_id",
      "type": "integer",
      "index": true
    },
    {
      "label": "总金额",
      "name": "amount",
      "type": "decimal",
      "index": true
    },
    {
      "label": "备注",
      "name": "remark",
      "type": "text",
      "nullable": true
    }
  ],
  "values": [],
  "relations": {
    "users": {
      "type": "hasOne",
      "model": "user",
      "key": "id",
      "foreign": "user_-id",
      "query": {}
    }
  },
  "option": { "timestamps": true, "soft_deletes": true }
}
```

<Notice type="success">
  提示：<strong>option.timestamps</strong> 为 true, 自动创建
  <strong>created_at</strong> 和 <strong>updated_at</strong> 字段, 用于保存数据记录的创建时间和更新时间。
  <strong>option.soft_deletes</strong> 为 true, 自动创建
  <strong>deleted_at</strong> 字段, 用于标记删除记录。详细说明参考数据模型文档。
</Notice>

应用目录结构:

```bash
├── models        # 用于存放数据模型描述文件
│   └── pet.mod.json
├── db
└── ui
└── app.json
```

扩展阅读:

<Extend
  title="数据模型文档"
  desc="了解字段类型、联合索引模型关联关系等定义方式。"
  link="f.参考手册/b.数据模型"
></Extend>

## Migrate 创建/更新数据表

在项目根目录下运行 `Migrate` ，创建/更新数据表结构，并插入默认数据。

```bash
cd /data/app
yao migrate -n pet
```

<Notice type="warning">
  注意：migrate 命令将删除数据库中同名数据表后重新创建，请注意数据备份。
</Notice>

扩展阅读:

<Extend
  title="命令行工具"
  desc="了解 Yao 都有哪些命令，以及这些命令如何使用。"
  link="f.参考手册/a.yao%20命令"
></Extend>

## 数据查询

列表查询

```bash
yao run models.pet.Get '::{}'
```

按主键查询数据

```bash
yao run models.pet.Find 1
```

删除一条数据

```bash
yao run models.pet.Delete 1
```

新增一条数据

```bash
yao run models.pet.Create '::{"name":"cat", "day":"2022-01-01 08:00:00", "status":"enabled", "user_id":1,"amount":1000,"remark":"cat ....."}'
```

更新一条数据

```bash
yao run models.pet.Update 1 '::{"remark":"一只可爱的三色猫"}'
```

保存一条数据，指定主键则更新，不指定创建创建。

```bash
yao run models.pet.Save '::{"name":"cat", "day":"2022-01-01 08:00:00", "status":"enabled", "user_id":1,"amount":1000,"remark":"cat ....."}'
```

```bash
yao run models.pet.Save '::{"id":1,"remark":"一只可爱的三色猫"}'
```

扩展阅读:

<Extend
  title="模型处理器文档"
  desc="数据模型处理器详细文档"
  link="b.基础特性/d.使用处理器"
></Extend>

## 推荐阅读

接下来，建议学习以下章节:

<Extend
  title="编写接口"
  desc="了解如何编写 RESTFul 数据接口"
  link="b.基础特性/b.编写接口"
></Extend>

<Div style={{ display: "flex", justifyContent: "space-between" }}>
  <Link type="prev" title="安装调试" link="a.介绍/b.安装调试"></Link>
  <Link type="next" title="编写接口" link="b.基础特性/b.编写接口"></Link>
</Div>
