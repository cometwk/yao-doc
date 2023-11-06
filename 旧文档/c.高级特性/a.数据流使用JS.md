# 数据流中使用 JS

<blockquote>
  <p>
    可以使用 JavaScript 脚本，对数据流节点返回值进行处理，按需返回数据结构。
  </p>
</blockquote>

## 使用 JS 脚本

编写数据流描述文件 `find.flow.json` 和 `find.format.js`，并放置在应用的 `flows` 目录中。

<Detail title="查看源码">

find.flow.json:

```json
{
  "label": "宠物",
  "version": "1.0.0",
  "description": "数据查询",
  "nodes": [
    {
      "name": "列表",
      "process": "models.pet.Find",
      "args": ["{{$in.0}}", { "select": ["id", "name", "kind"] }],
      "script": "format"
    }
  ],
  "output": "{{$res.列表}}"
}
```

find.format.js:

```javascript
/**
 * 为返回值添加颜色
 * @param []any args 数据流参数表 $in
 * @param any out  数据流节点处理器或QueryDSL返回值
 * @param [key:string]any res 数据流各个节点返回值
 */
function main(args, out, res) {
  var data = out || {};
  data["color"] = "#FEFEFE";
  return data;
}
```

</Detail>

**运行数据流**

```bash
yao run flows.find 1
```

## 脚本中使用函数

修改 `find.format.js` 实现根据种类添加颜色。

<Detail title="查看源码">

```javascript
/**
 * 根据类型设置颜色
 */
const color = (kind) => {
  if (kind == "猫") {
    return "#FEFEFE";
  } else if (kind == "狗") {
    return "#55555";
  }
};

/**
 * 宠物全名
 */
function fullname(id, kind, name) {
  return `${id}: ${kind} ${name}`;
}

/**
 * 为返回值添加颜色
 * @param []any args 数据流参数表 $in
 * @param any out  数据流节点处理器或QueryDSL返回值
 * @param [key:string]any res 数据流各个节点返回值
 */
function main(args, out, res) {
  var data = out || {};
  data["color"] = color(data.kind);
  data["fullname"] = fullname(args[0], data.kind, data.name);
  return data;
}
```

</Detail>

**运行数据流**

```bash
yao run flows.find 1
yao run flows.find 2
```

## 脚本中使用处理器

可以使用 `Process` 函数，调用处理器。 修改 `find.format.js` 同时返回用户信息。

<Detail title="查看源码">

```javascript
/**
 * 读取用户列表
 */
const users = () => {
  return Process("models.xiang.user.Get", { limit: 2, select: ["id", "name"] });
};

/**
 * 根据类型设置颜色
 */
const color = (kind) => {
  if (kind == "猫") {
    return "#FEFEFE";
  } else if (kind == "狗") {
    return "#55555";
  }
};

/**
 * 宠物全名
 */
function fullname(id, kind, name) {
  return `${id}: ${kind} ${name}`;
}

/**
 * 为返回值添加颜色
 * @param []any args 数据流参数表 $in
 * @param any out  数据流节点处理器或QueryDSL返回值
 * @param [key:string]any res 数据流各个节点返回值
 */
function main(args, out, res) {
  var data = out || {};
  data["color"] = color(data.kind);
  data["fullname"] = fullname(args[0], data.kind, data.name);
  data["users"] = users();
  return data;
}
```

</Detail>

**运行数据流**

```bash
yao run flows.find 1
```

## 推荐阅读

接下来，建议学习以下章节:

<Div style={{ display: "flex", justifyContent: "space-between" }}>
  <Link type="prev" title="查询数据" link="b.基础特性/f.查询数据"></Link>
  <Link
    type="next"
    title="数据模型关联"
    link="c.高级特性/b.数据模型关联"
  ></Link>
</Div>
