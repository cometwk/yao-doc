# Docker

本章节介绍如和构建 Docker 镜像并使用 Docker 镜像部署。

## 构建应用容器镜像

### 下载 Dockerfile :

下载地址: [https://github.com/YaoApp/dockerfiles](https://github.com/YaoApp/dockerfiles)

```bash
git clone https://github.com/YaoApp/dockerfiles /path/root/dockerfiles
```

### 构建命令:

#### AMD64

构建命令:

```bash
docker build \
   --platform linux/amd64 \
   --build-arg REPO=${REPO} \
   --build-arg TOKEN=${TOKEN} \
   --build-arg VERSION=${VERSION} \
   -t ${ORG}/${NAME}:${VERSION} .
```

示例:

```bash
cd /path/root/dockerfiles/application/amd64
docker build --platform linux/amd64 \
      --build-arg REPO=github.com/YaoApp/yao-wms  \
      --build-arg TOKEN=xxxxxxxxx  \
      --build-arg VERSION=1.0.3  \
      -t yaoapp/yao-wms:1.0.3-amd64 .
```

构建参数:

| 参数名  | 说明                                                                                                                                                     | 示例                      |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| REPO    | 应用代码仓库地址                                                                                                                                         | github.com/YaoApp/yao-wms |
| TOKEN   | GitHub personal access token [查看文档](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) | ghp_xxxxxxxxxxxxxxxxxx    |
| VERSION | 应用版本号                                                                                                                                               | 1.0.3                     |

#### ARM64

构建命令:

```bash
docker build \
   --platform linux/arm64 \
   --build-arg REPO=${REPO} \
   --build-arg TOKEN=${TOKEN} \
   --build-arg VERSION=${VERSION} \
   -t ${ORG}/${NAME}:${VERSION} .
```

示例:

```bash
cd /path/root/dockerfiles/application/arm64
docker build --platform linux/arm64 \
      --build-arg REPO=github.com/YaoApp/yao-wms  \
      --build-arg TOKEN=xxxxxxxxx  \
      --build-arg VERSION=1.0.3  \
      -t yaoapp/yao-wms:1.0.3-arm64 .
```

构建参数:

| 参数名  | 说明                                                                                                                                                     | 示例                      |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| REPO    | 应用代码仓库地址                                                                                                                                         | github.com/YaoApp/yao-wms |
| TOKEN   | GitHub personal access token [查看文档](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) | ghp_xxxxxxxxxxxxxxxxxx    |
| VERSION | 应用版本号                                                                                                                                               | 1.0.3                     |

## 使用应用容器镜像

### 环境变量

| 变量名            | 说明                                                                                                                                 | 示例            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| YAO_INIT          | `yaoadmin start` 首次启动前, 初始化数据，许可值 `demo` 初始化数据，并运行 DEMO 处理, `reset` 初始化数据。 不设置，则不执行初始化操作 | demo            |
| YAO_PROCESS_RESET | `yaoadmin reset` 成功迁移数据之后，运行的处理器                                                                                      | flows.init.menu |
| YAO_PROCESS_DEMO  | `yaoadmin reset --with-demo` 生成演示数据的处理器                                                                                    | flows.init.menu |

### SQLite 数据库

```bash
docker run -d -p 5099:5099 --restart unless-stopped \
    -e YAO_INIT=demo \
    -e YAO_PROCESS_RESET=flows.init.menu \
    -e YAO_PROCESS_DEMO=flows.demo.data  \
    yaoapp/yao-wms:1.0.3-amd64
```

### MySQL 数据库

```bash
docker run -d -p 3307:3306 --restart unless-stopped -e MYSQL_PASSWORD=123456 yaoapp/mysql:8.0-amd64
```

```bash
docker run -d -p 5099:5099 --restart unless-stopped \
    -e YAO_INIT=demo \
    -e YAO_PROCESS_RESET=flows.init.menu \
    -e YAO_PROCESS_DEMO=flows.demo.data  \
    -e YAO_DB_DRIVER=mysql \
    -e YAO_DB_PRIMARY="yao:123456@tcp(172.17.0.1:3307)/yao?charset=utf8mb4&parseTime=True&loc=Local" \
    yaoapp/yao-wms:1.0.3-amd64
```

Docker Compose

```yaml
version: "3.9"
services:
  yao:
    image: yaoapp/yao-wms:1.0.3-amd64
    environment:
      - YAO_INIT=demo
        YAO_PROCESS_RESET=flows.init.menu
        YAO_PROCESS_DEMO=flows.demo.data
        YAO_DB_DRIVER=mysql
        YAO_DB_PRIMARY="yao:123456@tcp(mysql:3306)/yao?charset=utf8mb4&parseTime=True&loc=Local"
    ports:
      - "5099:5099"
    volumes:
      - data:/data/app/data
    depends_on:
      - mysql
    deploy:
      restart_policy:
        condition: unless-stopped
        max-attempts: 3

  mysql:
    image: yaoapp/mysql:8.0-amd64
    environment:
      - MYSQL_PASSWORD=123456
    deploy:
      restart_policy:
        condition: unless-stopped
        max-attempts: 3

volumes:
  data: {}
```

### MySQL 数据库 + REDIS

```bash
docker run -d -p 3307:3306 --restart unless-stopped -e MYSQL_PASSWORD=123456 yaoapp/mysql:8.0-amd64
```

```bash
docker run -d -p 6371:6379 --restart unless-stopped -e REDIS_PASSWORD=123456 yaoapp/redis:6.2-amd64
```

```bash
docker run -d -p 5099:5099 --restart unless-stopped \
    -e YAO_INIT=demo \
    -e YAO_PROCESS_RESET=flows.init.menu \
    -e YAO_PROCESS_DEMO=flows.demo.data  \
    -e YAO_DB_DRIVER=mysql \
    -e YAO_DB_PRIMARY="yao:123456@tcp(172.17.0.1:3307)/yao?charset=utf8mb4&parseTime=True&loc=Local" \
    -e YAO_SESSION_STORE=redis \
    -e YAO_SESSION_HOST=172.17.0.1 \
    -e YAO_SESSION_PORT=6371 \
    -e YAO_SESSION_PASSWORD=123456 \
    yaoapp/yao-wms:1.0.3-amd64
```

Docker Compose

```yaml
version: "3.9"
services:
  yao:
    image: yaoapp/yao-wms:1.0.3-amd64
    environment:
      - YAO_INIT=demo
        YAO_PROCESS_RESET=flows.init.menu
        YAO_PROCESS_DEMO=flows.demo.data
        YAO_DB_DRIVER=mysql
        YAO_DB_PRIMARY="yao:123456@tcp(mysql:3306)/yao?charset=utf8mb4&parseTime=True&loc=Local"
        YAO_SESSION_STORE=redis \
        YAO_SESSION_HOST=redis \
        YAO_SESSION_PORT=6379 \
        YAO_SESSION_PASSWORD=123456 \
    ports:
      - "5099:5099"
    volumes:
      - data:/data/app/data
    depends_on:
      - mysql
        redis
    deploy:
      restart_policy:
        condition: unless-stopped
        max-attempts: 3

  mysql:
    image: yaoapp/mysql:8.0-amd64
    environment:
      - MYSQL_PASSWORD=123456
    deploy:
      restart_policy:
        condition: unless-stopped
        max-attempts: 3

  redis:
    image: yaoapp/mysql:8.0-amd64
    environment:
      - REDIS_PASSWORD=123456
    deploy:
      restart_policy:
        condition: unless-stopped
        max-attempts: 3

volumes:
  data: {}
```

### yaoadmin 管理脚本

#### yaoadmin start

启动服务.

**如设置 `YAO_INIT` 环境变量，启动前检查 `/data/app/data/.lock` 文件是否存在；如果不存在则添加 `.lock` 文件，并执行 RESET 逻辑。**

进入容器, 在宿主机运行

```bash
docker exec -it 容器名称 /bin/sh

```

在容器内运行

```bash
yaoadmin start
```

#### yaoadmin reset

**运行 yao migrate --reset 命令重置数据表结构，成功运行后运行 `YAO_PROCESS_RESET` 指定的处理器**

进入容器, 在宿主机运行

```bash
docker exec -it 容器名称 /bin/sh

```

在容器内运行

```bash
yaoadmin reset
```

如需添加演示数据，则添加 `--with-demo` 参数。成功 RESET 后运行 `YAO_PROCESS_DEMO` 指定的处理器，生成演示数据

```bash
yaoadmin reset --with-demo
```

## CI/CD

可以通过配置持续集成工作流，在更新 `app.json` 中版本信息时，自动构建并发布 docker 镜像。

### Github

Github Workflow 参考:

https://github.com/YaoApp/dockerfiles/blob/main/cicd/github/workflows/docker.yml

可以将示例 `github` 目录复制到项目根目录，改名为 `.github`

```bash
cp -r /path/root/dockerfiles/github  /your-project/path/root/.github
```

Secrets 变量说明

| 变量            | 说明                |
| --------------- | ------------------- |
| DOCKER_USER     | Docker hub 用户名   |
| DOCKER_PASSWORD | Docker hub 登录密码 |

[查看 Github Workflow 文档](https://docs.github.com/en/actions)
