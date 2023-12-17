
| 类型                 | 说明                           | 可选参数             | MySQL 字段类型                         |
| -------------------- | ------------------------------ | -------------------- | -------------------------------------- |
| string               | 字符串                         | `length`             | VARCHAR(`length` )                     |
| char                 | 字符                           | `length`             | CHAR (`length` )                       |
| text                 | 文本                           |                      | TEXT                                   |
| mediumText           | 中文本                         |                      | MEDIUMTEXT                             |
| longText             | 长文本                         |                      | LONGTEXT                               |
| binary               | 二进制数据                     |                      | VARBINARY                              |
| date                 | 日期                           |                      | DATE                                   |
| datetime             | 日期时间                       | `length`             | DATETIME                               |
| datetimeTz           | 带时区的日期时间               | `length`             | DATETIME                               |
| time                 | 时间                           | `length`             | TIME                                   |
| timeTz               | 带时区的时间                   | `length`             | TIME                                   |
| timestamp            | 时间戳                         | `length`             | TIMESTAMP                              |
| timestampTz          | 带时区的时间戳                 | `length`             | TIMESTAMP                              |
| tinyInteger          | 微整型                         |                      | TINYINT                                |
| tinyIncrements       | 无符号微整型+自增              |                      | TINYINT UNSIGNED AUTO_INCREMENT        |
| unsignedTinyInteger  | 无符号微整型                   |                      | TINYINT UNSIGNED                       |
| smallInteger         | 小整型                         |                      | SMALLINT                               |
| smallIncrements      | 无符号小整型+自增              |                      | SMALLINT UNSIGNED AUTO_INCREMENT       |
| unsignedSmallInteger | 无符号小整型                   |                      | SMALLINT UNSIGNED                      |
| integer              | 整型                           |                      | INT                                    |
| increments           | 无符号整型+自增                |                      | INT UNSIGNED AUTO_INCREMENT            |
| unsignedInteger      | 无符号整型                     |                      | INT UNSIGNED                           |
| bigInteger           | 长整型                         |                      | BIGINT                                 |
| bigIncrements        | 无符号长整型+自增              |                      | BIGINT UNSIGNED AUTO_INCREMENT         |
| unsignedBigInteger   | 无符号长整型                   |                      | BIGINT UNSIGNED                        |
| id                   | 长整型+自增                    |                      | BIGINT UNSIGNED AUTO_INCREMENT         |
| ID                   | 长整型+自增(同 id)             |                      | BIGINT UNSIGNED AUTO_INCREMENT         |
| decimal              | 小数(一般用于存储货币)         | `precision`、`scale` | DECIMAL(`precision`,`scale`)           |
| unsignedDecimal      | 无符号小数 (一般用于存储货币)  | `precision`、`scale` | DECIMAL (`precision`,`scale`) UNSIGNED |
| float                | 浮点数                         | `precision`、`scale` | FLOAT (`precision`,`scale`)            |
| unsignedFloat        | 无符号浮点数                   | `precision`、`scale` | FLOAT (`precision`,`scale`) UNSIGNED   |
| double               | 双精度                         | `precision`、`scale` | DOUBLE (`precision`,`scale`)           |
| unsignedDouble       | 无符号双精度                   | `precision`、`scale` | DOUBLE (`precision`,`scale`) UNSIGNED  |
| boolean              | 布尔型                         |                      | BOOLEAN                                |
| enum                 | 枚举型                         | `option`             | ENUM(`option...`)                      |
| json                 | JSON 文本                      |                      | JSON                                   |
| JSON                 | JSON 文本(同 json)             |                      | JSON                                   |
| jsonb                | JSON (二进制格式存储)          |                      | JSON                                   |
| JSONB                | JSON (二进制格式存储 同 jsonb) |                      | JSON                                   |
| uuid                 | UUID 格式字符串                |                      | VARCHAR(36)                            |
| ipAddress            | IP 地址                        |                      | INT                                    |
| macAddress           | MAC 地址                       |                      | BIGINT                                 |
| year                 | 年份                           |                      | SMALLINT                               |