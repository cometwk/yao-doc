# FileSystem

<blockquote>
  使用 FS 对象实现文件操作。 Yao 提供 System, DSL, Script 三个空间, System
  用于应用数据操作, DSL 用于DSL文件操作, Script 用于脚本文件操作; DSL 和 Script
  只能用于 stuido 脚本。
</blockquote>

**约定**

1. 示例中约定应用根目录为 `/data/app`, 实际编写时需替换为应用根目录。
2. 使用 `<>` 标识自行替换的内容。 例如: `icon-<图标名称>`, 实际编写时应替换为: `icon-foo`, `icon-bar` ...

| 空间    | 根目录            | 说明                                          |
| ------- | ----------------- | --------------------------------------------- |
| system  | /data/app/data    | 应用数据                                      |
| dsl     | /data/app         | 除 `scripts` 外的所有目录(仅 Studio 脚本可用) |
| scripts | /data/app/scirpts | 脚本目录(仅 Studio 脚本可用)                  |

**示例**

**System**

`/data/app/scripts/test.js`

```javascript
function ReadFile() {
  let fs = new FS("system");
  let data = fs.ReadFile("/f1.txt"); // /data/app/data/f1.txt
  return data;
}

function WriteFile() {
  let fs = new FS("system");
  let length = fs.WriteFile("/f2.txt", "hello", 0644); // /data/app/data/f2.txt
  return length;
}
```

**DSL**

`/data/app/studio/test.js`

```javascript
function ReadFile() {
  let fs = new FS("dsl");
  let data = fs.ReadFile("/models/f1.mod.json"); // /data/app/models/f1.mod.json
  return data;
}

function WriteFile() {
  let fs = new FS("dsl");
  let data = {
    name: "用户",
    table: { name: "f1" },
    columns: [{ label: "ID", name: "id", type: "ID" }],
  };
  let length = fs.WriteFile("/models/f2.mod.json", data, 0644); //  /data/app/models/f2.mod.json
  return length;
}
```

**Script**

```javascript
function ReadFile() {
  let fs = new FS("script");
  let data = fs.ReadFile("/f1.js"); // /data/app/scripts/f1.js
  return data;
}

function WriteFile() {
  let fs = new FS("script");
  let script = `
    function Foo() {
      return "Bar"
    }
  `;
  let length = fs.WriteFile("/models/f2.js", script, 0644); // /data/app/scripts/f2.js
  return length;
}
```

## API

```javascript
var fs = new FS("system");
var dataString = fs.ReadFile("/path/name.file");
var dataUnit8Array = fs.ReadFileBuffer("/path/name.file");
var length = fs.WriteFile("/path/name.file", "Hello");
var length = fs.WriteFile("/path/name.file", "Hello", 0644);
var length = fs.WriteFileBuffer("/path/name.file", dataUnit8Array);
var length = fs.WriteFileBuffer("/path/name.file", dataUnit8Array, 0644);
var dirs = fs.ReadDir("/path");
var dirs = fs.ReadDir("/path", true); // recursive
var err = fs.Mkdir("/path");
var err = fs.Mkdir("/path", 0644);
var err = fs.MkdirAll("/path/dir");
var err = fs.MkdirAll("/path/dir", 0644);
var temp = fs.MkdirTemp();
var temp = fs.MkdirTemp("/path/dir");
var temp = fs.MkdirTemp("/path/dir", "*-logs");
var ok = fs.Exists("/path");
var ok = fs.IsDir("/path");
var ok = fs.IsFile("/path");
var ok = fs.Remove("/path");
var ok = fs.RemoveAll("/path");
var err = fs.Chmod("/path", 0755);
var res = fs.BaseName("/path/name.file");
var res = fs.DirName("/path/name.file");
var res = fs.ExtName("/path/name.file");
var res = fs.MimeType("/path/name.file");
var res = fs.Mode("/path/name.file");
var res = fs.Size("/path/name.file");
var res = fs.ModTime("/path/name.file");
var res = fs.Copy("/path/foo.file", "/path/bar.file");
var res = fs.Copy("/path", "/root/new");
var res = fs.Move("/path/foo.file", "/path/bar.file");
var res = fs.Move("/path", "/root/new");
```
