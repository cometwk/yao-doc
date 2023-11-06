
## **约定**

1. 示例中约定应用根目录为 `/data/app`, 实际编写时需替换为应用根目录。
2. 使用 `<>` 标识自行替换的内容。 例如: `icon-<图标名称>`, 实际编写时应替换为: `icon-foo`, `icon-bar` ...

**命名**

DSL 文件命名:

1. 由 **小写字母**, **下划线 “\_”**, **横杠 "-"** 组成,
2. 必须由 **小写字母** 开头,
3. Widget ID 为文件名称(不含扩展名), 如包含多级目录用 **"."** 替代 **"\/"**


## app 目录参考12


```
.
├── aigcs
│   └── translate.ai.yml
├── apis
│   └── aigc.http.yao
├── app.yao
├── charts
│   └── pet.chart.yao
├── connectors
│   └── openai
│       ├── gpt-3_5-turbo.conn.yao
│       ├── text-embedding-ada-002.conn.yao
│       └── whisper-1.conn.yao
├── dashboards
│   └── kanban.dash.yao
├── data
│   └── 20231007
│       └── 517241DE-CC74-4876-9152-A4CF3550A95C.png
├── db
│   └── yao.db
├── flows
│   ├── app
│   │   └── menu.flow.yao
│   └── stat
│       └── data.flow.yao
├── forms
│   ├── admin
│   │   └── user.form.yao
│   └── demo
│       └── pet.form.yao
├── icons
│   ├── app.icns
│   ├── app.ico
│   └── app.png
├── langs
│   ├── zh-cn
│   │   └── global.yml
│   └── zh-hk
│       └── global.yml
├── logins
│   ├── admin.login.yao
│   └── user.login.yao
├── logs
│   └── application.log
├── models
│   ├── admin
│   │   └── user.mod.yao
│   └── pet.mod.yao
├── neo
│   └── neo.yml
├── public
│   ├── demo
│   │   └── pet.html
│   └── index.html
├── scripts
│   ├── dash.js
│   ├── guard.js
│   ├── setup.js
│   ├── stat.js
│   └── test.js
├── services
│   └── foo.js
├── studio
│   └── hello.js
└── tables
    ├── admin
    │   └── user.tab.yao
    └── demo
        ├── pet.tab.yao
        └── x.json

```
