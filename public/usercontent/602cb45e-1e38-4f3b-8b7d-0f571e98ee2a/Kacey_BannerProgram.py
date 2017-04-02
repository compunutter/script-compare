text = "TJ | Christopher Thompson III"

def bannermid(text, ch='*', length=33):
    spaced_text = ' %s ' % text
    banner = spaced_text.center(length, ch)
    print(banner)

def bannertop(ch='*', length=33):
    spaced_text = ""
    banner = spaced_text.center(length, ch)
    print(banner)
    
bannertop()
bannermid(text)
bannertop()
