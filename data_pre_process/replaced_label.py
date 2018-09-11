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
Usage:  Replace uninterested labels together, i.e.,
        merge 0, 2, 8 and 20 into 20. Alternatively, 1 can
        be replaced as well.
Replace rule:
        0, 2, 20, 8 => 3
        1 => 4
        1.1 => 0
        1.2 => 1
        1.3 => 2
Parameters:
        f1: the replaced output file
Replace method example:
        Replace 0 with 20
        list = [20 if x == 0 else x for x in list]
'''
import collections


def replaced_labels():
    f1 = open("D:\Academic\data_nvspl\SRCID_LAKE017_replaced_labels.txt", 'w')

    # Print some information of data first
    list = [float(l.split()[0]) for l in open("D:\Academic\data_nvspl\SRCID_LAKE017_labels.txt")]
    print('Labels counter before replacement:')
    print(collections.Counter(list))

    # Replace 0 with 4
    list = [3 if x == 0 else x for x in list]
    # Replace 2 with 4
    list = [3 if x == 2 else x for x in list]
    # Replace 20 with 4
    list = [3 if x == 20 else x for x in list]
    # Replace 8 with 4
    list = [3 if x == 8 else x for x in list]
    # Replace 1 with 0
    list = [4 if x == 1 else x for x in list]
    # Replace 1.1 with 1
    list = [0 if x == 1.1 else x for x in list]
    # Replace 1.2 with 2
    list = [1 if x == 1.2 else x for x in list]
    # Replace 1.3 with 3
    list = [2 if x == 1.3 else x for x in list]
    # Replace 19.0 with 4
    list = [4 if x == 19.0 else x for x in list]
    # Print the replacement result
    print('Labels counter after replacement:')
    print(collections.Counter(list))

    for i in list:
        f1.write(str(i) + '\n')

    f1.close()


if __name__ == '__main__':
    replaced_labels()
