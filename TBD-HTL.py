import itertools

num = 223336226

def sol(num):
    src =  str(num)
    groups = [ ''.join(list(g)) for k, g in itertools.groupby(src)]
    res = []
    length = len(groups)
    for i in xrange(length):
        if len(groups[i]) >=2:
            if i < length -1:
                res.append(
                  int(''.join(groups[:i]+[groups[i][1:]]+groups[i+1:])) )
            else:
                res.append(
                  int(''.join(groups[:i]+[groups[i][1:]])) )
    return max(res)

print sol(num)
