# 查询数据

<blockquote>
  <p>常规的数据CURD查询，可以使用数据模型的处理器实现。</p>
  <p>
    数据聚合统计等复杂的场景，或者需要对接数据仓库，可以在数据流中使用 Query DSL
    (Domain Specific Language) 实现。
  </p>
</blockquote>

## 使用数据模型处理器

编写数据流描述文件 `query.flow.json`，并放置在应用的 `flows` 目录中。

```json
{
  "label": "宠物",
  "version": "1.0.0",
  "description": "数据查询",
  "nodes": [
    {
      "name": "列表",
      "process": "models.pet.Get",
      "args": [
        {
          "select": ["id", "name", "remark"],
          "wheres": [{ "column": "name", "value": "猫" }],
          "limit": 3
        }
      ]
    },
    {
      "name": "分页",
      "process": "models.pet.Paginate",
      "args": [
        {
          "select": ["id", "name", "remark"],
          "wheres": [{ "column": "name", "value": "猫" }],
          "limit": 1
        },
        1,
        3
      ]
    },
    {
      "name": "一条记录",
      "process": "models.pet.Find",
      "args": [1, { "select": ["id", "name", "remark"] }]
    },
    {
      "name": "更新记录",
      "process": "models.pet.Update",
      "args": [1, { "name": "这是一只懒猫" }]
    },
    {
      "name": "插入记录",
      "process": "models.pet.Save",
      "args": [{ "name": "哮天犬", "amount": "2000", "remark": "新成员" }]
    },
    {
      "name": "删除记录",
      "process": "models.pet.Delete",
      "args": [1]
    }
  ],
  "output": "{{$res}}"
}
```

**运行数据流**

```bash
yao run flows.query
```

**在 JS 文件中使用**

获取多条

```json
  Process("models.pet.Get", {
    wheres: [{ column: "name", value: "cat", op: "=" }],
    limit: 1,
  });
```

获取 1 条，id 为 1 的数据

```json
  Process("models.pet.find", 1,{});
```

保存数据

```json
  Process("models.pet.save",{
    id:1,
    name:"cats foo bar"
  });
```

删除数据

```json
  Process("models.pet.delete",1,{});

```

扩展阅读:

<Extend
  title="数据模型文档"
  desc="了解数据模型的查询条件设定方式"
  link="f.参考手册/b.数据模型"
></Extend>

<Extend
  title="数据模型关联"
  desc="了解如何设置数据模型间的关联，并进行关联查询。"
  link="c.高级特性/b.数据模型关联"
></Extend>

<Extend
  title="数据模型处理器"
  desc="了解更多数据模型操作处理器。"
  link="d.处理器/b.数据模型"
></Extend>

## 使用 Query DSL 查询

Yao 提供以下 Query DSL, 可以在数据流节点中使用:

| DSL           | 说明                                                                                                                                |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Gou Query DSL | 适用基于 SQL 的查询数据引擎。 <a href="https://yaoapps.com/doc/f.%E5%8F%82%E8%80%83%E6%89%8B%E5%86%8C/e.Query%20DSL"> 查看文档 </a> |
| Tai Query DSL | 适用基于 ElasticSearch 的数据引擎。<strong>(内测中暂未开放)</strong>                                                                |

编写数据流描述文件 `stat.flow.json`，并放置在应用的 `flows` 目录中。

```json
{
  "label": "宠物统计",
  "version": "1.0.0",
  "description": "宠物统计",
  "nodes": [
    {
      "name": "类型统计S1",
      "engine": "xiang",
      "query": {
        "select": [":COUNT(id) as 数量", "name as 名字"],
        "groups": "名字",
        "from": "$pet"
      }
    },
    {
      "name": "类型统计S2",
      "engine": "xiang",
      "query": {
        "select": [":SUM(amount) as 金额", "name as 名字"],
        "groups": "名字",
        "from": "$pet"
      }
    }
  ],
  "output": "{{$res}}"
}
```

| 字段   | 说明                                                |
| ------ | --------------------------------------------------- |
| engine | 数据引擎名称， `xiang` 使用数据模型存储的数据源连接 |
| query  | Query DSL，根据数据源连接类型，编写对应的查询逻辑   |

**运行数据流**

```bash
yao run flows.stat
```

扩展阅读:

<Extend
  title="复杂数据查询"
  desc="了解更多复杂数据查询方式。"
  link="c.高级特性/c.复杂数据查询"
></Extend>

<Extend
  title="Gou Query DSL 文档"
  desc="Gou Query DSL 使用文档"
  link="f.参考手册/e.Query%20DSL"
></Extend>

## 推荐阅读

接下来，建议学习以下章节:

<Extend
  title="数据流使用JS"
  desc="了解如何在数据流中使用JS脚本处理查询结果。"
  link="c.高级特性/a.数据流使用JS"
></Extend>

<Div style={{ display: "flex", justifyContent: "space-between" }}>
  <Link type="prev" title="编写数据流" link="b.基础特性/e.编写数据流"></Link>
  <Link
    type="next"
    title="数据流使用JS"
    link="c.高级特性/a.数据流使用JS"
  ></Link>
</Div>
