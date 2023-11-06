# Task

<Detail title="查看源码">

```json
{
  "name": "测试task",
  "worker_nums": 10,
  "attempts": 3,
  "attempt_after": 200,
  "timeout": 2,
  "size": 1000,
  "process": "scripts.task.Send",
  "event": {
    "next": "scripts.task.NextID",
    "add": "scripts.task.OnAdd",
    "success": "scripts.task.OnSuccess",
    "error": "scripts.task.OnError",
    "progress": "scripts.task.OnProgress"
  }
}
```

</Detail>

查看 [代码示例](#代码示例)

一般来说我们把长耗时，消耗大量资源，或者容易出错的逻辑，非常适合从请求主流程中剥离出来，异步执行。例如新用户注册，注册成功后，系统通常会发送一封欢迎邮件。发送欢迎邮件的动作就可以从注册流程中剥离出来，作为异步任务执行。这样应用服务器避免被图片处理等计算密集型任务压垮，用户也能更快的得到响应。Yao 支持添加异步任务来减少服务器请求压力。

## 处理器清单

| 处理器             | 说明                     | 文档 |
| ------------------ | ------------------------ | ---- |
| tasks.XXX.Add      | 添加一个 task 任务       | -    |
| tasks.XXX.progress | 查询一个 task 处理器进度 | -    |
| tasks.XXX.get      | 获取 task 处理的信息     | -    |

## 命名规范

| 参数          | 含义                   | 说明 |
| ------------- | ---------------------- | ---- |
| name          | 任务名称               |      |
| worker_nums   | 指定进程数             |      |
| attempts      | 失败重试次数           |      |
| attempt_after | 重试间隔               |      |
| timeout       | 超时时间               |      |
| process       | 该 task 绑定的处理器   |      |
| next          | 生成任务唯一 id        |      |
| add           | 添加任务时触发的方法   |      |
| success       | 任务处理成功后触发方法 |      |
| error         | 任务失败后触发方法     |      |
| progress      | 任务处理中调用         |      |

## 代码示例

### 第一步：新建文件目录 `/tasks/task.js`

```json
{
  "name": "测试task",
  "worker_nums": 10,
  "attempts": 3,
  "attempt_after": 200,
  "timeout": 2,
  "size": 1000,
  "process": "scripts.task.Send",
  "event": {
    "next": "scripts.task.NextID",
    "add": "scripts.task.OnAdd",
    "success": "scripts.task.OnSuccess",
    "error": "scripts.task.OnError",
    "progress": "scripts.task.OnProgress"
  }
}
```

### 第二步：新建 `scripts/task.js`

<Detail title="查看源码">

```javascript
var id = 1024;

/**
 * Generate job id
 * @returns
 */
function NextID() {
  id = id + 1;
  console.log(`NextID: ${id}`);
  return id;
}

function Send(id, message) {
  console.log(message);
}

/**
 * OnAdd add event
 * @param {*} id
 */
function OnAdd(id) {
  log.Error("进入add");
  console.log(`OnAdd: #${id}`);
}

/**
 * OnProgress
 * @param {*} id
 * @param {*} current
 * @param {*} total
 * @param {*} message
 */
function OnProgress(id, current, total, message) {
  console.log(`OnProgress: #${id} ${message} ${current}/${total} `);
}

function OnSuccess(id, res) {
  console.log(`OnSuccess: #${id} ${JSON.stringify(res)}`);
}

function OnError(id, err) {
  console.log(`OnError: #${id} ${err}`);
}
```

</Detail>

### 第三步：新建路由`apis/task.http.json`

```json
{
  "name": "任务",
  "version": "1.0.0",
  "description": "任务",
  "guard": "",
  "group": "task",
  "paths": [
    {
      "path": "/task",
      "method": "GET",
      "process": "scripts.test.task",
      "in": [],
      "out": {
        "status": 200,
        "type": "application/json"
      }
    }
  ]
}
```

### 第四步：新建测试函数 `scripts/test.js`

```javascript
function task() {
  for (i = 1; i < 100; i++) {
    Process("tasks.test.Add", "进入任务" + i);
  }
}
```

运行项目 `yao start` 访问 url `127.0.0.1:5099/api/task/task`可以看到打印信息

### 调用 Task 处理器`tasks.处理器名称.Add`

<Div style={{ display: "flex", justifyContent: "space-between" }}>
  <Link type="prev" title="Store" link="手册/Widgets/Store"></Link>
  <Link type="next" title="Schedule" link="手册/Widgets/Schedule"></Link>
</Div>
