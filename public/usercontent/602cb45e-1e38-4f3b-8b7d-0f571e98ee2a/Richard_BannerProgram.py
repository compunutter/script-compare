#n = str(input('What is your name?'))
n = str('TJ | Christopher Thompson III')
f = (len(n))
line = f * ('*')

z = n.find ('|')
li = n[z+2:(len(n))]
i = n[0:z]
p = ((len(i))+4) * ('*')
g = ((len(li))+4) * ('*')

if '|' in n:
    print (p,' ',g,'\n','*',i,'*',' ','*',li,'*','\n',p,' ',g)
else:
    print (line,'\n', n, '\n',line)
