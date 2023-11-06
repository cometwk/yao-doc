# 部署

<blockquote>本章节介绍如何将 Yao 部署到生产环境。</blockquote>

## 使用 Docker

- 安装 Docker 下载安装 Docker

- 创建并启动容器: `docker run -d --restart unless-stopped --name yao -v <app root>:/data/app -p <Port>:5099 yaoapp/yao:0.9.1-amd64`

**Yao Docker Images**

| 镜像                   | 环境     | 使用场景                 |
| ---------------------- | -------- | ------------------------ |
| yaoapp/yao:0.9.1-amd64 | 生产环境 | 适用于云端部署           |
| yaoapp/yao:0.9.1-arm64 | 生产环境 | 适用于物联网边缘设备部署 |

检查服务状态:

```bash
curl http://127.0.0.1:<Port>/api/xiang/ping
```

## 手动部署

### 第一步: 安装 Yao

运行安装脚本:

```bash
curl -fsSL https://website.yaoapps.com/install.sh | bash
```

### 第二步: 添加用户

添加用户

```bash
useradd yao
```

创建应用文件夹

```bash
mkdir /yaoapps
```

### 第三步: 部署代码

将应用代码复制到应用目录，例如

```bash
git clone  https://github.com/YaoApp/demo-crm.git  /yaoapps/demo-crm
```

<Notice type="warning">
  注意：生产环境中，请将启动模式设置为 <strong>production</strong>
</Notice>

### 第四步: 配置服务

使用 `pm2` , `supervisor` 等服务进程管理工具。

supervisor 配置示例：

```bash
[program:demo-crm-server]
directory=/yaoapps/demo-crm
command=/usr/local/bin/yao start
process_name=demo-crm-server
numprocs=1
autostart=true
autorestart=true
user=yao
group=yao
redirect_stderr=true
stdout_logfile=/yaoapps/demo-crm/supervisor.log

```

<Notice type="warning">注意：不要使用 root 用户启动服务。</Notice>

启动服务：

```bash
supervisor start
```

检查服务状态:

```bash
curl http://127.0.0.1:<Port>/api/xiang/ping
```

## 代理服务器

如需要使用 HTTPS 或者 一台机器上安装有多个应用，可以使用 `Nginx`, `traefik` 等代理服务器。

`traefik` 配置示例

```bash
[[tls.certificates]]
  certFile = "/data/certs/star.yaoapps.com.crt"
  keyFile = "/data/certs/star.yaoapps.com.key"

[http.routers.demo-crm]
  tls = true
  rule = "Host(`demo-crm.yaoapps.com`)"
  service = "demo-crm@file"

[http.services]
  [http.services.demo-crm.loadBalancer]
    [[http.services.demo-crm.loadBalancer.servers]]
      url = "http://127.0.0.1:<port>/"

```
