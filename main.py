from referencevalues import LTEBandDecode

lteband = int(input('LTE band: '))
earfcn_low, earfcn_high, type = LTEBandDecode.earfcnlimits(lteband)
bandwidth = LTEBandDecode.availableBW(lteband)
print(int(earfcn_low))
print(int(earfcn_high))
print(type)
print(bandwidth)
