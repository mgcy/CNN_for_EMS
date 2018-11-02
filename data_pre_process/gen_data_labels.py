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
Usage: This code generates the needed training, validation and testing data
        automatically after determining the window_size.
Notation:
        If this is the first time to use new data, or add some new days into
        data set, import and run expand_sec.py and replaced_label.py.
Parameters:
    window_size;
    Output files:
    f1: training data
    f2: training labels
    f3: validation data
    f4: validation labels
    f5: testing data
    f6: testing labels
'''
import expand_sec
import replaced_label
import relabel
import merged_image
import combine_data_label
import delete_label
import shuffle_data_labels
import select_labels

window_size = 30
date_days = 16
pure = 1
confuse_tolerance = 1

print('Start expand')
expand_sec.expand_sec(date_days)
print('Finish expand')

print('Start replace')
replaced_label.replaced_labels()
print('Finish replace')

print('Start re-label')
if pure == 1:
    relabel.relabel_pure(window_size, confuse_tolerance)
if pure == 0:
    relabel.relabel(window_size)
print('Finish re-label')

print('Start merge images')
merged_image.merged_image(window_size, date_days)
print('Finish merge images')

print('Start combine')
combine_data_label.combine_data_label(pure)
print('Finish combine')

print('Start delete')
delete_label.delete_label(pure)
print('Finish delete')

print('Start shuffle')
shuffle_data_labels.shuffle_data_labels()
print('Finish shuffle')

print('Start select')
select_labels.select_labels()
print('Finish select')
