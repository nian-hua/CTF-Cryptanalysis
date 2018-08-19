###
###    Date:2018-08-19
###   Time:08:17 GMT
###  Author:nianhua
###

这个题考的是伪随机数生成器的题：首先要猜测到产生的随机数是多少：</br>
提示已经提示文件是BZ2根据文件头为aM5</br>
已知明文攻击：使用脚本getkey.py推测出12月的所有可能的随机数为：
````
└──╼ #python3 filexor.py 
fThe num is :1354709136
The num is :1355457619
The num is :1355486676
The num is :1355515733
The num is :1356145021
The num is :1356165071
The num is :1356174078
The num is :1356194128
The num is :1356414619
The num is :1356475333
The num is :1356724881
The num is :1356744931
````
分别使用以上密钥对加密后的文件进行解密(getfile.py)：</br>
当然只有一个是正确的~
````
└──╼ #python3 newxor.py 
This key:1354709136
````
会输出一个解密后的文件，解压之后找到flag
