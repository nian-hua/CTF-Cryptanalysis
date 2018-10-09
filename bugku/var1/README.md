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

eval()函数存在命令执行漏洞  我们的目标是查看flag1.php中的flag 首先想到的是本地包含漏洞查看源码  或者上传一句话木马等思路 </br>

而本题条件判断加了正则表达式判断，过滤了括号和引号等字符。无法构造！  但输出时是   $$args  我们想到构造 php中超全局变量 $GLOBALS </br>

最后补充一点  很多人都认为global和$GLOBALS[]只是写法上面的差别，其实不然。  前者为变量实体 后者为别名引用eg：
````
<?php
$var1 = 1;
function test(){
unset($GLOBALS['var1']);
}
test();
echo $var1;
?>
````
因为$var1被删除了，所以什么东西都没有打印。
````
<?php
$var1 = 1;
function test(){
global $var1;
unset($var1);
}
test();
echo $var1;
?>
````
意外的打印了1。证明删除的只是别名，$GLOBALS['var']的引用，起本身的值没有受到任何的改变。验证了我们之前所说的东西 


