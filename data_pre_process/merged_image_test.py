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
Usage: This code will merge the original data into an array, which can be easily used
        for the tensorflow
Parameters:
    f1: the merged file
    window_size: the size of window
    date_days: the number of days which are used for training
'''

import numpy as np

# target file
f1 = open("D:\Academic\data_nvspl\SRCID_LAKE017_data_test.txt", 'w')
window_size = 80
# Make the date from the first three days
date_days = 1

# Get all the dates in label file, which is not very useful
date_time = [str(l.split()[0]) for l in open("D:\Academic\data_nvspl\SRCID_LAKE017.txt")]

# Get the indices of days
date_index = []
[date_index.append(i) for i in date_time if not i in date_index]
len_date = len(date_index)

for i1 in range(date_days):
    # Choose a day
    day_index = date_index[i1]
    day_index = day_index.replace('-', '_')
    for i2 in range(24):
        if i2 < 10:
            data_dir = 'D:\Academic\data_nvspl\LAKE017\\NVSPL_LAKE017_' + day_index + '_0' + str(i2) + '.txt'
        else:
            data_dir = 'D:\Academic\data_nvspl\LAKE017\\NVSPL_LAKE017_' + day_index + '_' + str(i2) + '.txt'
        print(data_dir)
        label1 = [str(l.split(',')[2]) for l in open(data_dir, 'r')]
        label2 = [str(l.split(',')[3]) for l in open(data_dir, 'r')]
        label3 = [str(l.split(',')[4]) for l in open(data_dir, 'r')]
        label4 = [str(l.split(',')[5]) for l in open(data_dir, 'r')]
        label5 = [str(l.split(',')[6]) for l in open(data_dir, 'r')]
        label6 = [str(l.split(',')[7]) for l in open(data_dir, 'r')]
        label7 = [str(l.split(',')[8]) for l in open(data_dir, 'r')]
        label8 = [str(l.split(',')[9]) for l in open(data_dir, 'r')]
        label9 = [str(l.split(',')[10]) for l in open(data_dir, 'r')]
        label10 = [str(l.split(',')[11]) for l in open(data_dir, 'r')]
        label11 = [str(l.split(',')[12]) for l in open(data_dir, 'r')]
        label12 = [str(l.split(',')[13]) for l in open(data_dir, 'r')]
        label13 = [str(l.split(',')[14]) for l in open(data_dir, 'r')]
        label14 = [str(l.split(',')[15]) for l in open(data_dir, 'r')]
        label15 = [str(l.split(',')[16]) for l in open(data_dir, 'r')]
        label16 = [str(l.split(',')[17]) for l in open(data_dir, 'r')]
        label17 = [str(l.split(',')[18]) for l in open(data_dir, 'r')]
        label18 = [str(l.split(',')[19]) for l in open(data_dir, 'r')]
        label19 = [str(l.split(',')[20]) for l in open(data_dir, 'r')]
        label20 = [str(l.split(',')[21]) for l in open(data_dir, 'r')]
        label21 = [str(l.split(',')[22]) for l in open(data_dir, 'r')]
        label22 = [str(l.split(',')[23]) for l in open(data_dir, 'r')]
        label23 = [str(l.split(',')[24]) for l in open(data_dir, 'r')]
        label24 = [str(l.split(',')[25]) for l in open(data_dir, 'r')]
        label25 = [str(l.split(',')[26]) for l in open(data_dir, 'r')]
        label26 = [str(l.split(',')[27]) for l in open(data_dir, 'r')]
        label27 = [str(l.split(',')[28]) for l in open(data_dir, 'r')]
        label28 = [str(l.split(',')[29]) for l in open(data_dir, 'r')]
        label29 = [str(l.split(',')[30]) for l in open(data_dir, 'r')]
        label30 = [str(l.split(',')[31]) for l in open(data_dir, 'r')]
        label31 = [str(l.split(',')[32]) for l in open(data_dir, 'r')]
        label32 = [str(l.split(',')[33]) for l in open(data_dir, 'r')]
        label33 = [str(l.split(',')[34]) for l in open(data_dir, 'r')]
        # write by lines
        for i3 in range((int(3600 / window_size) - 1) * 2 + 1):
            # write data in each line
            for i4 in range(window_size / 2):
                f1.write("%s " % label1[window_size * i3 + i4 + 1])
                f1.write("%s " % label2[window_size * i3 + i4 + 1])
                f1.write("%s " % label3[window_size * i3 + i4 + 1])
                f1.write("%s " % label4[window_size * i3 + i4 + 1])
                f1.write("%s " % label5[window_size * i3 + i4 + 1])
                f1.write("%s " % label6[window_size * i3 + i4 + 1])
                f1.write("%s " % label7[window_size * i3 + i4 + 1])
                f1.write("%s " % label8[window_size * i3 + i4 + 1])
                f1.write("%s " % label9[window_size * i3 + i4 + 1])
                f1.write("%s " % label10[window_size * i3 + i4 + 1])
                f1.write("%s " % label11[window_size * i3 + i4 + 1])
                f1.write("%s " % label12[window_size * i3 + i4 + 1])
                f1.write("%s " % label13[window_size * i3 + i4 + 1])
                f1.write("%s " % label14[window_size * i3 + i4 + 1])
                f1.write("%s " % label15[window_size * i3 + i4 + 1])
                f1.write("%s " % label16[window_size * i3 + i4 + 1])
                f1.write("%s " % label17[window_size * i3 + i4 + 1])
                f1.write("%s " % label18[window_size * i3 + i4 + 1])
                f1.write("%s " % label19[window_size * i3 + i4 + 1])
                f1.write("%s " % label20[window_size * i3 + i4 + 1])
                f1.write("%s " % label21[window_size * i3 + i4 + 1])
                f1.write("%s " % label22[window_size * i3 + i4 + 1])
                f1.write("%s " % label23[window_size * i3 + i4 + 1])
                f1.write("%s " % label24[window_size * i3 + i4 + 1])
                f1.write("%s " % label25[window_size * i3 + i4 + 1])
                f1.write("%s " % label26[window_size * i3 + i4 + 1])
                f1.write("%s " % label27[window_size * i3 + i4 + 1])
                f1.write("%s " % label28[window_size * i3 + i4 + 1])
                f1.write("%s " % label29[window_size * i3 + i4 + 1])
                f1.write("%s " % label30[window_size * i3 + i4 + 1])
                f1.write("%s " % label31[window_size * i3 + i4 + 1])
                f1.write("%s " % label32[window_size * i3 + i4 + 1])
                f1.write("%s " % label33[window_size * i3 + i4 + 1])
            for i5 in range(window_size / 2, window_size):
                f1.write("%s " % label1[window_size * i3 + i4 + 1])
                f1.write("%s " % label2[window_size * i3 + i4 + 1])
                f1.write("%s " % label3[window_size * i3 + i4 + 1])
                f1.write("%s " % label4[window_size * i3 + i4 + 1])
                f1.write("%s " % label5[window_size * i3 + i4 + 1])
                f1.write("%s " % label6[window_size * i3 + i4 + 1])
                f1.write("%s " % label7[window_size * i3 + i4 + 1])
                f1.write("%s " % label8[window_size * i3 + i4 + 1])
                f1.write("%s " % label9[window_size * i3 + i4 + 1])
                f1.write("%s " % label10[window_size * i3 + i4 + 1])
                f1.write("%s " % label11[window_size * i3 + i4 + 1])
                f1.write("%s " % label12[window_size * i3 + i4 + 1])
                f1.write("%s " % label13[window_size * i3 + i4 + 1])
                f1.write("%s " % label14[window_size * i3 + i4 + 1])
                f1.write("%s " % label15[window_size * i3 + i4 + 1])
                f1.write("%s " % label16[window_size * i3 + i4 + 1])
                f1.write("%s " % label17[window_size * i3 + i4 + 1])
                f1.write("%s " % label18[window_size * i3 + i4 + 1])
                f1.write("%s " % label19[window_size * i3 + i4 + 1])
                f1.write("%s " % label20[window_size * i3 + i4 + 1])
                f1.write("%s " % label21[window_size * i3 + i4 + 1])
                f1.write("%s " % label22[window_size * i3 + i4 + 1])
                f1.write("%s " % label23[window_size * i3 + i4 + 1])
                f1.write("%s " % label24[window_size * i3 + i4 + 1])
                f1.write("%s " % label25[window_size * i3 + i4 + 1])
                f1.write("%s " % label26[window_size * i3 + i4 + 1])
                f1.write("%s " % label27[window_size * i3 + i4 + 1])
                f1.write("%s " % label28[window_size * i3 + i4 + 1])
                f1.write("%s " % label29[window_size * i3 + i4 + 1])
                f1.write("%s " % label30[window_size * i3 + i4 + 1])
                f1.write("%s " % label31[window_size * i3 + i4 + 1])
                f1.write("%s " % label32[window_size * i3 + i4 + 1])
                f1.write("%s " % label33[window_size * i3 + i4 + 1])

            f1.write('\n')
        open(data_dir, 'r').close()

f1.close()

# check the results
image_data = np.loadtxt('D:\Academic\data_nvspl\SRCID_LAKE017_data.txt')
print('The shape of the merged data as an array:')
print(image_data.shape)
