# Question 4: Show a sliding window plot of your 
# Tajima's D scans for all 3 populations (x-axis 
# should be position, and y-axis should be Tajima's D). [1 pt]

import pandas as pd
import matplotlib.pyplot as plt

popC = pd.read_csv('popC_TajimaD.txt', sep='\t')
popC_chrom_pos = popC['BIN_START']
popC_tajima = popC['TajimaD']

popL = pd.read_csv('popL_TajimaD.txt', sep='\t')
popL_chrom_pos = popL['BIN_START']
popL_tajima = popL['TajimaD']

popT = pd.read_csv('popT_TajimaD.txt', sep='\t')
popT_chrom_pos = popT['BIN_START']
popT_tajima = popT['TajimaD']

window_size = 5

plt.plot(popC_chrom_pos, popC_tajima, label="popC", color='red')
plt.plot(popL_chrom_pos, popL_tajima, label="popL", color='blue')
plt.plot(popT_chrom_pos, popT_tajima, label="popT", color='orange')

plt.xlabel('Chromosome Position')
plt.ylabel("Tajima's D")
plt.title("Guppy Population: Tajima's D")
plt.legend()
plt.grid(True)
plt.show()
