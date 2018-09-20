import base64
from z3 import *

ciphertext =  'BCU8EGwlJzAdBjAcGCgaFxgsNyEKIy9iOBxDLwFePVtEIj1kOxBsJisnCg1jHFd4HQ0GaSYnF2wuLDIKT2MJVjxVDA5pKScQOGEuOBkGYwFMeAYLSyg3chcjYSQ0Cg9jBld4AQsZPTEgCiImYiMKBDENTCtVAgQ7ZCUCPzUnNU8aJglKK1lEBSwyNxFsKiw+GEM3AF14FxEZJy08BGwyKjACBmMHXngURAYsJTxDLS8mcR8GNxxBeAUFGD1/chAjYS44GQZjHFA5AUhLLT07DSttYjkKQy4BXzABRBgoPWhDLS0ucQIaYwRRPhBISygoPkMhOGIiGxEmBl8sHUQcLDY3QysoNDQBQzcHGCwdAUsvLTwGPzViMg4WMA0YMRtECiUochckJGImABEvDBR4AQwOaSI7BCQ1YjcAEWMcUD1VKAIrISACOCgtP08MJUh1ORsPAicgfEMEJDA0TwowSEwwEEQbOy0oBmwnLSNPFysBS3gZAR0sKGhDKi0jNhQ3Kw1nNRQDAiobJQw+JR04HDw7B0olCS0vGyceIg4QLTIsC3swTTwe'



ciphertext = base64.b64decode(ciphertext)

lencipher = len(ciphertext)

cipher=[BitVecVal(ord(each),8) for each in ciphertext]

for keyLen in range(1,lencipher-1):

	keys,flags,separ = None,None,None

	keys = [BitVec('key_%i' % i ,8) for i in range(keyLen)]

	flags = [BitVec('flag_%i' % i ,8) for i in range(lencipher-keyLen-1)]

	separ = BitVec('separ',8)

	plaintext = flags+[separ]+keys

	solver = Solver()

	for i in range(len(plaintext)):

		solver.add(plaintext[i]^keys[i%keyLen]==cipher[i])

	solver.add(separ==ord('|'))

	if solver.check()==sat:
		print keyLen,lencipher-keyLen
		cc = ''

		mod = solver.model()

		for flag in flags:
			cc += chr(int(str(mod[flag])))

		print cc
