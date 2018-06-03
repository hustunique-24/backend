# backend
backend

## API 2.0
### API ROOT
**http://hack.laphets.com:8080/**
### 绑定操作 同时也是注册新用户的操作
**POST /register**

```json
{
    "username": "", //用户名
    "password": "", //密码
    "bao_id": "", //抱枕ID
    "human_age": null, // 老人的年龄
    "human_status": "", //老人的状态 可以是文字
    "human_xue": null, //老人的血型
    "human_sex": "" //老人的性别
}
```
### 获取个人信息 

**GET /api/userprofile/**

```json

[
    {
        "url": "http://hack.laphets.com:8080/api/userprofile/1/", //详细信息
        "bao_id": "123-456-789", // 抱枕id
        "UserProfile_Message": [], // 当前用户发送的信息
        "palce": "", //用户地址
        "human_age": 18, // 年龄
        "human_status": "hhh", // 老人状态
        "human_xue": "B", // 老人血型
        "human_sex": "男" // 老人性别
    }
]


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
**Get /userprofile/id/**

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
**POST /Message/**

```json

{
    "User":“http://hack.laphets.com:8080/userprofile/1/”, 发送的是 用户对应的url
    "type": "text", // 消息类型 目前只有 text
    "time": “2018-06-03T10:11:00Z”, // 发送时间 格式为2018-06-03T10:11:00Z
    "content": "" //内容
}

```







