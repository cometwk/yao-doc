# Store

<blockquote>
  <p>Key-Value 数据存储处理器</p>
</blockquote>

**约定**

1. 示例中约定应用根目录为 `/data/app`, 实际编写时需替换为应用根目录。
2. 示例中约定服务器地址为 `http://127.0.0.1:5099`, 实际编写时需自行替换。
3. 使用 `<>` 标识自行替换的内容。 例如: `icon-<图标名称>`, 实际编写时应替换为: `icon-foo`, `icon-bar` ...

## 处理器

**`<ID>` 为 `Store Widget ID`** 查看[使用 Widgets](../基础/使用Widgets)文档

Key: `String`

Value: `Any`

有效期: `Integer` 单位秒

| 处理器              | 参数表                             | 返回值                          | 说明                                                                |
| ------------------- | ---------------------------------- | ------------------------------- | ------------------------------------------------------------------- |
| stores.<ID\>.Get    | `[<Key>]`                          | Value                           | 查询给定键的数值 [示例](#get) [文档](./Store/Get)                   |
| stores.<ID\>.Set    | `[<Key>, <Value>, <有效期(可选)>]` | -                               | 存储数值 [示例](#set) [文档](./Store/Set)                           |
| stores.<ID\>.Has    | `[<Key>]`                          | 存在返回 true, 不存在返回 false | 查询给定键是否存在 [示例](#has) [文档](./Store/Has)                 |
| stores.<ID\>.Del    | `[<Key>]`                          | -                               | 删除键 [示例](#del) [文档](./Store/Del)                             |
| stores.<ID\>.GetDel | `[<Key>]`                          | Value                           | 查询给定键的数值, 然后删除键 [示例](#getdel) [文档](./Store/GetDel) |
| stores.<ID\>.Len    | `[]`                               | 键数量                          | 查询存储器键数量 [示例](#len) [文档](./Store/Len)                   |
| stores.<ID\>.Keys   | `[]`                               | 键名数组                        | 查询所有键名 [示例](#keys) [文档](./Store/Keys)                     |
| stores.<ID\>.Clear  | `[]`                               | -                               | 清除所有键 [示例](#clear) [文档](./Store/Clear)                     |

在脚本中可以使用 JS API: [查看 JS API 手册](../JSAPI/Store)

## 示例

### Get

### Set

### Has

### Del

### GetDel

### Len

### Keys

### Clear
