# Where 条件

## Object Where 数据结构

| 字段    | 类型                  | 说明                                                                         | 必填项 |
| ------- | --------------------- | ---------------------------------------------------------------------------- | ------ |
| field   | Field Expression      | 字段表达式，不支持设置别名 `as`                                              | 是     |
| value   | Any                   | 匹配数值。如果数据类型为 `Field Expression`, 用 `{}` 包括，如 `{updated_at}` | 否     |
| op      | String                | 匹配关系运算符。许可值 `=`,`like`,`in`,`>` 等，默认为 `=`                    | 否     |
| or      | Bool                  | `true` 查询条件逻辑关系为 `or`, 默认为 `false` 查询条件逻辑关系为 `and`      | 否     |
| wheres  | Array\<Object Where\> | 分组查询。用于 `condition 1` `and` ( `condition 2` OR `condition 3`) 的场景  | 否     |
| query   | Object QueryDSL       | 子查询；如设定 `query` 则忽略 `value` 数值。                                 | 否     |
| comment | String                | 查询条件注释，用于帮助理解查询条件逻辑和在开发平台中呈现。                   | 否     |

## 查询方法

| 查询方法 | 说明                                  |
| -------- | ------------------------------------- |
| where    | WHERE 字段 = 数值, WHERE 字段 >= 数值 |
| orwhere  | ... OR WHERE 字段 = 数值              |

## 匹配关系运算符

| 运算符    | 说明                             |
| --------- | -------------------------------- |
| `=`       | 默认值 等于 WHERE 字段 = 数值    |
| `>`       | 大于 WHERE 字段 > 数值           |
| `>=`      | 大于等于 WHERE 字段 >= 数值      |
| `<`       | 小于 WHERE 字段 < 数值           |
| `<=`      | 小于等于 WHERE 字段 <= 数值      |
| `like`    | 匹配 WHERE 字段 like 数值        |
| `match`   | 模糊匹配 WHERE 字段 match 数值   |
| `null`    | 为空 WHERE 字段 IS NULL          |
| `notnull` | 不为空 WHERE 字段 IS NOT NULL    |
| `in`      | 列表包含 WHERE 字段 IN (数值...) |

| 匹配关系 | 说明                             |
| -------- | -------------------------------- |
| eq       | 默认值 等于 WHERE 字段 = 数值    |
| like     | 匹配 WHERE 字段 like 数值        |
| gt       | 大于 WHERE 字段 > 数值           |
| ge       | 大于等于 WHERE 字段 >= 数值      |
| lt       | 小于 WHERE 字段 < 数值           |
| le       | 小于等于 WHERE 字段 <= 数值      |
| null     | 为空 WHERE 字段 IS NULL          |
| notnull  | 不为空 WHERE 字段 IS NOT NULL    |
| in       | 列表包含 WHERE 字段 IN (数值...) |
| ne       | 不等于                           |

<Div style={{ display: "flex", justifyContent: "space-between" }}>
  <Link type="prev" title="数据结构" link="手册/QueryDSL/数据结构"></Link>
  <Link type="next" title="新增" link="手册/QueryDSL/新增"></Link>
</Div>
