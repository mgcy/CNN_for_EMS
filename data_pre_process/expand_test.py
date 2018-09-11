date_time = [str(l.split()[0]) for l in open("D:\Academic\data_nvspl\SRCID_LAKE017_expand_labels_sort_test.txt")]
hr = [str(l.split()[1]) for l in open("D:\Academic\data_nvspl\SRCID_LAKE017_expand_labels_sort_test.txt")]
start_time = [str(l.split()[2]) for l in open("D:\Academic\data_nvspl\SRCID_LAKE017_expand_labels_sort_test.txt")]
len_time = [str(l.split()[3]) for l in open("D:\Academic\data_nvspl\SRCID_LAKE017_expand_labels_sort_test.txt")]
labels = [str(l.split()[4]) for l in open("D:\Academic\data_nvspl\SRCID_LAKE017_expand_labels_sort_test.txt")]

f1 = open("D:\Academic\data_nvspl\SRCID_LAKE017_expand_labels.txt", 'w')

len_labels = len(hr)
for i in range(0, 3600):
    for m in range(len_labels):
        print(str(m)+' '+str(i))

        if i < int(start_time[m]):
            f1.write('0\n')
            break
        if i >= int(start_time[m]) and i <= (int(start_time[m]) + int(len_time[m])):
            f1.write(labels[m] + '\n')
            break
        if i > (int(start_time[len_labels - 1]) + int(len_time[len_labels - 1])):
            f1.write('0\n')
            break


f1.close()
