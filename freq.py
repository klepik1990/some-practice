import collections

a=[1, 2, 2, 2, 1, 3, 2, 0, 2, 1, 3, 2, 4, 0, 4]
counter = collections.Counter(a)
print (counter.most_common(3))