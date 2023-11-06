# Yao 命令

```bash
yao <command> [options] [args...]
```

| 命令    | 说明             |
| ------- | ---------------- |
| init    | 项目初始化       |
| inspect | 显示应用配置信息 |
| migrate | 更新数据库结构   |
| run     | 运行处理器       |
| start   | 启动 WEB 服务    |
| version | 显示当前版本号   |

全局选项:

| 参数   | 简写 | 说明             |
| ------ | ---- | ---------------- |
| --app  | -a   | 指定应用路径     |
| --env  | -e   | 指定环境变量文件 |
| --help | -h   | 命令帮助         |

# yao init

项目初始化, 创建 app.json, data, models 等文件和目录。

```bash
cd /path/app
yao init
```

# yao inspect

显示应用配置信息

```bash
cd /path/app
yao inspect
```

# yao migrate

更新数据库结构，创建应用引擎和 models 文件夹下定义的数据表。默认更新 models 下所数据模型关联的数据表。

<Notice type="warning">
  注意：`migrate` 命令会清空当前数据表， 不推荐在 `production` 模式下使用。
</Notice>

选项:

| 参数    | 简写 | 说明                                   |
| ------- | ---- | -------------------------------------- |
| --name  | -n   | 指定模型名称                           |
| --force |      | 在 production 模式下, 强制使用 migrate |

```bash
cd /path/app
yao migrate
```

```bash
cd /path/app
yao migrate -n pet
```

# yao run

运行处理器, 第一个参数为处理器名称，其余参数为处理器参数表。

如果需要输入复杂数据结构可以使用 `::` 前缀，声明参数为 JSON 格式， 例如: `'::{"foo":"bar"}'`

```bash
cd /path/app
yao run scripts.day.NextDay 2020-01-02
```

```bash
cd /path/app
yao run xiang.flow.Return hello '::{"foo":"bar"}'
```

# yao start

启动 WEB 服务

选项:

| 参数    | 简写 | 说明             |
| ------- | ---- | ---------------- |
| --alpha |      | 启用内测功能     |
| --debug |      | 使用开发模式启动 |

```bash
cd /path/app
yao start
```

```bash
cd /path/app
yao start --debug
```

```bash
cd /path/app
yao start --alpha
```

# yao version

显示 Yao 版本号

```bash
yao version
```
