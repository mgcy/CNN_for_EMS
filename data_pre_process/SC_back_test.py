from pandas import read_csv
import numpy as np

window_size = 90
output_data = np.zeros([1, window_size * 90])
input_dir = 'D:\Academic\data_nvspl\SC_Q\SC_Qd\data_training_90_pure_silence_SC.txt'
output_dir = 'D:\Academic\data_nvspl\\SRCID_LAKE017_data_training_SC_zero.txt'

label = [float(l.split()[0]) for l in open('D:\Academic\data_nvspl\SC_Q\\label_training_90_pure_silence.txt')]

dataset = read_csv(input_dir, delimiter=' ', header=None)
dataset = dataset.values
dataset = dataset.astype('float32')

# zero padding
for i2 in range(len(label)):
    if label[i2] == 0:
        dataset[i2 * 90:(i2 + 1) * 90, 30:] = 0
    if label[i2] == 1:
        dataset[i2 * 90:(i2 + 1) * 90, 0:30] = 0
        dataset[i2 * 90:(i2 + 1) * 90, 60:] = 0
    if label[i2] == 2:
        dataset[i2 * 90:(i2 + 1) * 90, 0:60] = 0
    if label[i2] == 3:
        dataset[i2 * 90:(i2 + 1) * 90, :] = 0

for i in range(int(dataset.shape[0] / window_size)):
    # for i in range(3):
    tmp = np.reshape(dataset[i * 90:(i + 1) * 90, :], [1, window_size * 90])
    output_data = np.concatenate((output_data, tmp))

output_data = np.delete(output_data, (0), axis=0)
np.savetxt(output_dir, output_data, fmt='%.5f')
