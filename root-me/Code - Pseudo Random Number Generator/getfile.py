charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

def keyt(time):

    password = ''

    for i in range(32):
    
        time = (time * 214013 + 2531011)

        ceshi  = time >> 16 & 0x7fff
        
        password += charset[ceshi%61]

    return password

def alpher32xor(key,crypto):

    plantext = ""
    
    for i in range(len(key)):
       
        temp = ord(key[i]) ^ crypto[i] 
        
        if -1 < temp < 127 or temp == 32 :
            
            plantext += chr(temp)
    
        else:

            return -1

    return plantext


def filexor(key,string):

    plantextcc = ""
 
    for i in range(len(string)//32):

        temp = alpher32xor(key,string[i*32:(i+1)*32:])

        if temp == -1:

            return -1
        
        else:
        
            plantextcc += temp

    print("\n%s"%plantextcc)

    return 1


def newxorchar(num1,char2):
    
    return chr(num1 ^ ord(char2))


def newfile(key,string):

    newplantext = ""

    for i in range(len(string)):

        newplantext += newxorchar(string[i],key[i%32])

    return newplantext

def main():

    thiskey = input("This key:")

    fr = open('ming.crypt','rb+')
    
    string = fr.read()
    
    fr.close()

    newstring = newfile(keyt(int(thiskey)),string)

    fw = open('ming.bz2','wb+')

    fw.write(newstring.encode(encoding='latin1'))

    fw.close()

if "__main__" == __name__:

    main()
