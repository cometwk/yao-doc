# HTTP

<blockquote>
  <p>HTTP 请求处理器</p>
</blockquote>

**约定**

1. 示例中约定应用根目录为 `/data/app`, 实际编写时需替换为应用根目录。
2. 示例中约定服务器地址为 `http://127.0.0.1:5099`, 实际编写时需自行替换。
3. 使用 `<>` 标识自行替换的内容。 例如: `icon-<图标名称>`, 实际编写时应替换为: `icon-foo`, `icon-bar` ...

## 处理器

| 处理器      | 参数表                                                                       | 返回值   | 说明                                                                  |
| ----------- | ---------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------- |
| http.Get    | `[<URL>, <Query (可选)>, <Headers (可选)>]`                                  | 响应结果 | 发送 HTTP GET 请求 [示例](#get) [文档](./HTTP/Get)                    |
| http.Post   | `[<URL>, <Payload (可选)>, <Files (可选)>, <Query(可选)>, <Headers (可选)>]` | 响应结果 | 发送 HTTP POST 请求 [示例](#post) [文档](./HTTP/Post)                 |
| http.Head   | `[<URL>, <Payload (可选)>, <Query (可选)>, <Headers (可选)>]`                | 响应结果 | 发送 HTTP HEAD 请求 [示例](#head) [文档](./HTTP/Head)                 |
| http.Put    | `[<URL>, <Payload (可选)>, <Query(可选)>, <Headers (可选)>]`                 | 响应结果 | 发送 HTTP PUT 请求 [示例](#put) [文档](./HTTP/Put)                    |
| http.Patch  | `[<URL>, <Payload (可选)>, <Query(可选)>, <Headers (可选)>]`                 | 响应结果 | 发送 HTTP PATCH 请求 [示例](#patch) [文档](./HTTP/Patch)              |
| http.Delete | `[<URL>, <Payload (可选)>, <Query(可选)>, <Headers (可选)>]`                 | 响应结果 | 发送 HTTP DELETE 请求 [示例](#delete) [文档](./HTTP/Delete)           |
| http.Send   | `[<METHOD>, <URL>, <Query (可选)>, <Payload (可选)>, <Headers (可选)>]`      | 响应结果 | 发送 HTTP POST 请求, 返回 JSON 数据 [示例](#send) [文档](./HTTP/Send) |

在脚本中可以使用 JS API: [查看 JS API 手册](../JSAPI/HTTP)

### 参数说明

URL: 目标网址

Query: Query 参数, 示例: `{"foo":"bar", "arr[]":"hello,world"}`, 对应 Query String: `foo=bar&arr[]=hello&arr[]=world`

Headers: 请求 Header, 示例: `{"Secret":"********"}` 或 `[{"Secret":"********"}, {"Secret":"#####"}]`

Data: 请求数据, 示例: `{"name":"Pet"}`, `http.Post` 发送时候自动添加 `Content-type: application/json; charset=utf-8` Header

Files: 上传文件, 示例: `{"file":"/path/root/file"}`, 文件路径为相对路径 相对地址, 示例: `/text/foo.txt`, 绝对路径为: `/data/app/data/text/foo.txt`。 如 Files 不为 null，自动添加 `Content-type: multipart/form-data` Header

### 数据结构

#### 响应结果

| 字段    | 类型    | 示例                      | 说明                                                                   |
| ------- | ------- | ------------------------- | ---------------------------------------------------------------------- |
| status  | Integer | 200                       | 响应状态码                                                             |
| data    | Any     | `{"name":"test"}`         | 响应数据(如果 Content-Type 为 JSON, 则自动解析 )                       |
| headers | Object  | `{"content-length": 400}` | 响应头                                                                 |
| code    | Integer | 400                       | 提取响应数据中 `code` 字段数值, 如果 `code` 字段不存在, 等于响应状态码 |
| message | String  | "Someting Error"          | 提取响应数据中 `message` 字段数值                                      |

## 示例

### Get

### Head

### Post

### Put

### Patch

### Delete

### Upload

### Send
