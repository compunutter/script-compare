
## takes the input string and splits it into a list ##
#string = input('> ').split('|')
string = 'TJ | Christopher Thompson III'.split('|')

## creates the banner lists ##
bantop = []
banmid = []

## creates a list for the *** on the top and bot of the banner ##
## creates a list of the string inputs with * before and after each item ##

for x in range(len(string)):
    banmid.append("*{}*".format(string[x]))
    bantop.append("{}".format('*'*len(banmid[x])))

## prints the lists created in a banner format
print('{0}\n{1}\n{0}'.format(" ".join([str(x) for x in bantop]), " ".join([str(x) for x in banmid] )))


## Test String ##
'''
TJ | Christopher Thompson III
'''
