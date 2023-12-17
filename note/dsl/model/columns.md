
| 字段        | 类型                   | 说明                                                                                        | 必填项 |
| ----------- | ---------------------- | ------------------------------------------------------------------------------------------- | ------ |
| name        | String                 | 字段名称，对应数据表中字段名称                                                              | 是     |
| type        | String                 | 字段类型，                                                                                  | 是     |
| label       | String                 | 字段显示名称，用于在管理表单，开发平台等成场景下呈现                                        | 是     |
| comment     | String                 | 字段注释，对应数据表中字段注释                                                              | 否     |
| title       | String                 | 字段标题，可用于开发平台中呈现                                                              | 否     |
| description | String                 | 字段介绍，可用于开发平台中呈现                                                              | 否     |
| length      | Integer                | 字段长度，对 `string` 等类型字段有效                                                        | 否     |
| precision   | Integer                | 字段位数(含小数位)，对 `float`、`decimal` 等类型字段有效                                    | 否     |
| scale       | Integer                | 字段小数位位数，对 `float`、`decimal` 等类型字段有效                                        | 否     |
| option      | Array\<String\>        | 字段许可值，对 `enum` 类型字段有效                                                          | 否     |
| default     | String\|Integer\|Float | 字段默认值                                                                                  | 否     |
| default_raw | String                 | 字段默认值，支持数据库函数，如 `NOW()` default 和 default_raw 同时存在 default_raw 优先级高 | 否     |
| crypt       | String                 | 字段加密存储方式(MySQL Only)。许可值 `AES`, `PASSWORD`                                      | 否     |
| nullable    | Bool                   | 字段是否可以为空，默认为 false                                                              | 否     |
| index       | Bool                   | 字段是否为索引，默认为 false                                                                | 否     |
| unique      | Bool                   | 字段是否为唯一索引，默认为 false , 如为 true 无需同时将 `index` 设置为 true                 | 否     |
| primary     | Bool                   | 字段是否为主键，每张表至多一个主键字段。默认为 false                                        | 否     |
| validations | Array\<Object\>        | 字段校验规则                                                                                | 否     |
