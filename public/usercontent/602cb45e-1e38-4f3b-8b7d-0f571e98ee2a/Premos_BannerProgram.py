text = "TJ | Christopher Thompson III"

def sidebanner(text, ch='*', length=33):
    spaced_text = ' %s ' % text
    banner = spaced_text.center(length, ch)
    print (banner)
    
topbanner = "*********************************"
print(topbanner)  

sidebanner(text)
print(topbanner)
