banner_input = "TJ | Christopher Thompson III".split(" | ")

"""
Zach had the idea for the .split(" | ") so that it
can do it for any number of |'s - he has insisted
that I credited him for it.
"""

row, midrow = [], []

for x in banner_input:
    row.append("*"*(len(x)+4)+"   ")
    midrow.append("* {} *   ".format(x))
    
print("{0}\n{1}\n{0}".format("".join(row), "".join(midrow)) )
