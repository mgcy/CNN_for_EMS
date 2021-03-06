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
Usage: Expand the original label file seconds by seconds into a format
        which can be used for training easily.
Parameters:
    f2: the target output file
    date_days: how many days wanted to be included
'''
import collections


def expand_sec(date_days):
    date_time = [str(l.split()[0]) for l in open("D:\Academic\data_nvspl\SRCID_LAKE017.txt")]

    # Aim label file is f2, while f1 is a temporary file used for hourly data

    f2 = open("D:\Academic\data_nvspl\SRCID_LAKE017_labels.txt", 'w')

    # Make the date from the first three days
    # date_days = 3

    # Get the number of days
    date_index = []
    [date_index.append(i) for i in date_time if not i in date_index]
    len_date = len(date_index)
    print('The max number of days: ' + str(len_date))

    for i1 in range(date_days):
        # Choose a day
        day_index = date_index[i1]
        hr_index = []
        hr = []
        # Get the hour information first
        for l in open("D:\Academic\data_nvspl\SRCID_LAKE017.txt"):
            if l.split()[0] == day_index:
                hr_index.append(l.split()[1])
                [hr.append(i) for i in hr_index if not i in hr]

        # Write the hourly data in the temporary file f1
        for i3 in range(24):
            f1 = open("D:\Academic\data_nvspl\SRCID_LAKE017_expand_labels.txt", 'w')

            for l in open("D:\Academic\data_nvspl\SRCID_LAKE017.txt"):

                if l.split()[0] == day_index:
                    if str(i3) in hr:
                        if l.split()[1] == str(i3):
                            f1.write(l)
            f1.close()
            lines = open("D:\Academic\data_nvspl\SRCID_LAKE017_expand_labels.txt", 'r').readlines()
            f3 = open("D:\Academic\data_nvspl\SRCID_LAKE017_expand_labels_sort.txt", 'w')
            for line in sorted(lines, key=lambda line: int(line.split()[2])):
                f3.write(line)
            f3.close()

            # Read f1 and write labels in f2. It is possible that during some hours no event occurs.
            if str(i3) in hr:

                start_time = [str(l.split()[2]) for l in
                              open("D:\Academic\data_nvspl\SRCID_LAKE017_expand_labels_sort.txt")]
                len_time = [str(l.split()[3]) for l in
                            open("D:\Academic\data_nvspl\SRCID_LAKE017_expand_labels_sort.txt")]
                labels = [str(l.split()[4]) for l in
                          open("D:\Academic\data_nvspl\SRCID_LAKE017_expand_labels_sort.txt")]
                len_labels = len(labels)
                for i in range(1, 3601):
                    for m in range(0, len_labels):
                        '''
                        # Prior labels > post labels
                        if i < int(start_time[m]):
                            f2.write('0\n')
                            break
                        if i >= int(start_time[m]) and i < (int(start_time[m]) + int(len_time[m])):
                            f2.write(labels[m] + '\n')
                            break
                        if i >= (int(start_time[len_labels - 1]) + int(len_time[len_labels - 1])):
                            f2.write('0\n')
                            break
                        '''
                        # Prior labels < post labels
                        if m < (len_labels - 2):
                            if int(start_time[m + 1]) < (int(start_time[m]) + int(len_time[m])):
                                # overlap exist in this m
                                if i >= int(start_time[m + 1]) and i < (int(start_time[m]) + int(len_time[m]) - 1):
                                    f2.write(labels[m + 1] + '\n')
                                    break
                                if i < int(start_time[m + 1]) and i >= int(start_time[m]):
                                    f2.write(labels[m] + '\n')
                                    break
                            else:
                            # no overlab in this m
                                if i < int(start_time[m]):
                                    f2.write('0\n')
                                    break
                                if i >= int(start_time[m]) and i < (int(start_time[m]) + int(len_time[m])):
                                    f2.write(labels[m] + '\n')
                                    break
                                if i >= (int(start_time[len_labels - 1]) + int(len_time[len_labels - 1])):
                                    f2.write('0\n')
                                    break

                        else:
                            if i < int(start_time[m]):
                                f2.write('0\n')
                                break
                            if i >= int(start_time[m]) and i < (int(start_time[m]) + int(len_time[m])):
                                f2.write(labels[m] + '\n')
                                break
                            if i >= (int(start_time[len_labels - 1]) + int(len_time[len_labels - 1])):
                                f2.write('0\n')
                                break

            else:
                for i4 in range(3600):
                    f2.write('0\n')
    f2.close()

    # print some information of label file

    list = [float(l.split()[0]) for l in open("D:\Academic\data_nvspl\SRCID_LAKE017_labels.txt")]
    print('Counter information after expanding by seconds: ')
    print(collections.Counter(list))


if __name__ == '__main__':
    date_days = 1
    expand_sec(date_days)
