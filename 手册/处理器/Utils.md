# Utils

<blockquote>
  <p>一组实用程序处理器</p>
</blockquote>

**约定**

1. 示例中约定应用根目录为 `/data/app`, 实际编写时需替换为应用根目录。
2. 示例中约定服务器地址为 `http://127.0.0.1:5099`, 实际编写时需自行替换。
3. 使用 `<>` 标识自行替换的内容。 例如: `icon-<图标名称>`, 实际编写时应替换为: `icon-foo`, `icon-bar` ...

## 处理器

### 应用

| 处理器            | 参数表 | 返回值 | 说明 |
| ----------------- | ------ | ------ | ---- |
| utils.app.Ping    | `[]`   |        |      |
| utils.app.Inspect | `[]`   |        |      |

### 输入输出

| 处理器          | 参数表        | 返回值 | 说明 |
| --------------- | ------------- | ------ | ---- |
| utils.fmt.Print | `[...<Args>]` |        |      |

### 环境变量

| 处理器            | 参数表 | 返回值 | 说明 |
| ----------------- | ------ | ------ | ---- |
| utils.env.Get     | `[]`   |        |      |
| utils.env.Set     | `[]`   |        |      |
| utils.env.GetMany | `[]`   |        |      |
| utils.env.SetMany | `[]`   |        |      |

### 流程控制

| 处理器            | 参数表 | 返回值 | 说明          |
| ----------------- | ------ | ------ | ------------- |
| utils.flow.For    | `[]`   |        |               |
| utils.flow.Each   | `[]`   |        |               |
| utils.flow.Range  | `[]`   |        |               |
| utils.flow.Case   | `[]`   |        | Case 流程控制 |
| utils.flow.IF     | `[]`   |        | IF 流程控制   |
| utils.flow.Return | `[]`   |        | 返回输入数据  |

### JWT

| 处理器           | 参数表 | 返回值 | 说明 |
| ---------------- | ------ | ------ | ---- |
| utils.jwt.Make   | `[]`   |        |      |
| utils.jwt.Verify | `[]`   |        |      |

### 密码

| 处理器           | 参数表 | 返回值 | 说明 |
| ---------------- | ------ | ------ | ---- |
| utils.pwd.Hash   | `[]`   |        |      |
| utils.pwd.Verify | `[]`   |        |      |

### 图形/音频验证码

| 处理器               | 参数表 | 返回值 | 说明 |
| -------------------- | ------ | ------ | ---- |
| utils.captcha.Make   | `[]`   |        |      |
| utils.captcha.Verify | `[]`   |        |      |

### String

| 处理器             | 参数表                     | 返回值 | 说明         |
| ------------------ | -------------------------- | ------ | ------------ |
| utils.str.Concat   | `[<...str>]`               |        | 连接字符串   |
| utils.str.Join     | `[<字符串数组>, <分隔符>]` |        | 连接字符串   |
| utils.str.JoinPath | `[<...path>]`              |        | 连接文件目录 |

### 日期时间

| 处理器                | 参数表     | 返回值 | 说明                             |
| --------------------- | ---------- | ------ | -------------------------------- |
| utils.time.Sleep      | `[<毫秒>]` |        | Sleep 单位 ms                    |
| utils.now.Timestamp   | `[]`       |        | 当前时刻时间戳 (秒)              |
| utils.now.Timestampms | `[]`       |        | 当前时刻时间戳 (毫秒)            |
| utils.now.Date        | `[]`       |        | 当前时刻日期 2022-01-23          |
| utils.now.DateTime    | `[]`       |        | 当前时刻日期 2022-01-23 08:33:00 |
| utils.now.Time        | `[]`       |        | 当前时刻日期 08:33:00            |

### Array

| 处理器            | 参数表 | 返回值 | 说明 |
| ----------------- | ------ | ------ | ---- |
| utils.arr.Pluck   | `[]`   |        |      |
| utils.arr.Split   | `[]`   |        |      |
| utils.arr.Tree    | `[]`   |        |      |
| utils.arr.Unique  | `[]`   |        |      |
| utils.arr.Indexes | `[]`   |        |      |
| utils.arr.Get     | `[]`   |        |      |

### Map

| 处理器            | 参数表 | 返回值 | 说明 |
| ----------------- | ------ | ------ | ---- |
| utils.map.Get     | `[]`   |        |      |
| utils.map.Set     | `[]`   |        |      |
| utils.map.Del     | `[]`   |        |      |
| utils.map.DelMany | `[]`   |        |      |
| utils.map.Keys    | `[]`   |        |      |
| utils.map.Values  | `[]`   |        |      |
| utils.map.Merge   | `[]`   |        |      |
