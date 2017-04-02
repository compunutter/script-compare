## takes the input string and splits it into a list ##
#string = input('> ').split(' | ')
string = 'TJ | Christopher Thompson III'.split(' | ')

## creates the banner lists ##
bantop = []
banmid = []

## creates a list for the *** on the top and bot of the banner ##
for x in range(len(string)):
    bantop.append('*'*int(len(string[x])+2)+' ')

## creates a list of the string inputs with * before and after each item ##
for x in range(len(string)):
    banmid.append('*'+string[x]+'* ')

## prints the lists created in a banner format
print("".join([str(x) for x in bantop] )+'\n'+"".join([str(x) for x in banmid] )+'\n'+"".join([str(x) for x in bantop] ))
