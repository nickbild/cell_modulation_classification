import _pickle as cPickle
import numpy as np


# Open the dataset.
Xd = cPickle.load(open("RML2016.10a_dict.pkl",'rb'), encoding='latin1')

# 220 - 11 modulations, 20 SNRs each.
# print(len(Xd))

# 1000 samples for each modulation / SNR.
# print(len(Xd[('AM-DSB', -8)]))

# Each of the 1000 samples has 2 arrays.
# print(Xd[('AM-DSB', -8)][0])

# Each array is length of 128.
# print(len(Xd[('AM-DSB', -8)][0][0]))

# Modulation types.
mods = ['8PSK', 'AM-DSB', 'AM-SSB', 'BPSK', 'CPFSK', 'GFSK', 'PAM4', 'QAM16', 'QAM64', 'QPSK', 'WBFM']
# Signal-to-noise ratio levels.
snrs = range(-20, 20, 2)
# Number of samples to process for each mod/SNR pair (max 1000).
num_samples = 10

# Process a subset of the data into separate CSVs, identified by modulation type.
for mod in mods:
    for snr in snrs:
        for sample in range(num_samples):
            f = open("processed/{0}.{1}-{2}.csv".format(mod, snr, sample), "w")
            f.write("v1,v2\n")
            
            v1 = Xd[(mod, snr)][sample][0]
            v2 = Xd[(mod, snr)][sample][1]
            
            for measurement in range(128):
                f.write("{0},{1}\n".format(v1[measurement], v2[measurement]))
            
            f.close()

# Example processing.
# snrs,mods = map(lambda j: sorted(list(set(map(lambda x: x[j], Xd.keys())))), [1,0])
# X = []  
# lbl = []
# for mod in mods:
#     print(mod)
#     for snr in snrs:
#         # print("{0}".format(snr))
#         X.append(Xd[(mod,snr)])
#         for i in range(Xd[(mod,snr)].shape[0]):  lbl.append((mod,snr))


# X = np.vstack(X)
