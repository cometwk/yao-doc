
| 校验方法  | 参数                                                                                | 说明     | 示例                                                                  |
| --------- | ----------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------- |
| typeof    | `[<String>]` 许可值 `string`, `integer`, `float`, `number`, `datetime`, `timestamp` | 数值类型 | `{"method":"typeof", "args":["integer"]}`                             |
| min       | `[<Integer\|Float>]`                                                                | 最小值   | `{"method":"min", "args":[20]}`                                       |
| max       | `[<Integer\|Float>]`                                                                | 最大值   | `{"method":"max", "args":[0.618]}`                                    |
| enum      | `[String...]`                                                                       | 枚举选项 | `{"method":"enum", "args":["enabled", "disabled"]}`                   |
| pattern   | `[String]`                                                                          | 正则匹配 | `{"method":"pattern", "args":["^1[3-9]\\d{9}$"]}`                     |
| minLength | `[<Integer>]`                                                                       | 最小长度 | `{"method":"minLength", "args":[20]}`                                 |
| maxLength | `[<Integer>]`                                                                       | 最大长度 | `{"method":"maxLength", "args":[100]}`                                |
| email     | `[]`                                                                                | 邮箱     | `{"method":"email", "args":[]}`                                       |
| mobile    | `[<String>]` 区域列表(可选), 默认为 `cn` 许可值 `cn`,`us`                           | 手机号   | `{"method":"mobile", "args":[]}` `{"method":"mobile", "args":["us"]}` |

