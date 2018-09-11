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
Usage: This code shuffles the lines in combined data and label file.
Parameters:
    lines: desired data and label file after deleting .
    Output file: SRCID_LAKE017_shuffle.txt
'''
import random


def shuffle_data_labels():
    # lines = open("D:\Academic\data_nvspl\\test_2.txt").readlines()
    lines = open("D:\Academic\data_nvspl\\SRCID_LAKE017_delete.txt").readlines()

    random.shuffle(lines)
    open("D:\Academic\data_nvspl\\SRCID_LAKE017_shuffle.txt", 'w').writelines(lines)


if __name__ == '__main__':
    shuffle_data_labels()
