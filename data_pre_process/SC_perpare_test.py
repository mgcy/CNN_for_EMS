from pandas import read_csv
import numpy as np

window_size = 30


def gen_SC_Q(input_dir, output_dir, window_size):
    a = np.zeros([1, 33])
    # dir = 'D:\Academic\data_nvspl\SC_test.txt'
    dataset = read_csv(input_dir, delimiter=' ', header=None)
    dataset = dataset.values
    dataset = dataset.astype('float32')
    dataset = np.delete(dataset,[dataset.shape[1]-1],axis=1)
    for i in range(dataset.shape[0]):
        tmp = np.reshape(dataset[i], (window_size, 33))
        a = np.concatenate((a, tmp))
    b = np.delete(a, 0, 0)
    # a = np.reshape(dataset, [2, 33])
    np.savetxt(output_dir, b, fmt='%.1f')


input_dir = 'D:\Academic\data_nvspl\SRCID_LAKE017_data_training.txt'
output_dir = 'D:\Academic\data_nvspl\SC_Q\data_training.txt'
gen_SC_Q(input_dir, output_dir, window_size)

input_dir = 'D:\Academic\data_nvspl\SRCID_LAKE017_data_validation.txt'
output_dir = 'D:\Academic\data_nvspl\SC_Q\data_validation.txt'
gen_SC_Q(input_dir, output_dir, window_size)


input_dir = 'D:\Academic\data_nvspl\SRCID_LAKE017_data_testing.txt'
output_dir = 'D:\Academic\data_nvspl\SC_Q\data_testing.txt'
gen_SC_Q(input_dir, output_dir, window_size)
