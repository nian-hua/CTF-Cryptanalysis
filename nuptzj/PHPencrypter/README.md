###
###    Date:2018-08-25
###   Time:08:17 GMT
###  Author:nianhua
###


先使用在线工具对其进行rot13解密，倒叙，base64解密。</br>
得到字符串
````
~wfssut`eob`57ftbc`eob`42ups|gudo
````
使用脚本：
````
test = '''~wfssut`eob`57ftbc`eob`42ups|gudo'''

for i in test:

    print(chr(ord(i)-1),end='')
````
将输出的字符串倒叙即可




