import collections
f1 = open("D:\Academic\data_nvspl\SRCID_LAKE016.txt")
next(f1)
labels = [str(l.split()[4]) for l in f1]
print('LAME007:')
print(collections.Counter(labels))
f1.close()