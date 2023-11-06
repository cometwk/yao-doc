# 安装调试

<blockquote>

本章节介绍如何在本地建立 Yao 开发调试环境。生产环境使用，请参考 <a href="../部署/介绍">部署</a> 文档。

</blockquote>

## 安装

<Tabs defaultActiveKey='1'>
<TabPane tab='Linux & MacOS' key='1'>

在终端下运行脚本:

```bash
curl -fsSL https://website.yaoapps.com/install.sh | bash
```

</TabPane>

<TabPane tab='Windows' key='2'>

1. 安装 Docker [下载安装 Docker](https://docs.docker.com/desktop/windows/install/)

2. 创建并启动容器: `docker run -d --name yao -v <project root>:/data/app -p 5099:5099 yaoapp/yao:0.9.2-amd64-dev`

进入容器:

```bash
docker exec -it yao /bin/bash
```

在容器内使用 yao 命令

```bash
yao version
```

**Yao Docker Images**

| 镜像                       | 环境     | 使用场景                                                   |
| -------------------------- | -------- | ---------------------------------------------------------- |
| yaoapp/yao:0.9.2-amd64-dev | 开发环境 | `amd64` 适用于 MacOS Intel, Windows X86 64 位, Linux 64 位 |
| yaoapp/yao:0.9.2-arm64-dev | 开发环境 | `arm64` 适用于 MacOS M1, 树莓派, RK 开发板等               |
| yaoapp/yao:0.9.2-amd64     | 生产环境 | 适用于云端部署                                             |
| yaoapp/yao:0.9.2-arm64     | 生产环境 | 适用于物联网边缘设备部署                                   |

</TabPane>

<TabPane tab='Docker (推荐)' key='3'>

1. 安装 Docker [下载安装 Docker](https://docs.docker.com/get-docker/)

2. 创建并启动容器:`docker run -d --name yao -v <project root>:/data/app -p 5099:5099 yaoapp/yao:0.9.2-amd64-dev`

进入容器:

```bash
docker exec -it yao /bin/bash
```

在容器内使用 yao 命令

```bash
yao version
```

**Yao Docker Images**

| 镜像                       | 环境     | 使用场景                                                   |
| -------------------------- | -------- | ---------------------------------------------------------- |
| yaoapp/yao:0.9.2-amd64-dev | 开发环境 | `amd64` 适用于 MacOS Intel, Windows X86 64 位, Linux 64 位 |
| yaoapp/yao:0.9.2-arm64-dev | 开发环境 | `arm64` 适用于 MacOS M1, 树莓派, RK 开发板等               |
| yaoapp/yao:0.9.2-amd64     | 生产环境 | 适用于云端部署                                             |
| yaoapp/yao:0.9.2-arm64     | 生产环境 | 适用于物联网边缘设备部署                                   |

</TabPane>

</Tabs>

<Notice type="success">
  Yao 默认使用 Sqlite 存储数据，如果您需要使用
  MySQL、PostgreSQL数据库作为数据源，请参照数据库官方文档下载并安装。推荐使用
  MySQL 8 或Postgres14。
</Notice>

## 调试命令

### Run 运行处理器

进入项目目录，使用 `run` 命令，运行数据流、脚本、插件以及内建的处理器。

`yao run <process> [args...]`

```bash
cd /data/customer
yao run xiang.main.Inspect
```

参数表:

| 参数    | 必填 | 说明                                                     |
| ------- | ---- | -------------------------------------------------------- |
| process | 是   | 运行处理器名称. [处理器文档](../b.基础特性/d.使用处理器) |
| args... | 否   | 处理器的输入参数表。[处理器文档](../d.API参考/d.处理器)  |

### Start 启动服务

`yao start`

进入项目目录，使用 `start` 命令，启动服务。默认服务端口为 `5099`， 可通过声明环境变量，指定服务端口。 [环境变量](#环境变量)

```bash
cd /data/customer
yao start
```

参数表:

| 参数    | 必填 | 说明                                                               |
| ------- | ---- | ------------------------------------------------------------------ |
| --alpha | 否   | 如果希望试用 Yao 的一些内测功能，使用 `yao start --alpha` 命令启动 |
| --debug | 否   | 强制开启开发模式 `yao start --debug` 命令启动                      |

## 环境变量

可以通过声明环境变量，指定服务端口，配置数据库连接 例如：

```bash
export YAO_ENV="production" # development | production 运行模式
export YAO_ROOT="/data/app"  # 应用目录
export YAO_HOST="127.0.0.1" # 服务 HOST
export YAO_PORT="5099"  # 监听端口
export YAO_LOG="/data/app/logs/application.log"  # 日志文件位置
export YAO_LOG_MODE="TEXT"  # 日志模式 TEXT | JSON
export YAO_JWT_SECRET="bLp@bi!oqo-2U+hoTRUG"
export YAO_DB_DRIVER="mysql" # 数据库类型 mysql | sqlite3
export YAO_DB_PRIMARY="root:123456@tcp(db-server:3308)/xiang?charset=utf8mb4&parseTime=True&loc=Local"  # 主库连接
export YAO_DB_SECONDARY="root:123456@tcp(db-server:3308)/xiang?charset=utf8mb4&parseTime=True&loc=Local" # 从库连接
export YAO_DB_AESKEY="ZLX=T&f6refeCh-ro*r@" # 加密存储字段密钥 MySQL Only
```

可以在项目目录根目录下添加 `.env`，服务启动时将优先使用 .env 声明的环境变量；或将以上命令追加到 `~/.bashrc` 文件（macos `~/.bash_profile` )

`/data/customer/.env` 文件内容

```bash
YAO_ENV="production" # development | production 运行模式
YAO_ROOT="/data/app"  # 应用目录
YAO_HOST="127.0.0.1" # 服务 HOST
YAO_PORT="5099"  # 监听端口
YAO_LOG="/data/app/logs/application.log"  # 日志文件位置
YAO_LOG_MODE="TEXT"  # 日志模式 TEXT | JSON
YAO_JWT_SECRET="bLp@bi!oqo-2U+hoTRUG"
YAO_DB_DRIVER="mysql" # 数据库类型 mysql | sqlite3
YAO_DB_PRIMARY="root:123456@tcp(db-server:3308)/xiang?charset=utf8mb4&parseTime=True&loc=Local"  # 主库连接
YAO_DB_SECONDARY="root:123456@tcp(db-server:3308)/xiang?charset=utf8mb4&parseTime=True&loc=Local" # 从库连接
YAO_DB_AESKEY="ZLX=T&f6refeCh-ro*r@" # 加密存储字段密钥 MySQL Only

```

<!--
## 视频讲解

<Video src="https://player.bilibili.com/player.html?aid=507380047&bvid=BV1Sg411w7hs&cid=465617729&page=1"></Video>

-->

## 相关内容

接下来，建议学习以下章节:

<Extend
  title="创建数据模型"
  desc="了解如何创建模型，存储数据到数据库"
  link="b.基础特性/a.创建数据模型"
></Extend>

<Div style={{ display: "flex", justifyContent: "space-between" }}>
  <Link type="prev" title="入门指南" link="a.介绍/a.入门指南"></Link>
  <Link type="next" title="为什么选择Yao" link="a.介绍/c.为什么选择Yao"></Link>
</Div>
