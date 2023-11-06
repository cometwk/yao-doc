# Session

<blockquote>
  <p>会话数据处理器</p>
</blockquote>

**约定**

1. 示例中约定应用根目录为 `/data/app`, 实际编写时需替换为应用根目录。
2. 示例中约定服务器地址为 `http://127.0.0.1:5099`, 实际编写时需自行替换。
3. 使用 `<>` 标识自行替换的内容。 例如: `icon-<图标名称>`, 实际编写时应替换为: `icon-foo`, `icon-bar` ...

## 处理器

| 处理器          | 参数表                             | 返回值          | 说明                                                        |
| --------------- | ---------------------------------- | --------------- | ----------------------------------------------------------- |
| session.Start   | `[]`                               | 会话 ID         | 生成一个会话 ID [示例](#start) [文档](./Session/Start)      |
| session.ID      | `[]`                               | 会话 ID         | 读取会话 ID [示例](#id) [文档](./Session/ID)                |
| session.Get     | `[<Key>]`                          | 数值            | 读取会话数据 [示例](#get) [文档](./Session/Get)             |
| session.Set     | `[<Key>, <Value>, <有效期(可选)>]` | -               | 设置会话数据 [示例](#set) [文档](./Session/Set)             |
| session.SetMany | `[<Data>, <有效期(可选)>]`         | -               | 批量设置会话数据 [示例](#setmany) [文档](./Session/SetMany) |
| session.Dump    | `[]`                               | 会话数据( Map ) | 读取所有会话数据 [示例](#dump) [文档](./Session/Dump)       |

**参数说明**

Key: `String` 键

Value: `Any` 值

Data: Key-Value Map, 示例: `{"user_id": 1, "name": "Bob"}`

有效期: Integer 单位秒

## 示例

### Start

### ID

### Get

### Set

### SetMany

### Dump
