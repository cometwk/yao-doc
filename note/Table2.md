# Table 理解


先从查询API开始

- `GET /api/__yao/table/:id/search`
  - 按条件查询， see [手册/Widgets/API](https://yaoapps.com/doc/%E6%89%8B%E5%86%8C/Widgets/API#URL%20Query%20String%20%E4%B8%8E%20QueryParam%20%E5%AF%B9%E7%85%A7%E8%A1%A8)
  - 请求: `URL Query Params` 
    - 符合 ORM 查询规范的参数
    - 或者自定义
  - 响应: 返回带有分页信息和记录数组                              

**处理器**

- `yao.table.Search` 处理器参数 `[<Widget ID>, <查询参数>, <当前页码>, <每页显示记录>]` 



例如：

```http
http://localhost:5099/api/__yao/table/demo.pet/search?where.name.match=x&where.type.eq=cat&page=3&pagesize=2
```
- prefix: `__yao`
- DSL Widget: `table`
- Widget ID: `demo.pet`
- API Params: `where.name.match=x&where.type.eq=cat&page=3&pagesize=2`
  - 除去page参数， query params 可以映射为处理器查询参数

响应
```json
{
    "data": [
        {
            "appearance": [
                2
            ],
            "cost": 1000,
            "created_at": "2023-10-07 00:41:34",
            "curing_status": "1",
            "deleted_at": null,
            "detail": "hello",
            "id": 4,
            "images": "",
            "mode": "enabled",
            "name": "xx",
            "online": "1",
            "status": "checked",
            "stay": "2023-10-07 00:41:18",
            "type": "cat",
            "updated_at": null
        }
    ],
    "next": -1,
    "page": 1,
    "pagecnt": 1,
    "pagesize": 2,
    "prev": -1,
    "total": 1
}
```
