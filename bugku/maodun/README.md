地址：http://120.24.86.145:8002/get/index1.php


````
$num=$_GET['num'];
if(!is_numeric($num))
{
echo $num;
if($num==1)
echo 'flag{**********}';
}
````

这个函数中有两个if，要同时满足这两个条件才能够拿到flag。</br>

is_numeric函数，如果num是数字和数字字符串则返回TRUE，否则返回FALSE。</br>

根据题目要求，需要一个字符串才能通过第一个if，这个简单，只要有字符即可。</br>

第二个if是两个等号，所以只要保证第一个字符是1即可。

