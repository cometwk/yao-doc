# Store Key-Value 存储

Store 键-值存储，支持将数据保存在 `内存` `Redis`, `MongoDB` 中。

Store DSL 文件放置在项目 `stores` 文件夹下，命名为小写英文字母，扩展名为 `.类型.json` [查看示例](https://github.com/YaoApp/yao/tree/main/tests/stores)

| 引擎版本 | 说明                                                             |
| -------- | ---------------------------------------------------------------- |
| v0.10.2  | **支持** [下载地址](https://github.com/YaoApp/website-doc-zh-CN) |
| v0.10.1  | 部分支持, 不支持关联 Connector                                   |
| v0.9.2   | 部分支持, 不支持关联 Connector                                   |
| v0.9.1   | 不支持                                                           |

<Detail title="查看源码">

Connector: `redis.conn.json`

```json
{
  "LANG": "1.0.0",
  "VERSION": "1.0.0",
  "label": "Redis TEST",
  "type": "redis",
  "options": {
    "host": "127.0.0.1",
    "port": "6379",
    "pass": "123456",
    "db": "2"
  }
}
```

Store: `share.redis.json`

````json
{
  "name": "Redis Cache",
  "description": "Redis 缓存",
  "connector": "redis",
  "option": {}
}


LRU缓存: `cache.lru.json`

```json
{
  "name": "LRU Cache",
  "description": "LRU 缓存",
  "type": "lru",
  "option": {}
}
````

</Detail>

查看 [代码示例](#示例)

## DSL 结构

| 字段        | 说明                                                                |
| ----------- | ------------------------------------------------------------------- |
| name        | 名称                                                                |
| description | 描述                                                                |
| connector   | 绑定连接器名称(连接器) [查看连接器文档](Connector) **Yao v0.10.2+** |
| type        | 类型 `lru` LRU 缓存 (connector 为空时有效)                          |
| option      | 配置项 `{"size":10240}` type 为 `lru` 时有效， size 为 LRU 缓存大小 |

## 处理器清单

| 处理器                 | 参数表                    | 说明                     |
| ---------------------- | ------------------------- | ------------------------ |
| stores.存储名称.Get    | `[key:String]`            | 读取给定键的数值         |
| stores.存储名称.Set    | `[key:String, value:Any]` | 写入给定键的数值         |
| stores.存储名称.Has    | `[key:String]`            | 检查给定键的数值是否存在 |
| stores.存储名称.Del    | `[key:String]`            | 删除数据                 |
| stores.存储名称.GetDel | `[key:String]`            | 读取数据后，删除         |
| stores.存储名称.Len    | `[]`                      | 返回数量                 |
| stores.存储名称.Keys   | `[]`                      | 返回所有键               |
| stores.存储名称.Clear  | `[]`                      | 清除所有数据             |

## JS API

```javascript
var share = new Store("share");
share.Set("key1", "bar");
share.Get("key1");
share.Has("key1");
share.Del("key1");
share.GetSet("key1", function (key) {
  return key + " value";
});
share.Len();
share.Keys();
share.GetDel("key1");
share.Clear();
```

## 示例

https://github.com/YaoApp/yao/tree/main/tests/stores
