import bisect

table_lte_bands = {
    1: {"type": "FDD", "frequency": "2100", "range": ["1920-1980", "2110-2170"], "bandwidths": [5, 10, 15, 20],
        "earfcn": [0, 599], "rel": 8, 'FDL_Low': 2110, 'NDL_Offset': 0, 'DL_range': (0, 599), 'FUL_Low': 1920,
        'NUL_Offset': 18000, 'UP_range': (1800, 18599), },
    2: {"type": "FDD", "frequency": "1900", "range": ["1850-1910", "1930-1990"], "bandwidths": [1.4, 3, 5, 10, 15, 20],
        "earfcn": [600, 1199], "rel": 8, 'FDL_Low': 1930, 'NDL_Offset': 600, 'DL_range': (600, 1199), 'FUL_Low': 1850,
        'NUL_Offset': 18600, 'UP_range': (18600, 19199), },
    3: {"type": "FDD", "frequency": "1800", "range": ["1710-1785", "1805-1880"], "bandwidths": [1.4, 3, 5, 10, 15, 20],
        "earfcn": [1200, 1949], "rel": 8, 'FDL_Low': 1805, 'NDL_Offset': 1200, 'DL_range': (1200, 1949),
        'FUL_Low': 1710,
        'NUL_Offset': 19200, 'UP_range': (19200, 19949), },
    4: {"type": "FDD", "frequency": "1700", "range": ["1710-1755", "2110-2155"], "bandwidths": [1.4, 3, 5, 10, 15, 20],
        "earfcn": [1950, 2399], "rel": 8, 'FDL_Low': 2110, 'NDL_Offset': 1950, 'DL_range': (1950, 2399),
        'FUL_Low': 1710,
        'NUL_Offset': 19950, 'UP_range': (19950, 20399), },
    5: {"type": "FDD", "frequency": "850", "range": ["824-849", "869-894"], "bandwidths": [1.4, 3, 5, 10],
        "earfcn": [2400, 2649], "rel": 8, 'FDL_Low': 869, 'NDL_Offset': 2400, 'DL_range': (2400, 2649), 'FUL_Low': 824,
        'NUL_Offset': 20400, 'UP_range': (20400, 20649), },
    6: {"type": "FDD", "frequency": "850", "range": ["830-840", "875-885"], "bandwidths": [5, 10], "rel": 8, 'FDL_Low': 875,
        'NDL_Offset': 2650, 'DL_range': (2650, 2749), 'FUL_Low': 830, 'NUL_Offset': 20650, 'UP_range': (20650, 20749), },
    7: {"type": "FDD", "frequency": "2600", "range": ["2500-2570", "2620-2690"], "bandwidths": [5, 10, 15, 20],
        "earfcn": [2750, 3449], "rel": 8, 'FDL_Low': 2620, 'NDL_Offset': 2750, 'DL_range': (2750, 3449), 'FUL_Low': 2500,
        'NUL_Offset': 20750, 'UP_range': (20750, 21449), },
    8: {"type": "FDD", "frequency": "900", "range": ["880-915", "925-960"], "bandwidths": [1.4, 3, 5, 10],
        "earfcn": [3450, 3799], "rel": 8},
    9: {"type": "FDD", "frequency": "1800", "range": ["1749.9-1784.9", "1844.9-1879.9"], "bandwidths": [5, 10, 15, 20],
        "earfcn": [3800, 4149], "rel": 8},
    10: {"type": "FDD", "frequency": "1700", "range": ["1710-1770", "2110-2170"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [4150, 4749], "rel": 8},
    11: {"type": "FDD", "frequency": "1500", "range": ["1427.9-1447.9", "1475.9-1495.9"], "bandwidths": [5, 10],
         "earfcn": [4750, 4949], "rel": 8},
    12: {"type": "FDD", "frequency": "700", "range": ["699-716", "729-746"], "bandwidths": [1.4, 3, 5, 10],
         "earfcn": [5010, 5179], "rel": 8.4},
    13: {"type": "FDD", "frequency": "700", "range": ["777-787", "746-756"], "bandwidths": [5, 10],
         "earfcn": [5180, 5279], "rel": 8},
    14: {"type": "FDD", "frequency": "700", "range": ["788-798", "758-768"], "bandwidths": [5, 10],
         "earfcn": [5280, 5370], "rel": 8},
    17: {"type": "FDD", "frequency": "700", "range": ["704-716", "734-746"], "bandwidths": [5, 10],
         "earfcn": [5730, 5849], "rel": 8.3},
    18: {"type": "FDD", "frequency": "850", "range": ["815-830", "860-875"], "bandwidths": [5, 10, 15],
         "earfcn": [5850, 5999], "rel": 9},
    19: {"type": "FDD", "frequency": "850", "range": ["830-845", "875-890"], "bandwidths": [5, 10, 15],
         "earfcn": [6000, 6149], "rel": 9},
    20: {"type": "FDD", "frequency": "800", "range": ["832-862", "791-821"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [6150, 6449], "rel": 9},
    21: {"type": "FDD", "frequency": "1500", "range": ["1447.9-1462.9", "1495.9-1510.9"], "bandwidths": [5, 10, 15],
         "earfcn": [6450, 6559], "rel": 9},
    22: {"type": "FDD", "frequency": "3500", "range": ["3410-3490", "3510-3590"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [6600, 7399], "rel": 10.4},
    23: {"type": "FDD", "frequency": "2000", "range": ["2000-2020", "2180-2200"], "bandwidths": [1.4, 3, 5, 10, 15, 20],
         "earfcn": [7500, 7699], "rel": 10.3},
    24: {"type": "FDD", "frequency": "1600", "range": ["1626.5-1660.5", "1525-1559"], "bandwidths": [5, 10],
         "earfcn": [7700, 8039], "rel": 10.1},
    25: {"type": "FDD", "frequency": "1900", "range": ["1850-1915", "1930-1995"], "bandwidths": [1.4, 3, 5, 10, 15, 20],
         "earfcn": [8040, 8689], "rel": 10.0},
    26: {"type": "FDD", "frequency": "850", "range": ["814-849", "859-894"], "bandwidths": [1.4, 3, 5, 10, 15, 20],
         "earfcn": [8690, 9039], "rel": 11.0},
    27: {"type": "FDD", "frequency": "800", "range": ["807-824", "852-869"], "bandwidths": [1.4, 3, 5, 10],
         "earfcn": [9040, 9209], "rel": 11.1},
    28: {"type": "FDD", "frequency": "700", "range": ["703-748", "758-803"], "bandwidths": [3, 5, 10, 15, 20],
         "earfcn": [9210, 9659], "rel": 11.1},
    29: {"type": "SDL", "frequency": "700", "range": ["717-728"], "bandwidths": [3, 5, 10], "earfcn": [9660, 9790],
         "rel": 11.3},
    30: {"type": "FDD", "frequency": "2300", "range": ["2305-2315", "2350-2360"], "bandwidths": [5, 10],
         "earfcn": [9770, 9869], "rel": 12.0},
    31: {"type": "FDD", "frequency": "450", "range": ["452.5-457.5", "462.5-467.5"], "bandwidths": [1.4, 3, 5],
         "earfcn": [9870, 9919], "rel": 12.0},
    32: {"type": "SDL", "frequency": "1500", "range": ["1452-1496"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [9920, 10359], "rel": 12.4},
    33: {"type": "TDD", "frequency": "2100", "range": ["1900-1920"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [36000, 36199], "rel": 8},
    34: {"type": "TDD", "frequency": "2100", "range": ["2010-2025"], "bandwidths": [5, 10, 15],
         "earfcn": [36200, 36349], "rel": 8},
    35: {"type": "TDD", "frequency": "1900", "range": ["1850-1910"], "bandwidths": [1.4, 3, 5, 10, 15, 20],
         "earfcn": [36350, 36949], "rel": 8},
    36: {"type": "TDD", "frequency": "1900", "range": ["1930-1990"], "bandwidths": [1.4, 3, 5, 10, 15, 20],
         "earfcn": [36950, 37549], "rel": 8},
    37: {"type": "TDD", "frequency": "1900", "range": ["1910-1930"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [37550, 37749], "rel": 8},
    38: {"type": "TDD", "frequency": "2600", "range": ["2570-2620"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [37750, 38249], "rel": 8},
    39: {"type": "TDD", "frequency": "1900", "range": ["1880-1920"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [38250, 38649], "rel": 8},
    40: {"type": "TDD", "frequency": "2300", "range": ["2300-2400"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [38650, 39649], "rel": 8},
    41: {"type": "TDD", "frequency": "2500", "range": ["2496-2690"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [39650, 41589], "rel": 10.0},
    42: {"type": "TDD", "frequency": "3400", "range": ["3400-3600", "2110-2170"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [41590, 43589], "rel": 10.0},
    43: {"type": "TDD", "frequency": "3700", "range": ["3600-3800"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [43590, 45589], "rel": 10.0},
    44: {"type": "TDD", "frequency": "700", "range": ["703-803"], "bandwidths": [3, 5, 10, 15, 20],
         "earfcn": [45590, 46589], "rel": 11.1},
    45: {"type": "TDD", "frequency": "1500", "range": ["1447-1467"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [46590, 46789], "rel": 13.2},
    46: {"type": "LAA", "frequency": "5200", "range": ["5150-5925"], "bandwidths": [10, 20], "earfcn": [46790, 54539],
         "rel": 13.2},
    47: {"type": "TDD", "frequency": "5900", "range": ["5855-5925"], "bandwidths": [10, 20], "earfcn": [54540, 55239],
         "rel": 14.1},
    48: {"type": "TDD", "frequency": "3600", "range": ["3550-3700"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [55240, 56739], "rel": 14.2},
    49: {"type": "TDD", "frequency": "3600", "range": ["3550-3700"], "bandwidths": [10, 20], "earfcn": [56740, 58239],
         "rel": 15.1},
    50: {"type": "TDD", "frequency": "1500", "range": ["1432-1517"], "bandwidths": [3, 5, 10, 15, 20],
         "earfcn": [58240, 59089], "rel": 15.0},
    51: {"type": "TDD", "frequency": "1500", "range": ["1427-1432"], "bandwidths": [3, 5], "earfcn": [59090, 59139],
         "rel": 15.0},
    52: {"type": "TDD", "frequency": "3300", "range": ["3300-3400"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [59140, 60139], "rel": 15.2},
    53: {"type": "TDD", "frequency": "2500", "range": ["2483.35-2494.85"], "bandwidths": [1.4, 3, 5, 10],
         "earfcn": [60140, 60254], "rel": 16.0},
    65: {"type": "FDD", "frequency": "2100", "range": ["1920-2010", "2110-2200"], "bandwidths": [1.4, 3, 5, 10, 15, 20],
         "earfcn": [65536, 66425], "rel": 13.2},
    66: {"type": "FDD", "frequency": "1700", "range": ["1710-1780", "2110-2200"], "bandwidths": [1.4, 3, 5, 10, 15, 20],
         "earfcn": [66436, 67335], "rel": 13.2},
    67: {"type": "SDL", "frequency": "700", "range": ["738-758"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [67336, 67535], "rel": 13.2},
    68: {"type": "FDD", "frequency": "700", "range": ["698-728", "753-783"], "bandwidths": [5, 10, 15],
         "earfcn": [67536, 67835], "rel": 13.3},
    69: {"type": "SDL", "frequency": "2600", "range": ["2570-2620"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [67836, 68335], "rel": 14.0},
    70: {"type": "FDD", "frequency": "2000", "range": ["1695-1710", "1995-2020"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [68336, 68535], "rel": 14.0},
    71: {"type": "FDD", "frequency": "600", "range": ["663-698", "617-652"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [68586, 68935], "rel": 15.0},
    72: {"type": "FDD", "frequency": "450", "range": ["451-456", "461-466"], "bandwidths": [1.4, 3, 5],
         "earfcn": [68936, 68985], "rel": 15.0},
    73: {"type": "FDD", "frequency": "450", "range": ["450-455", "460-465"], "bandwidths": [1.4, 3, 5],
         "earfcn": [68986, 69035], "rel": 15.0},
    74: {"type": "FDD", "frequency": "1500", "range": ["1427-1470", "1475-1518"], "bandwidths": [1.4, 3, 5, 10, 15, 20],
         "earfcn": [69036, 69465], "rel": 15.0},
    75: {"type": "SDL", "frequency": "1500", "range": ["1432-1517"], "bandwidths": [5, 10, 15, 20],
         "earfcn": [69466, 70315], "rel": 15.0},
    76: {"type": "SDL", "frequency": "1500", "range": ["1427-1432"], "bandwidths": [5], "earfcn": [70316, 70365],
         "rel": 15.0},
    85: {"type": "FDD", "frequency": "700", "range": ["698-716", "728-746"], "bandwidths": [5, 10],
         "earfcn": [70366, 70545], "rel": 15.2},
    87: {"type": "FDD", "frequency": "450", "range": ["410-415", "420-425"], "bandwidths": [1.4, 3, 5],
         "earfcn": [70546, 70595], "rel": 16.2},
    88: {"type": "FDD", "frequency": "450", "range": ["412-417", "422-427"], "bandwidths": [1.4, 3, 5],
         "earfcn": [70596, 70645], "rel": 16.2},
    252: {"type": "SDL", "frequency": "5200", "range": ["5150-5250"], "bandwidths": [20], "earfcn": [255144, 256143],
          "rel": 'null'},
    255: {"type": "SDL", "frequency": "5800", "range": ["5725-5850"], "bandwidths": [20], "earfcn": [260894, 262143],
          "rel": 'null'},
}

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


class LTEParameters:

    def availablebw(lteband):
        bandwidth = table_lte_bands[lteband]['bandwidths']
        return bandwidth

    def verifybw(lteband, bw):
        bandwidth = table_lte_bands[lteband]['bandwidths']
        try:
            bw = bandwidth.index(bw)
        except ValueError:
            return False
        else:
            return True


class EARFCNCalculator:

    def band_ndl(num, breakpoints=None, result=None):
        if result is None:
            result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                      30, 31, 32]
        if breakpoints is None:
            breakpoints = [599, 1199, 1949, 2399, 2649, 2749, 3449, 4149, 4749, 4949, 5179, 5279, 5379, 5849, 5999,
                           6149, 6449, 6559, 7399, 7699, 8039, 8689, 9039, 9209, 9659, 9769, 9869, 9919, 10359, 36199]
        i = bisect.bisect(breakpoints, num - 1)
        return result[i]

    def earfcnlimits(lteband):
        earfcn_low = table_lte_bands[lteband]['earfcn'][0]
        earfcn_high = table_lte_bands[lteband]['earfcn'][1]
        return earfcn_low, earfcn_high

    def dlfrequency(earfcn, lteband):
        fdl = table_lte_bands[lteband]['FDL_Low'] + 0.1 * (earfcn - table_lte_bands[lteband]['NDL_Offset'])
        dlearfcn = earfcn
        return fdl, dlearfcn
