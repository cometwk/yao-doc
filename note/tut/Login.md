# Login 登录

## DSL

```nomnoml render
[DSL|
  [DSL]-:>[<label> id]
  [DSL]-:>[<label> name]
  [DSL]-:>[action]
  [DSL]-:>[layout]
  [DSL]-:>[thirdPartyLogin]

  [action]-:>[ActionDSL]
  [layout]-:>[LayoutDSL]
  [thirdPartyLogin]-:>[ThirdPartyLoginDSL]

  [<state>Setting]
  [name] --[Setting]
  [LayoutDSL] --[Setting]
  [ThirdPartyLoginDSL] --[Setting]

  [ActionDSL]--[<label> server处理器]
]
```

```ts
  interface DSL {
    id?: string
    name?: string
    action?: ActionDSL
    layout?: LayoutDSL
    thirdPartyLogin?: ThirdPartyLoginDSL[]
  }

  interface ActionDSL {
    process?: string
    args?: any[] // 由于 Go 中使用了 interface{}，这里使用 any[] 表示一个任意类型数组
  }

  interface LayoutDSL {
    entry?: string
    captcha?: string
    cover?: string
    slogan?: string
    site?: string
  }

  interface ThirdPartyLoginDSL {
    title?: string
    href?: string
    icon?: string
    blank?: boolean
  }
```

## Setting

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
