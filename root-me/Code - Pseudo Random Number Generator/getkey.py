
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

def main():

    for  i in range(1354376984,1356882584):

        test = keyt(i)

        if test[:3] == 'aM5':

            print("The num is :%d"%i)


if "__main__" == __name__:

    main()

