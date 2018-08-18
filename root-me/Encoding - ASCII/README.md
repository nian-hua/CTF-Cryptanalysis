###
###    Date:2018-08-19
###   Time:08:17 GMT
###  Author:nianhua
###


解密脚本如下：

````
hexadecimalcontrast = {
        '0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'a':'1010',
        'b':'1011',
        'c':'1100',
        'd':'1101',
        'e':'1110',
        'f':'1111',
        }

def BinToStr(strbin):
    "Turn the binary string to a ASCII string"

    strten = ""  
    for i in range(len(strbin)//8):
        num = 0
        test = strbin[i*8:i*8+8]
        for j in range(8):
            num += int(test[j])*(2**(7-j))
        strten += chr(num)
    return strten

def HexToBin(string):
    "Convert sixteen to binary"

    Binstring = ""
    string = string.lower()
    for i in string:
        try:
            Binstring += hexadecimalcontrast[i]
        except:
            return -1
    return Binstring

def main():

    string = input("please enter 16 binary system:").lower()
    for i in range(len(string)//2):
       print(BinToStr(HexToBin(string[i*2:i*2+2])),end='')
    print('')

if "__main__" == __name__:

    main()


````
