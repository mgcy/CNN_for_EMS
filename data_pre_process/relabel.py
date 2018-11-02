# Copyright 2018 Yifan Yang. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
'''
Usage: This code compress the labels into low dimension, which indicated by
        window_size.
Parameters:
    f1: the original label file
    f2: the output label file
    window_size: the size to compress the labels
        e.g., window_size = 30,
        Dim( original label) =  3600
        Dim( new label) = 3600 / 30 = 120
'''
import statistics
import collections


def relabel(window_size):
    # Input parameters
    f1 = open("D:\Academic\data_nvspl\SRCID_LAKE017_replaced_labels.txt", 'r')
    f2 = open("D:\Academic\data_nvspl\SRCID_LAKE017_re_labels.txt", 'w')
    # window_size = 10

    # Read the labels
    labels = [int(l.split()[0]) for l in f1]
    # Then the size of image will be 33 x 30

    window_num = len(labels) / window_size

    for i1 in range(int(window_num)):
        list1 = labels[window_size * i1:window_size * (i1 + 1)]
        list_table = statistics._counts(list1)
        len_table = len(list_table)
        if len_table == 1:
            label = statistics.mode(list1)
            f2.write(str(label) + '\n')
        else:
            list2 = []
            print(i1)
            for i2 in range(len_table):
                list2.append(list_table[i2][0])
            label = max(list2)
            f2.write(str(label) + '\n')

    f1.close()
    f2.close()

    # print some information about new labels
    f3 = open("D:\Academic\data_nvspl\SRCID_LAKE017_re_labels.txt", 'r')
    new_labels = [int(l.split()[0]) for l in f3]
    print('Labels counter after re-label: ')
    print(collections.Counter(new_labels))
    f3.close()


def relabel_pure(window_size, confuse_tolerance):
    f1 = open("D:\Academic\data_nvspl\SRCID_LAKE017_replaced_labels.txt", 'r')
    f2 = open("D:\Academic\data_nvspl\SRCID_LAKE017_re_labels_pure.txt", 'w')
    # window_size = 30
    # confuse_tolerance = 3

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


if __name__ == '__main__':
    window_size = 20
    relabel(window_size)
