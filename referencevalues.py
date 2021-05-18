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

cqi = {
    0: {
        'modulation': 'QPKS',
        'tbsindex': 0,
    },
    1: {
        'modulation': 'QPKS',
        'tbsindex': 1,
    },
    2: {
        'modulation': 'QPKS',
        'tbsindex': 2,
    },
    3: {
        'modulation': 'QPKS',
        'tbsindex': 3,
    },
    4: {
        'modulation': 'QPKS',
        'tbsindex': 4,
    },
    5: {
        'modulation': 'QPKS',
        'tbsindex': 5,
    },
    6: {
        'modulation': 'QPKS',
        'tbsindex': 6,
    },
    7: {
        'modulation': 'QPKS',
        'tbsindex': 7,
    },
    8: {
        'modulation': 'QPKS',
        'tbsindex': 8,
    },
    9: {
        'modulation': 'QPKS',
        'tbsindex': 9,
    },
    10:{
        'modulation': '16QAM',
        'tbsindex': 9,
    },
    11: {
        'modulation': '16QAM',
        'tbsindex': 11,
    },
    12: {
        'modulation': '16QAM',
        'tbsindex': 12,
    },
}

print(cqi[0]['tbsindex'])
bitrateperrb = (modulation['64QAM']*resourceblock['symbols']*resourceblock['subcarrier'])/1000
throughput = bandwidth[20]['resource_block']*bitrateperrb
print(throughput)