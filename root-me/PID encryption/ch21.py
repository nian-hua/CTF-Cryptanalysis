from pwn import *

context.log_level = 'debug'

shell  = ssh('cryptanalyse-ch21','challenge01.root-me.org',password='cryptanalyse-ch21',port=2221)

p = shell.run('sh')

def sd(cont):
	p.sendline(cont)
def cv(cont):
	return p.recvuntil(cont)

sd('./ch21 12345')
temp =  cv('Fail')[8:-4]

print temp


name = "ch21"

ch = process(name)

ch.sendline(temp)

temp = ch.recvline()

temp = temp.replace('$','\$')

print temp

sd('./ch21 ' + temp)

p.recvline()

p.interactive()
