# 文件处理

文件处理器。

| 处理器            | 说明                       | 文档                                    |
| ----------------- | -------------------------- | --------------------------------------- |
| xiang.fs.Upload   | 上传文件到应用 `data` 目录 | [查看](../e.处理器参考/a.数据模型#Find) |
| xiang.fs.ReadFile | 读取 `data` 目录下文件内容 | [查看](../e.处理器参考/a.数据模型#Find) |

导出 Excel 操作，新建路由文件：`/apis/utils.http.json`代码如下：

```json
{
  "name": "下载Excel",
  "version": "1.0.0",
  "description": "下载Excel",
  "group": "utils",
  "guard": "-",
  "paths": [
    {
      "guard": "-",
      "path": "/export/:name",
      "method": "GET",
      "process": "flows.utils.export",
      "in": ["$param.name"],
      "out": {
        "status": 200,
        "type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "headers": {
          "Content-Disposition": "attachment;filename=导出数据.xlsx"
        }
      }
    }
  ]
}
```

新建文件：`/flows/utils/export.flow.json`代码如下：

```json
{
  "label": "下载",
  "version": "1.0.0",
  "description": "下载",
  "nodes": [
    {
      "name": "文件",
      "process": "xiang.table.Export",
      "args": ["{{$in.0}}", {}, 20]
    },
    {
      "name": "数据",
      "process": "xiang.fs.ReadFile",
      "args": ["{{$res.文件}}", false]
    }
  ],
  "output": "{{$res.数据.content}}"
}
```

假如有一个表格名字叫：`/tables/pet.tab.json`，导出表格的列表数据只需要请求：`/utils/export/pet`

上传文件操作，上传文件名为 file 的文件，新建`/apis/storage.http.json `代码如下：

```json
{
  "name": "存储接口",
  "version": "1.0.0",
  "description": "存储接口API",
  "group": "storage",
  "guard": "bearer-jwt",
  "paths": [
    {
      "path": "/upload",
      "method": "POST",
      "guard": "-",
      "process": "flows.upload",
      "in": ["$file.file"],
      "out": {
        "status": 200,
        "type": "application/json"
      }
    }
  ]
}
```

新建`/flows/upload.flow.json `代码如下：

```json
{
  "label": "上传文件",
  "version": "1.0.0",
  "description": "上传文件",
  "nodes": [
    {
      "name": "上传",
      "process": "xiang.fs.Upload",
      "args": ["{{$in.0}}"]
    }
  ],
  "output": "{{$res.上传}}"
}
```
