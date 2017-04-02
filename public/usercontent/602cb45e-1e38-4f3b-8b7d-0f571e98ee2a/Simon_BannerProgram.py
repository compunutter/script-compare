banner_input = "TJ | Christopher Thompson III"

place = banner_input.find("|")

first, second = banner_input[0:place-1], banner_input[place+2:]

first_s, second_s = "*"*(len(first)+4), "*"*(len(second)+4)

constructed = "{}   {}".format(first_s, second_s)

print("{}\n* {} *   * {} *\n{}".format(constructed, first, second, constructed))
