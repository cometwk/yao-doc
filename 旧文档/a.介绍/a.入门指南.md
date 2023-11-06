# 入门指南

<blockquote>
  YAO 是一款开源应用引擎，使用 Golang
  编写，仅一个命令行工具,下载即用。适合用于开发业务系统、网站/APP API
  接口、管理后台、自建低代码平台等。
</blockquote>

## 介绍

Yao 基于 **flow-based** 编程思想，采用 **Go** 语言开发，支持多种方式扩展数据流处理器。这使得 Yao 具有极好的**通用性**，大部分场景下可以代替编程语言, 在复用性和编码效率上是传统编程语言的 **10 倍**；应用性能和资源占比上优于 **PHP**, **JAVA** 等语言。

Yao 内置了一套数据管理系统，通过编写 **JSON** 描述界面布局，即可实现 90% 常见界面交互功能，特别适合快速制作各类管理后台、CRM、ERP 等企业内部系统。对于特殊交互功能亦可通过编写扩展组件或 HTML 页面的方式实现。内置管理系统与 Yao 并不耦合，亦可采用 **VUE**, **React** 等任意前端技术实现管理界面。

Yao 的名字源于汉字**爻(yáo)**，是构成八卦的基本符号。八卦，是上古大神伏羲观测总结自然规律后，创造的一个可以指代万事万物的符号体系。爻，有阴阳两种状态，就像 0 和 1。爻的阴阳转换，驱动八卦更替，以此来总结记录事物的发展规律。

## 演示

### 客户关系管理系统

一套通用 CRM 管理系统

<Button className="mr_12" type="primary">
  <a
    href="https://demo-crm.yaoapps.com/xiang/login/admin?autoLogin=true"
    target="_blank"
  >
    演示
  </a>
</Button>

GitHub: https://github.com/YaoApp/demo-crm

Infra 一键部署: https://letsinfra.com/openapp/crm

### 智能仓库管理系统

云+边物联网应用示例，支持人脸识别、RFID 的无人值守智能仓库管理系统。

<Button className="mr_12" type="primary">
  <a
    href="https://demo-wms.yaoapps.com/xiang/login/admin?autoLogin=true"
    target="_blank"
  >
    演示
  </a>
</Button>

GitHub: https://github.com/YaoApp/yao-wms

Infra 一键部署: https://letsinfra.com/openapp/wms

## 起步

<Notice type="warning">
  注意：开始前需要了解JSON、RESTFul
  API、关系型数据库的基本概念和常识，并可以使用常见终端命令。
  如需处理非常复杂的业务逻辑，则需要掌握 JavaScript 语言。
</Notice>

参考文档: [YAO 编程基础](../基础/YAO%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80.mdx)

### 准备: 安装 Yao

在终端下运行脚本: ( MacOS / Linux )

```bash
curl -fsSL https://website.yaoapps.com/install.sh | bash
```

windows 用户请参考安装调试章节:

<Extend
  title="安装调试"
  desc="了解如何在本地建立Yao开发调试环境"
  link="安装调试"
></Extend>

### 第一步: 创建项目

新建一个项目目录，进入项目目录，运行 `yao init` 命令，创建一个空白的 Yao 应用。

```bash
mkdir -p /data/crm  # 创建项目目录
cd /data/crm  # 进入项目目录
yao init # 运行初始化程序
```

命令运行成功后，将创建 `app.json文件` , `db`, `ui` , `data` 等目录

```bash
├── data        # 用于存放应用产生的文件，如图片,PDF等
├── db          # 用于存放 SQLite 数据库文件
│   └── yao.db
└── ui          # 静态文件服务器文件目录，可以放置自定义前端制品，该目录下文件可通过 http://host:port/文件名称 访问。
└── app.json    # 应用配置文件, 用来定义应用名称等
```

### 第二步: 创建数据表

使用 `yao migrate` 命令创建数据表，打开命令行终端，**在项目根录下运行**:

```bash
yao migrate
```

初始化菜单

```bash
yao run flows.setmenu
```

扩展阅读:

<Extend
  title="使用Widgets"
  desc="了解如何使用 Yao Model Widget 创建数据表存储数据"
  link="基础/使用Widgets"
></Extend>

### 第三步: 启动服务

打开命令行终端，**在项目根录下运行**:

```bash
yao start
```

1. 打开浏览器, 访问 `https://127.0.0.1:5099/xiang/login/admin`，

2. 输入默认用户名: `xiang@iqka.com`， 密码: `A123456p+`

## 相关内容

接下来，建议学习以下章节:

<Extend
  title="为什么选择Yao"
  desc="了解 Yao 的一些特性和对比其他开发方式的优势"
  link="为什么选择Yao"
></Extend>

<Div style={{ display: "flex", justifyContent: "right" }}>
  <Link type="next" title="安装调试" link="安装调试"></Link>
</Div>
