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
Usage: This code deletes class "4", i.e. "Aircraft" from the combined data
        label file.
Parameters:
    f1: the input combined data and label file
    f2: the output label file
    Delete example:
    Delete "4":
    i1 = 0
    for line in f1:
        if labels[i1] != 4:
            f2.write(line)
        i1 = i1 + 1
'''
import collections


def delete_label(pure):
    labels = [int(l.split()[0]) for l in open("D:\Academic\data_nvspl\\SRCID_LAKE017_combine_data_label.txt")]
    f1 = open("D:\Academic\data_nvspl\\SRCID_LAKE017_combine_data_label.txt", 'r')
    f2 = open("D:\Academic\data_nvspl\\SRCID_LAKE017_delete.txt", 'w')

    if pure == 0:
        i1 = 0
        for line in f1:
            if labels[i1] != 4:
                f2.write(line)
            i1 = i1 + 1
    if pure == 1:
        i1 = 0
        for line in f1:
            if labels[i1] != 999:
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


if __name__ == '__main__':
    delete_label(pure=0)
