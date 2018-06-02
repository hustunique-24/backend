# backend
backend

## API 1.0
###登陆

**POST /api-auth** 

```json
{
    "username": "",
    "password": ""
}
```

若密码正确返回：

```json

{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6IndnYiIsImV4cCI6MTUyNzk1ODgxMywiZW1haWwiOiIxQDE2My5jb20ifQ.Ihrnc3vAB-w_WbuHSupm2oZoRjCOkq36m3F-uTACe_Q"
}

```
若密码错误返回：

```json

{
    "non_field_errors": [
        "Unable to log in with provided credentials."
    ]
}
```

### 

### 绑定操作
**POST /api/User**

```json
{
    "bao_id": "",
    "owner_id": "",
    "password": "",
    "human1_age": null,
    "human1_status": "",
    "human2_age": null,
    "human2_status": "",
    "ip": ""
}
```

### 获得消息
**GET /api/Message/**

```

{
    "User": 1,
    "type": "sound",
    "time": "2018-06-03T00:01:00Z",
    "content": "hello world"
}


```

### 发送消息
**POST /api/Message/**

```json


```







