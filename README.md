# 华中师范大学小雅平台学习时长统计分析

- [华中师范大学小雅平台学习时长统计分析](#华中师范大学小雅平台学习时长统计分析)
  - [网络分析](#网络分析)
  - [模拟发送](#模拟发送)
  - [其他](#其他)


## 网络分析

打开一个课程，使用控制台进行网络分析

通过网络监听

![image-20240331140852362](https://cdn.jsdelivr.net/gh/zzh-0/Pic@img/img/202403311408409.png)

找到 `learnRecord` ，根据名称就可以判断其为学习时长统计

查看标头

> - **请求网址:** https://ccnu.ai-augmented.com/api/jx-iresource/learnLength/learnRecord
>
> - **请求方法:** POST

![image-20240331142045825](https://cdn.jsdelivr.net/gh/zzh-0/Pic@img/img/202403311420859.png)

对时间进行分析，发现为每隔一分钟发送一次

![image-20240331141638648](https://cdn.jsdelivr.net/gh/zzh-0/Pic@img/img/202403311416705.png)

![image-20240331141559497](https://cdn.jsdelivr.net/gh/zzh-0/Pic@img/img/202403311415555.png)

查看载荷，每次请求的载荷都一样

![image-20240331141833185](https://cdn.jsdelivr.net/gh/zzh-0/Pic@img/img/202403311418219.png)

对载荷内容进行分析

> - `clientType`  身份类型
> - `group_id`  班级id
> - `resourceId`  当前任务id
> - `roleType`  身份类型
> - `user_id`  用户id，非手机号



**响应结果**

![image-20240331150319844](https://cdn.jsdelivr.net/gh/zzh-0/Pic@img/img/202403311503883.png)

对多个响应结果进行分析，以下参数值会发生变化

> - `partition`  无规律
> - `baseOffset`  无规律
> - `logAppendTime`  **不断增加**，猜测为记录的时间，但是未呈现递增趋势

## 模拟发送

代码如下

```python
import requests

url = 'https://ccnu.ai-augmented.com/api/jx-iresource/learnLength/learnRecord'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

if __name__ == '__main__':
    group_id = input('group_id: ')
    resourceId = input('resourceId: ')
    user_id = input('user_id: ')
    data = {
    "clientType": 1,
    "group_id": group_id,
    "resourceId": resourceId,
    "roleType": 1,
    "user_id": user_id,
    }
    response = requests.post(url,headers=headers,json=data)
    if response.status_code == 200:    
        print('Request successful: ', response.text)  
    else:  
        print('Request failed: ', response.status_code, response.text)
```

运行发现，服务器对时间没有限制



## 其他

在监听过程中，发现 `global` 这一项，它和 `learnRecord` 一样每隔一分钟发送一次。

笔者猜测其为开发测试的遗留，响应中包含开发者的名称和手机号、测试用的手机号、测试 ip 等

![image-20240331145624301](https://cdn.jsdelivr.net/gh/zzh-0/Pic@img/img/202403311456345.png)

希望开发者对其进行处理