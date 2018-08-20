from math import *

class Railfence:

    def encipher(self,plaintext,key):

        ciphertext = ''

        for j in range(key):
            for i in range(len(plaintext)//key+1):
                try:
                    ciphertext += plaintext[i*key+j:i*key+j+1]
                except:
                    pass
    
        return ciphertext

    def decipher(self,ciphertext,key):

        plaintext = []

        plainstr = ''

        column = len(ciphertext)//key

        remainder = len(ciphertext)%key

        for i in range(key):

            if i < remainder:

                plaintext.append(ciphertext[:column+1])
    
                ciphertext = ciphertext[column+1:]

            else:

                plaintext.append(ciphertext[:column])

                ciphertext = ciphertext[column:]

        for i in range(column+1):

            for j in range(key):

                try:
                    plainstr += plaintext[j][i]
                except:
                    pass

        return plainstr


    def enciphe(self,plaintext,key):

        ciphertext = ''

        v = ceil(len(plaintext)/(2*(key-1)))

        for i in range(key):

            for j in range(v):
 
                try:
                    ciphertext += plaintext[(j*(key-1)*2) + i]
                    if(i != 0 and i != (key-1)):
                        ciphertext += plaintext[(j*(key-1)*2) + (((key-1)*2)-i)]
                
                except:
                    pass
    
        return ciphertext

    def deciphe(self,ciphertext,key):

        cipherarray = []        

        plaintext = ''

        v = ceil(len(ciphertext)/(2*(key-1)))
    
        rv = len(ciphertext)//(2*(key-1))

        re = len(ciphertext)%(2*(key-1))

        maxlen = 0

        cipherarray.append(ciphertext[:v])
        
        ciphertext = ciphertext[v:]
        
        if  re <= (key-1):

            for i in range(re-1):

                cipherarray.append(ciphertext[:2*rv+1])

                ciphertext = ciphertext[2*rv+1:]
            
            for i in range(key-(re+1)):
            
                cipherarray.append(ciphertext[:2*rv])

                ciphertext = ciphertext[2*rv:]
            
            cipherarray.append(ciphertext)
            
            ciphertext = ''
       
        else:        

            for i in range(2*key-re-2):

                cipherarray.append(ciphertext[:2*rv+1])

                ciphertext = ciphertext[2*rv+1:]

            for i in range(re-key):

                cipherarray.append(ciphertext[:(2*rv+2)])

                ciphertext = ciphertext[(2*rv+2):]
            
            cipherarray.append(ciphertext)

            ciphertext = ''

        cipherarray = [i for i in cipherarray if i != '']

        for i in cipherarray:

            if(len(i)>maxlen):

                maxlen = len(i)

        for i in range(ceil(maxlen/2)):

                for j in range(len(cipherarray)):

                    plaintext += cipherarray[j][:1]
                    
                    cipherarray[j] = cipherarray[j][1:]

                for j in range(len(cipherarray)-2,0,-1):
                                        
                    plaintext += cipherarray[j][:1]

                    cipherarray[j] = cipherarray[j][1:]

        return plaintext

def main():

    newobj = Railfence()

    print(newobj.deciphe('Wnb.r.ietoeh Fo"lKutrts"znl cc hi ee ekOtggsnkidy hini cna neea civo lh',8))

if "__main__" == __name__ :

    main()
