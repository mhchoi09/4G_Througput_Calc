bandwidth = {
    1.4: {
        'resource_block': 6,
        'subcarriers': 72,
        'uplink': 1.08,
        'downlink': 1.095,
    },
    3: {
        'resource_block': 15,
        'subcarriers': 180,
        'uplink': 2.7,
        'downlink': 2.715,
    },
    5: {
        'resource_block': 25,
        'subcarriers': 300,
        'uplink': 4.5,
        'downlink': 4.515,
    },
    10: {
        'resource_block': 50,
        'subcarriers': 600,
        'uplink': 9.0,
        'downlink': 9.015,
    },
    15: {
        'resource_block': 75,
        'subcarriers': 900,
        'uplink': 13.5,
        'downlink': 13.515,
    },
    20: {
        'resource_block': 100,
        'subcarriers': 1200,
        'uplink': 18,
        'downlink': 18.015,
    },
}

resourceblock = {
    'subcarrier': 12,
    'bandwidth': 180,
    'symbols': 14,
}
radioframe = {
    'subframe': 10,
    'slots': 20,
    'symbols': 140,
    'time': 10,
}

modulation = {
    'QPSK': 2,
    '16QAM': 4,
    '64QAM': 6,
    '256QAM': 8,
    '1024QAM': 16,
}

bitrateperrb = (modulation['64QAM']*resourceblock['symbols']*resourceblock['subcarrier'])/1000
throughput = bandwidth[20]['resource_block']*bitrateperrb*2
print(throughput)