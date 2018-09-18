###
###    Date:2018-08-19
###   Time:08:17 GMT
###  Author:nianhua
###

通过分析题意可知，此加密文件原为bmp图片，所以可以根据bmp文件头推算出加密密钥：102,97,108,108,101,110</br>


解密脚本如下：
````
key = 'kelaibei'

keyLen = len(key)

fr = open('encode.png','rb+')

string =  fr.read()

fr.close()

newstring = ""

for i in range(len(string)):

 newstring += chr(string[i] ^ ord(key[i%keyLen]))

fw = open('out.png','wb+')

fw.write(newstring.encode(encoding="latin1"))

fw.close()
````
