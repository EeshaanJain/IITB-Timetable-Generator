"""
Mappings for the courses:
a) Time Mappings
b) Color Mappings
"""

"""
At IITB, the times at which lectures take place are different for M/T/Th and W/F, so:
For Monday, Tuesday and Thursday :-
+---------------+--------+---------+----------+
|      Time     | Monday | Tuesday | Thursday |
+---------------+--------+---------+----------+
|  8:30 - 9:25  |   1A   |    4B   |    3C    |
+---------------+--------+---------+----------+
|  9:30 - 10:25 |   2A   |    1B   |    4C    |
+---------------+--------+---------+----------+
| 10:35 - 11:30 |   3A   |    2B   |    1C    |
+---------------+--------+---------+----------+
| 11:35 - 12:30 |   4A   |    3B   |    2C    |
+---------------+--------+---------+----------+
| 14:00 - 15:25 |   8A   |   10A   |    8B    |
+---------------+--------+---------+----------+
| 15:30 - 16:55 |   9A   |   11A   |    9B    |
+---------------+--------+---------+----------+
| 17:30 - 18:55 |   12A  |   14A   |    12B   |
+---------------+--------+---------+----------+
| 17:00 - 20:25 |   13A  |   15A   |    13B   |
+---------------+--------+---------+----------+

For Wednesday:-
+---------------+-----------+
|      Time     | Wednesday |
+---------------+-----------+
|  8:30 - 9:25  |     7A    |
+---------------+-----------+
|  9:30 - 10:55 |     5A    |
+---------------+-----------+
| 11:05 - 12:30 |     6A    |
+---------------+-----------+
| 14:00 - 14:55 |     X1    |
+---------------+-----------+
| 15:00 - 15:55 |     X2    |
+---------------+-----------+
| 16:00 - 16:55 |     X3    |
+---------------+-----------+
| 17:30 - 18:55 |     XC    |
+---------------+-----------+
| 19:00 - 20:25 |     XD    |
+---------------+-----------+

For Friday:-
+---------------+--------+
|      Time     | Friday |
+---------------+--------+
|  8:30 - 9:25  |   7B   |
+---------------+--------+
|  9:30 - 10:55 |   5B   |
+---------------+--------+
| 11:05 - 12:30 |   6B   |
+---------------+--------+
| 14:00 - 15:25 |   10B  |
+---------------+--------+
| 15:30 - 16:55 |   11B  |
+---------------+--------+
| 17:30 - 18:55 |   14B  |
+---------------+--------+
| 19:00 - 20:25 |   15B  |
+---------------+--------+
"""

from collections import defaultdict

def get_headers():
    header = ('Time', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
    return header



def get_time_maps():
    time_map = [
        '8:30 - 9:25',
        '9:30 - 10:25',
        '10:35 - 10:55',
        '10:55 - 11:30',
        '11:35 - 12:30',
        '12:30 - 14:00',
        '14:00 - 14:55',
        '15:00 - 15:25',
        '15:25 - 15:55',
        '16:00 - 16:55',
        '17:00 - 17:30',
        '17:30 - 18:55',
        '19:00 - 20:25'
    ]
    return time_map

def get_slot_maps():
    slot_maps = {
        '1A' : 'B2',
        '2A' : 'B3',
        '3A' : 'B4:B5',
        '4A' : 'B6',
        '8A' : 'B8:B9',
        '9A' : 'B10:B11',
        '12A': 'B13',
        '13A': 'B14',
        '4B' : 'C2',
        '1B' : 'C3',
        '2B' : 'C4:C5',
        '3B' : 'C6',
        '10A': 'C8:C9',
        '11A': 'C10:C11',
        '14A': 'C13',
        '15A': 'C14',
        '7A' : 'D2',
        '5A' : 'D3:D4',
        '6A' : 'D5:D6',
        'X1' : 'D8',
        'X2' : 'D9:D10',
        'X3' : 'D11',
        'XC' : 'D13',
        'XD' : 'D14',
        '3C' : 'E2',
        '4C' : 'E3',
        '1C' : 'E4:E5',
        '2C' : 'E6',
        '8B' : 'E8:E9',
        '9B' : 'E10:E11',
        '12B': 'E13',
        '13B': 'E14',
        '7B' : 'F2',
        '5B' : 'F3:F4',
        '6B' : 'F5:F6',
        '10B' : 'F8:F9',
        '11B' : 'F10:F11',
        '14B': 'F13',
        '15B': 'F14',
    }
    return slot_maps

def get_sub_slots():
    sub_slots = {
        '1' : ['1A', '1B', '1C'],
        '2' : ['2A', '2B', '2C'],
        '3' : ['3A', '3B', '3C'],
        '4' : ['4A', '4B', '4C'],
        '5' : ['5A', '5B'],
        '6' : ['6A', '6B'],
        '7' : ['7A', '7B'],
        '8' : ['8A', '8B'],
        '9' : ['9A', '9B'],
        '10' : ['10A', '10B'],
        '11' : ['11A', '11B'],
        '12' : ['12A', '12B'],
        '13' : ['13A', '13B'],
        '14' : ['14A', '14B'],
        '15' : ['15A', '15B'],
        'Lx' : ['X1', 'X2', 'X3'],
        'L1' : ['8A', '9A'],
        'L2' : ['10A', '11A'],
        'L3' : ['8B', '9B'],
        'L4' : ['10B', '11B'],
        'L5' : ['5A', '6A'],
        'L6' : ['5B', '6B']

    }
    return sub_slots

def get_color_maps(slot_num):
    color_map = defaultdict(lambda : '#FFFFFF')

    color_map['1A'] = '#C6EFCE'
    color_map['1B'] = '#C6EFCE'
    color_map['1C'] = '#C6EFCE'

    color_map['2A'] = '#FFC7CE'
    color_map['2B'] = '#FFC7CE'
    color_map['2C'] = '#FFC7CE'

    color_map['3A'] = '#FFE598'
    color_map['3B'] = '#FFE598'
    color_map['3C'] = '#FFE598'

    color_map['4A'] = '#9CC2E5'
    color_map['4B'] = '#9CC2E5'
    color_map['4C'] = '#9CC2E5'

    color_map['5A'] = '#D9D2E9'
    color_map['5B'] = '#D9D2E9'

    color_map['6A'] = '#FFFFCC'
    color_map['6B'] = '#FFFFCC'

    color_map['7A'] = '#CFE2F3'
    color_map['7B'] = '#CFE2F3'

    color_map['8A'] = '#D9D9D9'
    color_map['8B'] = '#D9D9D9'

    color_map['9A'] = '#D9D9D9'
    color_map['9B'] = '#D9D9D9'

    color_map['10A'] = '#C27BA0'
    color_map['10B'] = '#C27BA0'

    color_map['11A'] = '#C27BA0'
    color_map['11B'] = '#C27BA0'

    color_map['X1'] = '#FF8370'
    color_map['X2'] = '#FF8370'
    color_map['X3'] = '#FF8370'

    color_map['12A'] = '#FED8B1'
    color_map['12B'] = '#FED8B1'

    color_map['13A'] = '#B4C6E7'
    color_map['13B'] = '#B4C6E7'

    color_map['14A'] = '#FBC5E2'
    color_map['14B'] = '#FBC5E2'

    color_map['15A'] = '#DEAAFF'
    color_map['15B'] = '#DEAAFF'

    color_map['XC'] = '#FFE9DC'
    color_map['XD'] = '#FFE9DC'

    return color_map[slot_num]
