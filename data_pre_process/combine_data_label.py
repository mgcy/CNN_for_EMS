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
Usage: This code combines data file and label file together into a new file.
Parameters:
    labels: the desired list of labels
    f1: the input data file
    f2: the output combined file
'''
import collections


def combine_data_label():
    labels = [int(l.split()[0]) for l in open("D:\Academic\data_nvspl\\SRCID_LAKE017_re_labels.txt")]
    f1 = open("D:\Academic\data_nvspl\\SRCID_LAKE017_data.txt", 'r')
    f2 = open("D:\Academic\data_nvspl\\SRCID_LAKE017_combine_data_label.txt", 'w')
    i0 = 0
    for line in f1:
        f2.write(str(labels[i0]) + ' ')
        f2.write(line)
        i0 = i0 + 1
    f1.close()
    f2.close()

    # check the results
    labels_new = [int(l.split()[0]) for l in open("D:\Academic\data_nvspl\\SRCID_LAKE017_combine_data_label.txt")]
    print('Check whether the dimension of the data is the same after combining.')
    print('Label counter before combining:')
    print(collections.Counter(labels))
    print('Label counter after combining:')
    print(collections.Counter(labels_new))
    print('If the old labels and new labels are same:')
    print(labels == labels_new)


if __name__ == '__main__':
    combine_data_label()
