地址：http://120.24.86.145:8004/index1.php </br>

````
<?php  

error_reporting(0);                            //关闭报错提示
include "flag1.php";                           //包含文件 flag1.php
highlight_file(__file__);                      //对文件进行语法高亮显示
if(isset($_GET['args'])){                      //条件判断 get方法传递的args参数是否存在存在为真
    $args = $_GET['args'];                     //赋值给变量  $args
    if(!preg_match("/^\w+$/",$args)){          //正则表达式判断
                                               //正则表达式格式 为：开头 /^   结尾 $/   \w 代表任意大小写字母和数字  不包括特殊符号  +为连接符 
                                               //if条件判断 $args 是否符合正则表达式格式   不符合返回true    (函数取反) 
        die("args error!");                    //输出 args error！  
    }
    eval("var_dump($$args);");                 //eval()函数 将字符串作为php代码执行结尾加分号    
                                               //var_dump()函数 显示关于一个或多个表达式的结构信息，包括表达式的类型与值。数组将递归展开值，通过缩进显示其结构。
}
?>
````


$$args 可以理解为$($args)    </br>

````
eg:

 $a="hello world!";

 $args="a";

 echo $$args;   输出结果为： hello world!  
````
$$args 可以理解为$($args)   
````
eg:

 $a="hello world!";

 $args="a";

 echo $$args;   输出结果为： hello world!  
 
 ````
