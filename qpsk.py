import numpy as np
import math as mp
import matplotlib.pyplot as plt

def qfunc(x):
	return 0.5*mp.erfc(x/np.sqrt(2))

#Number of SNR samples 
snrlen = 15
#SNR values in dB
snrdb = np.linspace(0,14,15)
#Number of samples
simlen = int(1e6)
#Simulated BER declaration		
err = []
#Analytical BER declaration
ber = []
temp=0
noise1 = np.random.normal(0,1,simlen)
noise2 = np.random.normal(0,1,simlen)

#vary SNR 0 to 15 dB
for i in range(0,snrlen):
	snr = 10**(0.1*snrdb[i])
	rx = np.sqrt(2*snr) + noise1
	ry = noise2
	crct = 0
	for j in range (0,len(rx)):
	    if ((rx[j]>ry[j]) and (rx[j]>-ry[j])):
	    	crct=crct+1                
	#calculating the total number of errors
	#calcuating the simulated BER
	err.append(1-(crct/float(simlen)))
	#calculating the analytical BER
	ber.append(1-(1-qfunc(np.sqrt(snr)))**2)
plt.semilogy(snrdb.T,ber,label='Analysis')
plt.semilogy(snrdb.T,err,'o',label='Simulation')
plt.xlabel('SNR$\\left(\\frac{E_b}{N_0}\\right)$')
plt.ylabel('probability of error')
plt.legend()
plt.grid()
plt.show()
