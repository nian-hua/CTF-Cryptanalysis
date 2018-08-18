###
###    Date:2018-08-19
###   Time:08:17 GMT
###  Author:nianhua
###

通过分析题意可知，此加密文件原为bmp图片，所以可以根据bmp文件头推算出加密密钥：102,97,108,108,101,110</br>


解密脚本如下：
````
fr = open('ch3.bmp','rb+')

string =  fr.read()

fr.close()

newstring = ""

for i in range(len(string)):

    if i%6 == 0:

        newstring += chr(string[i] ^ 102)

    elif i%6 == 1:

        newstring += chr(string[i] ^ 97)
    
    elif i%6 == 2:

        newstring += chr(string[i] ^ 108)
    
    elif i%6 == 3:

        newstring += chr(string[i] ^ 108)
    
    elif i%6 == 4:

        newstring += chr(string[i] ^ 101)
    
    elif i%6 == 5:
    
        newstring += chr(string[i] ^ 110)

fw = open('out.bmp','wb+')

fw.write(newstring.encode(encoding="latin1"))

fw.close()

#print(newstring)

````
