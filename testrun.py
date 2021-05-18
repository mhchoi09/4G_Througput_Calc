from referencevalues import LTEParameters
from referencevalues import EARFCNCalculator

lteband = int(input('LTE band: '))
bandwidth = LTEParameters.availablebw(lteband)
print(bandwidth)
bw = float(input('Select BW: '))
isbandwidthvalid = LTEParameters.verifybw(lteband, bw)

earfcn = int(input('EARFCN: '))
lteband = EARFCNCalculator.band_ndl(earfcn)
bandwidth = LTEParameters.availablebw(lteband)
fdl, earfcn = EARFCNCalculator.dlfrequency(earfcn, lteband)
print(lteband, fdl, earfcn)
print('Possible BW: ', bandwidth)
