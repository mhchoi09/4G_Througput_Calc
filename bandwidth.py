table_bw = {
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

table_framestructure = {
    'resourceblock': {
        'subcarrier': 12,
        'bandwidth': 180
    },
    'schedulingblock': {
        'resourceblock': 2,
        'symbols': 14,
    },
    'slot': {
        'symbols': 7,
    },
    'subframe': {
        'slots': 2,
        'symbols': 14,
        'time': 1,
    },
    'radioframe': {
        'symbols': 140,
        'slots': 20,
        'subframe': 10,
        'time': 10,
    },
}

table_modulation = {
    'QPSK': 2,
    '16QAM': 4,
    '64QAM': 6,
    '256QAM': 8,
    '1024QAM': 16,
}

print(table_modulation['256QAM'])