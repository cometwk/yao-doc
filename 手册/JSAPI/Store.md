# Store 缓存

## 示例

Store 使用缓存，新增文件`stores/cache.lru.json`：



应用目录结构:

```bash
├── apis        # 用于存放接口描述文件
│
├── models        # 用于存放数据模型描述文件
│
├── db
└── stores    #用于存放缓存目录
|
└── app.json
````

编写代码`cache.lru.json`：

```javascript
{
  "name": "LRU Cache",
  "description": "LRU缓存",
  "type": "lru",
  "option": { "size": 102400 }
}

```

在任意 JS 文件中使用缓存，Set 设置缓存，Get 获取缓存数据

```javascript
var cache = new Store("cache");

cache.Set("key", "for bar .....");

var cache_info = cache.Get("key");
```
