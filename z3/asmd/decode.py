from z3 import *


flags = [Int('flag_%d' % i) for i in range(20)]

solver = Solver()


solver.add(flags[15]+flags[4]==10)
solver.add(flags[1]*flags[18]==2)
solver.add(flags[15]/flags[9]==1)
solver.add(flags[17]-flags[0]==4)
solver.add(flags[5]-flags[17]==-1)
solver.add(flags[15]-flags[1]==5)
solver.add(flags[1]*flags[10]==18)
solver.add(flags[8]+flags[13]==14)
solver.add(flags[18]*flags[8]==5)
solver.add(flags[4]*flags[11]==0)
solver.add(flags[8]+flags[9]==12)
solver.add(flags[12]-flags[19]==1)
solver.add(flags[9]%flags[17]==7)
solver.add(flags[14]*flags[16]==40)
solver.add(flags[7]-flags[4]==1)
solver.add(flags[6]+flags[0]==6)
solver.add(flags[2]-flags[16]==0)
solver.add(flags[4]-flags[6]==1)
solver.add(flags[0]%flags[5]==4)
solver.add(flags[5]*flags[11]==0)
solver.add(flags[10]%flags[15]==2)
solver.add(flags[11]/flags[3]==0)
solver.add(flags[14]-flags[13]==-4)
solver.add(flags[18]+flags[19]==3)

if solver.check() == sat:

	mod = solver.model()

	cc = ''

	for flag in flags:

		cc += str(mod[flag])
	print cc
