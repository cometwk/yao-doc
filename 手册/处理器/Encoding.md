# Encoding

<blockquote>
  <p>编码解码处理器</p>
</blockquote>

**约定**

1. 示例中约定应用根目录为 `/data/app`, 实际编写时需替换为应用根目录。
2. 示例中约定服务器地址为 `http://127.0.0.1:5099`, 实际编写时需自行替换。
3. 使用 `<>` 标识自行替换的内容。 例如: `icon-<图标名称>`, 实际编写时应替换为: `icon-foo`, `icon-bar` ...

## 处理器

| 处理器                 | 参数表           | 返回值             | 说明                                                              |
| ---------------------- | ---------------- | ------------------ | ----------------------------------------------------------------- |
| encoding.base64.Encode | `[<Source>]`     | Base64 编码字符串  | Base64 编码 [示例](#base64encode) [文档](./Encoding/Base64Encode) |
| encoding.base64.Decode | `[<Base64Code>]` | 原始字符串         | Base64 解码 [示例](#base64decode) [文档](./Encoding/Base64Decode) |
| encoding.hex.Encode    | `[<Source>]`     | 十六进制编码字符串 | 十六进制编码 [示例](#hexencode) [文档](./Encoding/HexEncode)      |
| encoding.hex.Decode    | `[<HexCode>]`    | 原始字符串         | 十六进制解码 [示例](#hexdecode) [文档](./Encoding/HexDecode)      |
| encoding.json.Encode   | `[<SourceData>]` | JSON 字符串        | JSON 格式编码 [示例](#jsonencode) [文档](./Encoding/JSONEncode)   |
| encoding.json.Decode   | `[<JSON>]`       | 原始数据           | JSON 格式解码 [示例](#jsondecode) [文档](./Encoding/JSONDecode)   |

**参数说明**

Source: `String` 原始数据

SourceData: `Any` 原始数据

Base64Code: `String` Base64 编码字符串

HexCode: `String` 十六进制编码字符串

JSON: JSON 格式字符串

## 示例

### base64.Encode

### base64.Decode

### hex.Encode

### hex.Decode

### json.Encode

### json.Decode
