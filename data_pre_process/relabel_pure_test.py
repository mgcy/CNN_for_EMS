'''
If the compressed label is eligible, write the label, else write 999.
Parameters:
    f1: the original label file
    f2: the output label file
'''

import statistics
import collections

f1 = open("D:\Academic\data_nvspl\SRCID_LAKE017_replaced_labels.txt", 'r')
f2 = open("D:\Academic\data_nvspl\SRCID_LAKE017_re_labels_pure.txt", 'w')
window_size = 30
confuse_tolerance = 3

# Read the labels
labels = [int(l.split()[0]) for l in f1]
# Then the size of image will be 33 x 30

window_num = len(labels) / window_size

for i1 in range(int(window_num)):
    list1 = labels[window_size * i1:window_size * (i1 + 1)]
    try:
        label = statistics.mode(list1)
        # If Jet
        if label == 0:
            if list1.count(1) <= confuse_tolerance and list1.count(2) <= confuse_tolerance and list1.count(
                    4) <= confuse_tolerance:
                f2.write(str(label) + '\n')
            else:
                f2.write(str(999) + '\n')
        # If Prop
        if label == 1:
            if list1.count(0) <= confuse_tolerance and list1.count(2) <= confuse_tolerance and list1.count(
                    4) <= confuse_tolerance:
                f2.write(str(label) + '\n')
            else:
                f2.write(str(999) + '\n')
        # If Heli
        if label == 2:
            if list1.count(1) <= confuse_tolerance and list1.count(0) <= confuse_tolerance and list1.count(
                    4) <= confuse_tolerance:
                f2.write(str(label) + '\n')
            else:
                f2.write(str(999) + '\n')
        # If unknown
        if label == 3:
            if list1.count(1) <= confuse_tolerance and list1.count(2) <= confuse_tolerance and list1.count(
                    4) <= confuse_tolerance and list1.count(0) <= confuse_tolerance:
                f2.write(str(label) + '\n')
            else:
                f2.write(str(999) + '\n')
        # If just aircraft
        if label == 4:
            f2.write(str(999) + '\n')

    except statistics.StatisticsError:
        f2.write(str(999) + '\n')

f1.close()
f2.close()

# print some information about new labels
f3 = open("D:\Academic\data_nvspl\SRCID_LAKE017_re_labels_pure.txt", 'r')
new_labels = [int(l.split()[0]) for l in f3]
print('Labels counter after re-label: ')
print(collections.Counter(new_labels))
f3.close()
