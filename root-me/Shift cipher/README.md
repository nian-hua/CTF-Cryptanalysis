###
###    Date:2018-08-19
###   Time:08:17 GMT
###  Author:nianhua
###

解密脚本如下：
````
fr = open('ch7.bin','rb')

string = fr.read()

for i in range(128):

    for j in string:

        print(chr(j-i),end="")

    print("")

fr.close()
````
