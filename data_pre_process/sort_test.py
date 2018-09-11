lines = open("D:\Academic\data_nvspl\SRCID_LAKE017_expand_labels_test.txt", 'r').readlines()
f2 = open("D:\Academic\data_nvspl\SRCID_LAKE017_expand_labels_sort_test.txt", 'w')

# f2.write(''.join(sorted(f1, key=lambda s: s.split()[2], reverse=False)))
for line in sorted(lines, key=lambda line: int(line.split()[2])):
    f2.write(line)

f2.close()
