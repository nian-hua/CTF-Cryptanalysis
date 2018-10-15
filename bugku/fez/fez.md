````
import os

def xor(a,b):
    assert len(a)==len(b)             a和b的长度务必相同
    c=""
    for i in range(len(a)):
        c+=chr(ord(a[i])^ord(b[i]))
    return c

def f(x,k):
    return xor(xor(x,k),7)

def round(M,K):                m是变的      K[i]
    
    L=M[0:27]                  M 的左半部分
    
    R=M[27:54]                 M 的右半部分
    
    new_l=R                    新的左 = 旧的右
    
    new_r=xor(xor(R,L),K)      异或处理
    
    return new_l+new_r         返回新字符串

def fez(m,K):
    
    for i in K:              一共循环7次

        m=round(m,i)         依次把m和k[i]进行round
    
    return m

K=[]                            K = 空数组

for i in range(7):
    K.append(os.urandom(27))    7*27个随机字符

m=open("flag","rb").read()      m是读取flag中的内容

assert len(m)<54                m的长度小于54

m+=os.urandom(54-len(m))        使用随机值补全到54

test=os.urandom(54)             test是54个随机值

print test.encode("hex")        test的hex

print fez(test,K).encode("hex") fez test和K    --》可以求出k

print fez(m,K).encode("hex")。   fez m和K       --》可以求出m --〉flag



round一共执行了7次 --》。   第一次用的是K[0]

                          最后一次用的是k[6]



                        如果要求k，首先要知道test  


                        左边  右边

                        新的左边 = 右边

                        新的右边 = xor(xor(左边,右边),K)

                        新的右边 

                        新的左边 -- 旧的右边


                        K = （xor(旧的左边，旧的右边)，新的右边）

````
````
6e8a78be3a7c92f74db065a6a18cc659de4278f24af163c435853c06d2a0adeb49859c78dccdf8c85e5ed8cda7e22d6f098e6b1e4142
944360ff8ecd3a4d66b27dfcf7d9c1b5d22f53a9eb84edd29d2a4cc851abea669afaef060b5d1241338f92546a97d1d7ce00fa7b5e3e
a0a9f3660de9c2e347a141054548088827c481868b86473fc590aaf45d21aaa4a4f5c51ecd6812254be19d20f50b3aa24fa0bc7316dc
````
