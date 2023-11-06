# Schema

<blockquote>
  <p>数据表结构操作处理器</p>
</blockquote>

**约定**

1. 示例中约定应用根目录为 `/data/app`, 实际编写时需替换为应用根目录。
2. 示例中约定服务器地址为 `http://127.0.0.1:5099`, 实际编写时需自行替换。
3. 使用 `<>` 标识自行替换的内容。 例如: `icon-<图标名称>`, 实际编写时应替换为: `icon-foo`, `icon-bar` ...

## 处理器

**`<ID>` 为 `Connector Widget ID`** 查看[使用 Widgets](../基础/使用Widgets)文档

| 处理器                    | 参数表                               | 返回值         | 说明                                                                                  |
| ------------------------- | ------------------------------------ | -------------- | ------------------------------------------------------------------------------------- |
| schemas.<ID\>.Create      | `[<数据库名称>]`                     | -              | 创建一个数据库(或 Schema) [示例](#create) [文档](./Schema/Create)                     |
| schemas.<ID\>.Drop        | `[<数据库名称>]`                     | -              | 删除一个数据库(或 Schema) [示例](#drop) [文档](./Schema/Drop)                         |
| schemas.<ID\>.Tables      | `[<数据表前缀(可选)>]`               | 数据表名称数组 | 读取数据表, 返回数据表名称数组 [示例](#tables) [文档](./Schema/Tables)                |
| schemas.<ID\>.TableGet    | `[<数据表名称>]`                     | 数据表结构信息 | 读取数据表结构, 返回数据表结构信息 [示例](#tableget) [文档](./Schema/TableGet)        |
| schemas.<ID\>.TableCreate | `[<数据表名称>, <数据表结构>]`       | -              | 创建一张数据表 [示例](#tablecreate) [文档](./Schema/TableCreate)                      |
| schemas.<ID\>.TableSave   | `[<数据表名称>, <数据表结构>]`       | -              | 保存一张数据表, 不存在创建, 存在更新 [示例](#tablesave) [文档](./Schema/TableSave)    |
| schemas.<ID\>.TableDrop   | `[<数据表名称>]`                     | -              | 删除一张数据表 [示例](#tabledrop) [文档](./Schema/TableDrop)                          |
| schemas.<ID\>.TableRename | `[<数据表名称>, <新数据表名称>]`     | -              | 数据表改名 [示例](#tablerename) [文档](./Schema/TableRename)                          |
| schemas.<ID\>.TableDiff   | `[<数据表结构>, <另一个数据表结构>]` | 两个表结构差异 | 比较两个表结构, 返回两张表差异信息 [示例](#tablediff) [文档](./Schema/TableDiff)      |
| schemas.<ID\>.ColumnAdd   | `[<数据表名称>, <字段结构>]`         | -              | 给数据表添加一个字段 [示例](#columnadd) [文档](./Schema/ColumnAdd)                    |
| schemas.<ID\>.ColumnAlt   | `[<数据表名称>, <字段结构>]`         | -              | 更新字段结构,如字段不存在则添加一个字段 [示例](#columnalt) [文档](./Schema/ColumnAlt) |
| schemas.<ID\>.ColumnDel   | `[<数据表名称>, <字段名称>]`         | -              | 删除一个字段 [示例](#columndel) [文档](./Schema/ColumnDel)                            |
| schemas.<ID\>.IndexAdd    | `[<数据表名称>, <索引结构>]`         | -              | 添加一个索引 [示例](#indexadd) [文档](./Schema/IndexAdd)                              |
| schemas.<ID\>.IndexDel    | `[<数据表名称>, <索引名称>]`         | -              | 删除一个索引 [示例](#indexdel) [文档](./Schema/IndexDel)                              |

### 数据结构

#### 数据表结构

#### 字段结构

#### 索引结构

#### 表结构差异

## 示例

### Create

### Drop

### Tables

### TableGet

### TableCreate

### TableSave

### TableDrop

### TableRename

### TableDiff

### ColumnAdd

### ColumnAlt

### ColumnDel

### IndexAdd

### IndexDel
