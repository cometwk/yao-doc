# Model

<blockquote>
  <p>数据模型原子操作处理器</p>
</blockquote>

**约定**

1. 示例中约定应用根目录为 `/data/app`, 实际编写时需替换为应用根目录。
2. 示例中约定服务器地址为 `http://127.0.0.1:5099`, 实际编写时需自行替换。
3. 使用 `<>` 标识自行替换的内容。 例如: `icon-<图标名称>`, 实际编写时应替换为: `icon-foo`, `icon-bar` ...

## 处理器

**`<ID>` 为 `Model Widget ID`** 查看[使用 Widgets](../基础/使用Widgets)文档

| 处理器                           | 参数表                                        | 返回值                     | 说明                                                                                                                                        |
| -------------------------------- | --------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| models.<ID\>.Find                | `[<主键值>,<查询条件>]`                       | 单条记录                   | 查询单条记录 [示例](#find) [文档](./Model/Find)                                                                                             |
| models.<ID\>.Get                 | `[<主键值>,<查询条件>]`                       | 记录数组                   | 按条件查询, 不分页 [示例](#get) [文档](./Model/Get)                                                                                         |
| models.<ID\>.Paginate            | `[<查询条件>,<当前页码>, <每页显示记录数>]`   | 分页信息和记录数组         | 按条件查询, 分页 [示例](#paginate) [文档](./Model/Paginate)                                                                                 |
| models.<ID\>.Create              | `[<记录>]`                                    | 新记录主键值               | 创建单条记录, 返回新创建记录 ID [示例](#create) [文档](./Model/Create)                                                                      |
| models.<ID\>.Update              | `[<主键值>,<记录>]`                           | -                          | 更新单条记录 [示例](#update) [文档](./Model/Update)                                                                                         |
| models.<ID\>.Save                | `[<记录>]`                                    | 记录主键值                 | 保存单条记录, 不存在创建记录, 存在更新记录, 返回记录 ID [示例](#save) [查看](./Model/Save)                                                  |
| models.<ID\>.Delete              | `[<主键值>]`                                  | -                          | 删除单条记录(标记删除) [示例](#delete) [文档](./Model/Delete)                                                                               |
| models.<ID\>.Destroy             | `[<主键值>]`                                  | -                          | 删除单条记录(真删除) [示例](#destroy) [文档](./Model/Destroy)                                                                               |
| models.<ID\>.Insert              | `[<字段名称数组>, <二维记录值数组>]`          | 成功插入行数               | 插入多条记录, 返回插入行数 [示例](#insert) [文档](./Model/Insert)                                                                           |
| models.<ID\>.UpdateWhere         | `[<查询条件>,<记录>]`                         | 成功更新行数               | 按条件更新记录, 返回更新行数 [示例](#updatewhere) [文档](./Model/UpdateWhere)                                                               |
| models.<ID\>.DeleteWhere         | `[<查询条件>]`                                | 成功删除行数               | 按条件删除数据, 返回删除行数(标记删除) [示例](#deletewhere) [文档](./Model/DeleteWhere)                                                     |
| models.<ID\>.DestroyWhere        | `[<查询条件>]`                                | 成功删除行数               | 按条件删除数据, 返回删除行数(真删除) [示例](#destroywhere) [文档](./Model/DestroyWhere)                                                     |
| models.<ID\>.EachSave            | `[<记录数组>, <记录(共有字段)>]`              | 创建或更新的记录主键值数组 | 保存多条记录, 不存在创建记录, 存在更新记录, 返回记录 ID 集合 [示例](#eachsave) [文档](./Model/EachSave)                                     |
| models.<ID\>.EachSaveAfterDelete | `[<主键值数组>,<记录数组>, <记录(共有字段)>]` | 创建或更新的记录主键值数组 | 删除一组给定 ID 的记录后，保存多条记录, 不存在创建, 存在更新, 返回 ID 集合 [示例](#eachsaveafterdelete) [文档](./model/EachSaveAfterDelete) |

### 数据结构

#### 查询条件

#### 记录

#### 分页查询结果

## 示例

### Find

### Get

### Paginate

### Create

### Update

### Save

### Delete

### Destroy

### Insert

### UpdateWhere

### DeleteWhere

### DestroyWhere

### EachSave

### EachSaveAfterDelete
