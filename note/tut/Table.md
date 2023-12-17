# Table 表格界面

## 概述

```nomnoml render
[DSL|
  [DSL]-:>[<label> id]
  [DSL]-:>[<label> name]
  [DSL]-:>[config]
  [DSL]-:>[layout]
  [DSL]-:>[fields]
  [DSL]-:>[action]

  [config]-:>[<label> {}]
  [action]-:>[ActionDSL]
  [layout]-:>[LayoutDSL]
  [fields]-:>[FieldsDSL]

  [<state>Setting ]

  [name] --[Setting]
  [LayoutDSL] 主体部分--[Setting]
  [FieldsDSL] 嵌入--[Setting]
  [<label> {}] 嵌入--[Setting]

  [ActionDSL]--[<label> server处理器]



]


```

```nomnoml render

[Setting|
  [Setting]-:>[<label> name]
  [Setting]-:>[<label> primary]
  [Setting]-:>[config]
  [Setting]-:>[fields]
  [Setting]-:>[filters]
  [Setting]-:>[header]
  [Setting]-:>[table]
]

```
