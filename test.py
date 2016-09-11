import itertools
src = '223336226'
groups = [ ''.join(list(g)) for k, g in itertools.groupby(src)]
print groups