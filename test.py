import re
s1 = 'rfv7788 013ab 5566wsx '
m = re.findall( r'[0-9]+[a-zA-Z]+', s1)
print m