#name = input('Whats the name you would like to be in banner')
name = 'TJ | Christopher Thompson III'
#Ask's for what name you wish to be in the banner

def Banner(name, star='*'): #making a function, setting the star to = *
    banner = star * (len(name) + 4) #TheBanner will print 4 more * than there are letters
    print(banner) #Prints the top of the banner
    print('{0} {1} {0}'.format(star,name)) #Prints the middle of the banner the {0} prints * and the {1} prints the name
    print(banner) #Prints the bottom of the banner

print(Banner(name))
