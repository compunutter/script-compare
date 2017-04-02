def b(a):
    output = ""
    for x in range(len(a)+4):
                  output += "*"     #what to do that stars are printed in one line
    return output


def bannerfunction(a):
    stars = b(a)
    return("{}\n* {} *\n{}".format(stars, a, stars)) # wenn es nicht funktioniert problem vereinfachen


def findline(a):
    output = ""
    for c in a:
        output += str(c)
        if c == " ":
            break
    return (str(output))

def findline2 (a):
    output2 = ""
    for x in (a[::-1]):
        output2 += str(x)
        if x == " ":
            break
    return (str((output2)[::-1]))
# b(findline(a) funktioniert nicht, weil findline(a) aus irgendeinem grund keine laenge hat

def star(a):
    output = "***" #aus irgendeonem grund nur 3 sterne noetig
    for x in a:
        output += "*"
        if x == " ":
            break
    return (output)

def star2(a):
    output = "***"
    for x in (a[::-1]):
        output += "*"
        if x == " ":
           break
    return (output)

def bannerfunction3(a):
    #stars = star(a)
    #part = findline(a)
    return("{} {}\n* {}* *{} *\n{} {}".format(star(a),star2(a),findline(a),findline2(a),star(a),star2(a)))

def bannerprogram(a):
    if findline2(a) == findline(a):
        print (bannerfunction(a))
    else:
        print (bannerfunction3(a))

bannerprogram('TJ | Christopher Thompson III')
