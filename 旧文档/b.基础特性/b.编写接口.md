# 编写接口

<blockquote>
  编写 API 接口 JSON 描述文件，将其放置在应用 `apis` 目录中，运行 yao start
  命令启动服务时，引擎将按接口描述的定义，生成 RESTFul API 接口。
</blockquote>

## 接口描述

编写一个接口描述文件 `/apis/pet.http.json`，指定接口路径、请求方式以及绑定的处理器，放置在应用的 `apis` 目录中。

描述文件内容:

```json
{
  "name": "宠物",
  "version": "1.0.0",
  "description": "宠物接口",
  "guard": "bearer-jwt",
  "group": "pet",
  "paths": [
    {
      "path": "/search",
      "method": "GET",
      "guard": "-",
      "process": "models.pet.Paginate",
      "in": [":query-param", "$query.page", "$query.pagesize"],
      "out": {
        "status": 200,
        "type": "application/json"
      }
    },
    {
      "path": "/save",
      "method": "POST",
      "guard": "-",
      "process": "models.pet.Save",
      "in": [":payload"],
      "out": {
        "status": 200,
        "type": "application/json"
      }
    },
    {
      "path": "/update/:id",
      "method": "PATCH",
      "guard": "-",
      "process": "models.pet.Update",
      "in": ["$params.id", ":payload"],
      "out": {
        "status": 200,
        "type": "application/json"
      }
    },
    {
      "path": "/delete/:id",
      "method": "DELETE",
      "guard": "-",
      "process": "models.pet.Delete",
      "in": ["$params.id"],
      "out": {
        "status": 200,
        "type": "application/json"
      }
    }
  ]
}
```

应用目录结构:

```bash
├── apis        # 用于存放接口描述文件
│   └── pet.http.json
├── models        # 用于存放数据模型描述文件
│   └── pet.mod.json
├── db
└── ui
└── app.json
```

## Start 启动服务

```bash
cd /data/app
yao start
```

<Extend
  title="命令行工具"
  desc="命令行工具完整文档"
  link="f.参考手册/a.yao%20命令"
></Extend>

## 接口调试

使用 `curl` 或 `Postman` 等接工具口调试，访问接口调试。

分页查询接口

```bash
 curl 'http://127.0.0.1:5099/api/pet/search?where.name.match=Cookie&page=1&pagesize=1'
```

保存数据接口

```bash
curl -X POST http://127.0.0.1:5099/api/pet/save
   -H 'Content-Type: application/json'
   -d '{"sn":"300001", "name":"旺旺", "type":"狗", "desc":"新成员"}'
```

## 推荐阅读

接下来，建议学习以下章节:

<Extend
  title="描述界面"
  desc="了解如何制作一个数据操作 CURD 界面。"
  link="b.基础特性/c.描述界面"
></Extend>

<Div style={{ display: "flex", justifyContent: "space-between" }}>
  <Link
    type="prev"
    title="创建数据模型"
    link="b.基础特性/a.创建数据模型"
  ></Link>
  <Link type="next" title="描述界面" link="b.基础特性/c.描述界面"></Link>
</Div>
