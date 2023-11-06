# Widgets 手册

<blockquote>
  <p>
    Widget 抽象出一个功能模块的通用部分,使用 DSL 描述差异,
    实现快速复制，有效提升开发效率。Yao 提供一组内建 Widgets,
    覆盖大部分常用功能。
  </p>
  <p>Widget 支持自定义, 支持使用 Studio 脚本创建实例，可用于自建低代码平台。</p>
</blockquote>

**目录**

| Widget           | 目录(相对应用根目录) | 扩展名        | 说明                                                                                                   |
| ---------------- | -------------------- | ------------- | ------------------------------------------------------------------------------------------------------ |
| App              | `/app.json`          | `-`           | APP Widget 每一个应用只有一个 [查看文档](App)                                                          |
| Model            | `/models`            | `.mod.json`   | 数据模型 用于描述数据表结构 [查看文档](Model)                                                          |
| Store            | `/stores`            | `.stor.json`  | Key-Value 存储 [查看文档](Store)                                                                       |
| Flow             | `/flows`             | `.flow.json`  | 数据流 用于编排处理器调用逻辑 [查看文档](Flow)                                                         |
| API              | `/apis`              | `.http.json`  | REST API 用于编写 RESTFul API [查看文档](API)                                                          |
| Connector        | `/connectors`        | `.conn.json`  | 连接器 用于连接 Redis, Mongo, MySQL, ES 等外部服务, 连接器可与 Model, Store 关联 [查看文档](Connector) |
| Task             | `/tasks`             | `.task.json`  | 并发任务 [查看文档](Task)                                                                              |
| Schedule         | `/schedules`         | `.sch.json`   | 计划任务 [查看文档](Schedule)                                                                          |
| WebSocket Server | `/apis`              | `.ws.json`    | WebSocket Server[查看文档](WebSocket)                                                                  |
| WebSocket Client | `/websockets`        | `.ws.json`    | WebSocket Client[查看文档](WebSocket)                                                                  |
| Socket           | `/sockets`           | `.sock.json`  | Socket Server/Client [查看文档](Socket)                                                                |
| Cert             | `/certs`             | `.pem`        | PEM 证书导入 [查看文档](Cert)                                                                          |
| Import           | `/imports`           | `.imp.json`   | 数据导入 可以与表格界面关联 [查看文档](Import)                                                         |
| Login            | `/logins`            | `.login.json` | 登录界面 [查看文档](Login)                                                                             |
| Table            | `/tables`            | `.tab.json`   | 表格界面 [查看文档](Table)                                                                             |
| Form             | `/forms`             | `.form.json`  | 表单界面 [查看文档](Form)                                                                              |
| Chart            | `/charts`            | `.chart.json` | 图表界面 [查看文档](Chart)                                                                             |
