#x = input('Please type your name')
x = 'TJ | Christopher Thompson III'

def banner():
    bst=(len(x)+4)
    while bst>0:
        print ('*', end='')
        bst = bst - 1

def text():
    print ('\n''*',x, '*')

banner()
text()
banner()
