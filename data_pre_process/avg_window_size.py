import statistics
import collections
import matplotlib.pyplot as plt

duration_time = [int(l.split()[3]) for l in open("D:\Academic\data_nvspl\SRCID_LAKE017.txt")]
labels = [float(l.split()[4]) for l in open("D:\Academic\data_nvspl\SRCID_LAKE017.txt")]

jet_duration = []
prop_duration = []
heli_duration = []
unknown = []

print('Counter of labels:')
print(collections.Counter(labels))

for i in range(len(labels)):
    if labels[i] == 1.1:
        jet_duration.append(duration_time[i])
    if labels[i] == 1.2:
        prop_duration.append(duration_time[i])
    if labels[i] == 1.3:
        heli_duration.append(duration_time[i])
    if labels[i] != 1 and labels[i] != 1.1 and labels[i] != 1.2 and labels[i] != 1.3:
        unknown.append(duration_time[i])

sorted_duration = sorted(duration_time)
avg_duration = statistics.mean(duration_time)
print('Average Duration:')
print(avg_duration)
print('Counter Information:')
print(collections.Counter(duration_time))
print('Max:')
print(max(duration_time))
print('Min:')
print(min(duration_time))

plt.figure(0)
plt.hist(duration_time, 100, alpha=0.5, ec='black')
plt.title('Duration Histogram')
plt.xlabel('Duration')
plt.ylabel('Frequency')
plt.axvline(avg_duration, color='r', linestyle='dashed', linewidth=2)
plt.axvline(30, color='r', linestyle='dashed', linewidth=2)

plt.figure(1)
plt.hist(jet_duration, 100, alpha=0.5, ec='black')
plt.title('Jet Duration Histogram')
plt.xlabel('Duration')
plt.ylabel('Frequency')
plt.axvline(statistics.mean(jet_duration), color='r', linestyle='dashed', linewidth=2)

plt.figure(2)
plt.hist(prop_duration, 100, alpha=0.5, ec='black')
plt.title('Prop Duration Histogram')
plt.xlabel('Duration')
plt.ylabel('Frequency')
plt.axvline(statistics.mean(prop_duration), color='r', linestyle='dashed', linewidth=2)

plt.figure(3)
plt.hist(heli_duration, 100, alpha=0.5, ec='black')
plt.title('Heli Duration Histogram')
plt.xlabel('Duration')
plt.ylabel('Frequency')
plt.axvline(statistics.mean(heli_duration), color='r', linestyle='dashed', linewidth=2)

plt.figure(4)
plt.hist(unknown, 100, alpha=0.5, ec='black')
plt.title('Unknown Duration Histogram')
plt.xlabel('Duration')
plt.ylabel('Frequency')
plt.axvline(statistics.mean(unknown), color='r', linestyle='dashed', linewidth=2)