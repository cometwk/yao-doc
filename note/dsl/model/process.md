
| 处理器                                 | 说明                                                                 | 文档                                          |
| ------------------------------------- | ------------------------------------------------------------------- | --------------------------------------------- |
| models.<模型名称\>.Find                | 查询单条记录                                                     | [查看](../处理器/process/Find)                |
| models.<模型名称\>.Get                 | 按条件查询, 不分页                                                | [查看](../处理器/process/Get)                 |
| models.<模型名称\>.Paginate            | 按条件查询, 分页                                                  | [查看](../处理器/process/Paginate)            |
| models.<模型名称\>.Create              | 创建单条记录, 返回新创建记录 ID                                     | [查看](../处理器/process/Create)              |
| models.<模型名称\>.Update              | 更新单条记录                                                      | [查看](../处理器/process/Update)              |
| models.<模型名称\>.Save                | 保存单条记录, 不存在创建记录, 存在更新记录, 返回记录 ID                 | [查看](../处理器/process/Save)                |
| models.<模型名称\>.Delete              | 删除单条记录(标记删除)                                             | [查看](../处理器/process/Delete)              |
| models.<模型名称\>.Destroy             | 删除单条记录(真删除)                                               | [查看](../处理器/process/Destroy)             |
| models.<模型名称\>.Insert              | 插入多条记录, 返回插入行数                                          | [查看](../处理器/process/Insert)              |
| models.<模型名称\>.UpdateWhere         | 按条件更新记录, 返回更新行数                                         | [查看](../处理器/process/UpdateWhere)         |
| models.<模型名称\>.DeleteWhere         | 按条件删除数据, 返回删除行数(标记删除)                                | [查看](../处理器/process/DeleteWhere)         |
| models.<模型名称\>.DestroyWhere        | 按条件删除数据, 返回删除行数(真删除)                                  | [查看](../处理器/process/DestroyWhere)        |
| models.<模型名称\>.EachSave            | 保存多条记录, 不存在创建记录, 存在更新记录, 返回记录 ID 集合             | [查看](../处理器/process/EachSave)            |
| models.<模型名称\>.EachSaveAfterDelete | 删除一组给定 ID 的记录后，保存多条记录, 不存在创建, 存在更新, 返回 ID 集合 | [查看](../处理器/process/EachSaveAfterDelete) |
