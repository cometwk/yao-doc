**`hasOne`示例**

**模型示例**

user 和 profile :

```js
// user.mod.json 模型ID=user
({
  name: '用户',
  table: { name: 'user' },
  columns: [
    { name: 'id', label: 'ID', type: 'increments', primary: true },
    { name: 'name', label: '命名', type: 'string' },
    { name: 'email', label: '邮箱', type: 'string', unique: true },
  ],
})
// profile.mod.json 模型ID=profile
({
  name: '用户资料',
  table: { name: 'profile' },
  columns: [
    { name: 'id', label: 'ID', type: 'increments', primary: true },
    { name: 'user_id', label: 'user表关联', type: 'integer', unique: true },
    { name: 'bio', label: '个人简介', type: 'string' },
  ],
})
```

**建立关系**

在模型文件 `profile.mod` 中, 建立关系  `profile.user_id = user.id` 。

```js
// profile.mod.json
({
  table: { name: 'profile' },
  // ...
  relations: {
    user: {
      type: 'hasOne', // 关系类型
      model: 'user',  // 和 user 关联
      key: 'id',  // key 和 foreign 一起使用
      foreign: 'user_id', // profile.user_id = user.id 
      query: { select: ['name', 'email'] }, // 查询user表的字段
    },
  },
})
```

**使用**

```
yao run models.profile.Find 
```

引擎解析后的 SQL 为:

```sql
SELECT `user`.*,
  `manu`.`short` AS `user_manu_short`,
  `manu`.`company` AS `user_manu_company`,
  FROM `user` AS `user`
  LEFT JOIN `manu` as `user_manu` ON `user_manu`.`id` = `user`.`manu_id`
```

**访问**

在调用 `process` 查询时，传入 `with` 参数，即可同时返回厂商信息

```bash
GET /api/profile/find/1?with=user&user.select=id,email
```

