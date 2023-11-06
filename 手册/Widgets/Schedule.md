# Schedule

<Detail title="查看源码">

```json
{
  "name": "每分钟调用一次",
  "schedule": "*/1 * * * *",
  "process": "scripts.schedules.Send",
  "args": []
}
```

</Detail>

查看 [代码示例](#代码示例)

Yao 的计划任务是 Widget 功能，利用任务计划功能，可以将任何 DSL 脚本、Flows 安排在某个最方便的时间运行。任务计划在每次系统启动的时候启动并在后台运行。
当我们需要在服务器上定时执行一些重复性的事件时使用的，可以通过计划任务程序来运行准备好的 DSL 脚本在某个特定的时间运行。

## 命名规范

```json
{
  "name": "计划任务描述",
  "schedule": "计划任务时间设置",
  "process": "指定的处理器",
  "args": []
}
```

## DSL 结构

| 字段     | 说明             |
| -------- | ---------------- |
| name     | 名称             |
| schedule | 计划任务时间设置 |
| process  | 指定的处理器     |

## 代码示例

### 第一步：新建计划任务

- 新建 `/schedules/test.sch.json`，定时任务的写法和 Linux 的 crontab 是一样的，代码：

```json
{
  "name": "每分钟调用一次",
  "schedule": "*/1 * * * *",
  "process": "scripts.schedules.Send",
  "args": []
}
```

### 第二步：创建处理逻辑

- 新建 `scripts/schedules.js`代码：

```javascript
function Send() {
  console.log("进入定时任务！");
}
```

执行 `yao start`等待 1 分钟后可以看到打印信息

<Div style={{ display: "flex", justifyContent: "space-between" }}>
  <Link type="prev" title="Task" link="手册/Widgets/Task"></Link>
  <Link type="next" title="WebSocket" link="手册/Widgets/WebSocket"></Link>
</Div>
