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
Usage: This code selects data and labels for training, validation and testing after
        shuffling. The samples in those files are same.
Parameters:
    Input file: SRCID_LAKE017_shuffle.txt
    Output files:
    f1: training data
    f2: training labels
    f3: validation data
    f4: validation labels
    f5: testing data
    f6: testing labels
'''
import collections


def select_labels():
    labels = [int(l.split()[0]) for l in open("D:\Academic\data_nvspl\\SRCID_LAKE017_shuffle.txt")]
    f1 = open("D:\Academic\data_nvspl\\SRCID_LAKE017_data_training.txt", 'w')
    f2 = open("D:\Academic\data_nvspl\\SRCID_LAKE017_label_training.txt", 'w')
    f3 = open("D:\Academic\data_nvspl\\SRCID_LAKE017_data_validation.txt", 'w')
    f4 = open("D:\Academic\data_nvspl\\SRCID_LAKE017_label_validation.txt", 'w')
    f5 = open("D:\Academic\data_nvspl\\SRCID_LAKE017_data_testing.txt", 'w')
    f6 = open("D:\Academic\data_nvspl\\SRCID_LAKE017_label_testing.txt", 'w')
    label_table = collections.Counter(labels)

    len_0 = label_table[0]
    len_0_1 = int(len_0 / 3 * 1)
    len_0_2 = int(len_0 / 3 * 2)

    len_1 = label_table[1]
    len_1_1 = int(len_1 / 3 * 1)
    len_1_2 = int(len_1 / 3 * 2)

    len_2 = label_table[2]
    len_2_1 = int(len_2 / 3 * 1)
    len_2_2 = int(len_2 / 3 * 2)

    len_3 = label_table[3]
    len_3_1 = int(len_3 / 3 * 1)
    len_3_2 = int(len_3 / 3 * 2)

    i = 0
    i0 = 0
    i1 = 0
    i2 = 0
    i3 = 0
    for line in open("D:\Academic\data_nvspl\\SRCID_LAKE017_shuffle.txt"):
        if labels[i] == 0:
            if i0 < len_0_1:
                f1.write(line[2:])
                f2.write(str(labels[i]) + '\n')
            elif i0 < len_0_2:
                f3.write(line[2:])
                f4.write(str(labels[i]) + '\n')
            else:
                f5.write(line[2:])
                f6.write(str(labels[i]) + '\n')
            i0 = i0 + 1

        if labels[i] == 1:
            if i1 < len_1_1:
                f1.write(line[2:])
                f2.write(str(labels[i]) + '\n')
            elif i1 < len_1_2:
                f3.write(line[2:])
                f4.write(str(labels[i]) + '\n')
            else:
                f5.write(line[2:])
                f6.write(str(labels[i]) + '\n')
            i1 = i1 + 1

        if labels[i] == 2:
            if i2 < len_2_1:
                f1.write(line[2:])
                f2.write(str(labels[i]) + '\n')
            elif i2 < len_2_2:
                f3.write(line[2:])
                f4.write(str(labels[i]) + '\n')
            else:
                f5.write(line[2:])
                f6.write(str(labels[i]) + '\n')
            i2 = i2 + 1

        if labels[i] == 3:
            if i3 < len_3_1:
                f1.write(line[2:])
                f2.write(str(labels[i]) + '\n')
            elif i3 < len_3_2:
                f3.write(line[2:])
                f4.write(str(labels[i]) + '\n')
            else:
                f5.write(line[2:])
                f6.write(str(labels[i]) + '\n')
            i3 = i3 + 1
        i = i + 1
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()

    # check the select results
    print('The length of the original label file:')
    print(str(len(labels)))
    print('The original label counter information:')
    print(label_table)

    label_training = [int(l.split()[0]) for l in open("D:\Academic\data_nvspl\\SRCID_LAKE017_label_training.txt")]
    print('The length of the selected training label file:')
    print(len(label_training))
    print('The training label counter information:')
    print(collections.Counter(label_training))

    label_validation = [int(l.split()[0]) for l in open("D:\Academic\data_nvspl\\SRCID_LAKE017_label_validation.txt")]
    print('The length of the selected validation label file:')
    print(len(label_validation))
    print('The validation label counter information:')
    print(collections.Counter(label_validation))

    label_testing = [int(l.split()[0]) for l in open("D:\Academic\data_nvspl\\SRCID_LAKE017_label_testing.txt")]
    print('The length of the selected testing label file:')
    print(len(label_testing))
    print('The testing label counter information:')
    print(collections.Counter(label_testing))


if __name__ == '__main__':
    select_labels()
