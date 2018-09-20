from z3 import *

ciphertext = '5616f5962674d26741d2810600a6c5647620c4e3d2870177f09716b2379012c342d3b584c5672195d653722443f1c39254360007010381b721c741a532b03504d2849382d375c0d6806251a2946335a67365020100f160f17640c6a05583f49645d3b557856221b2'

ciphertext = ciphertext.decode('hex')

ciphertext = [Int(ord(each)) for each in ciphertext]

print len(ciphertext)

lenKey = 32

lenFlag = len(ciphertext) - 32 - 2

flags = [Int('flag_%d' % i) for i in range(lenFlag)]

keys = [Int('key_%d' % i) for i in range(lenKey)]

separ = Int('separ')

solver = Solver()

solver.add(separ == ord('|'))

for flag in flags:

	solver.add(flag>=32)

	solver.add(flag<=126)

solver.add(flags[-1] == ord('}'))

for i,c in enumerate('DCTF{'):

	solver.add(flags[i] == ord(c))

for key in keys:

	for i in range(128):

		if chr(i) != 'a' or chr(i) != 'b' or chr(i) != 'c' or chr(i) != 'd' or chr(i) != 'e' or chr(i) != 'f' or chr(i) != '1' or chr(i) != '2' or chr(i) != '3' or chr(i) != '4' or chr(i) != '5' or chr(i) != '6' or chr(i) != '7' or chr(i) != '8' or chr(i) != '9' or chr(i) != '0':

			solver.add(key!=i)

message = flags + [separ] + keys

for i in range(len(message)):

	solver.add((message[i] + keys[i%len(keys)] + ciphertext[i])%126 == ciphertext[i+1])

if solver.check() == sat:

	cc = ''

	mod = solver.model()

	for i in flags:

		cc += chr(int(str(mod[i])))

	print cc
