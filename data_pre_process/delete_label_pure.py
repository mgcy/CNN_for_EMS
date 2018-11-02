import collections

labels = [int(l.split()[0]) for l in open("D:\Academic\data_nvspl\\SRCID_LAKE017_combine_data_label.txt")]
f1 = open("D:\Academic\data_nvspl\\SRCID_LAKE017_combine_data_label.txt", 'r')
f2 = open("D:\Academic\data_nvspl\\SRCID_LAKE017_delete.txt", 'w')

i1 = 0
for line in f1:
    if labels[i1] != 4:
        f2.write(line)
    i1 = i1 + 1

f1.close()
f2.close()

# check the results
print('Label counter before deleting:')
print(collections.Counter(labels))
new_labels = [int(l.split()[0]) for l in open("D:\Academic\data_nvspl\\SRCID_LAKE017_delete.txt")]
print('Label counter after deleting:')
print(collections.Counter(new_labels))
