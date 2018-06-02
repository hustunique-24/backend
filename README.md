# backend
backend

## API 2.0
### 绑定操作 同时也是注册新用户的操作
**POST /register**

```json
{
    "username": "", //用户名
    "password": "", //密码
    "bao_id": "", //抱枕ID
    "human": null, // 老人的年龄
    "human_status": "", //老人的状态 可以是文字
    "human_xue": null, //老人的血型
    "human_sex": "" //老人的性别
}
```


###登陆
**POST /login** 

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

### 注意接下来所有操作，均需要在Header中绑定字段如下
JWT 后面就是你获取的token

```
Authorization:JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6IndnYiIsImV4cCI6MTUyNzk3ODExOCwiZW1haWwiOiIxQDE2My5jb20ifQ.pjqKbjCUPp2NFkOr8ktDesltA1C3_l5sfV9YmNzZnXI

```


### 获取用户基本信息
**Get /userprofile/<id>/**
例如：Get userprofile/2/
返回：

```json
[
    {
        "url": "http://127.0.0.1:8000/userprofile/2/",
        "bao_id": "123",
        "palce": "",
        "human": 123,
        "human_status": "123",
        "human_xue": 123,
        "human_sex": "123"
    }
]

```


### 获得消息 ？
**GET /api/Message/**

```

{
    "User": 1,
    "type": "sound",
    "time": "2018-06-03T00:01:00Z",
    "content": "hello world"
}


```

### 发送消息 ？
**POST /api/Message/**

```json


```







