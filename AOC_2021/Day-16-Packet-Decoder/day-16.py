
'''
Basic pseudocode

def process_packets():
  process packet header
  if expecting sub-packets with n bits:
    process_packets(bit_limit=n)
  if expecting n sub-packets:
    process_packets(packet_limit=n)

def parse(text):
  version, remaining_text = ...
  typ, remaining_text = ...
  # ...
  sz, remaining_text = ...
  while sz > 0:
    subpacket, rest = parse(remaining_text)
    sz -= len(remaining_text) - len(rest)
    remaining_text = rest
  return packet, remaining_text

'''

# Convert hex into bits
# bin(int(INPUT, 16))[2:]


from math import prod
from aoc import *


def to_bin(hexchar):
    return f"{int(hexchar, 16):04b}"


def to_decimal(binary_digits):
    return int(binary_digits, 2)


# print(to_bin("D2FE28"))  # 110 100 10111 11110 00101 000
# print(to_decimal("00000000011"))  # 110 100 1 0111 1 1110 0 0101 000


# Packets with type id 4
# linx_filename = "sample.txt"
# windows_filename = "AOC_2021\Day-16-Packet-Decoder\sample.txt"

# with open(windows_filename) as f:
#     data = "".join(f"{int(x,16):04b}" for x in f.read().strip())

# packet_version = to_decimal(data[0:3])
# type_id = to_decimal(data[3:6])

# # Literal value
# if type_id == 4:
#     while len(data) % 4 != 0:
#         data = "0" + data
#     start = 0
#     data_group_list = []
#     data_group = data[6:]

#     while (data_group):
#         print(f"data_group = {data_group}")
#         if int(data_group[0]) == 1 and len(data_group) >= 5:
#             print("First 5 bits")
#             print("Adding the first 4 bits of the number")
#             print(data_group[start + 1:start+5])
#             data_group_list.append(data_group[start + 1:start+5])
#         elif int(data_group[0]) == 0 and (len(data_group) >= 5):
#             # It has reached the last group
#             print("Last 4 bits")
#             data_group_list.append(data_group[start + 1:start+5])
#             break

#         # Slice the first 5 bits
#         data_group = data_group[start+5:]
#         print(f"data_group_list = {data_group_list}")
#     print(to_decimal("".join(data_group_list)))
# else:
#     if int(data[6:7]) == 0:
#         total_length_in_bits = to_decimal(data[7:22])
#         print(
#             f'The length of the sub -packets in bits = {total_length_in_bits}')
#     else:
#         number_of_sub_packets = data[7:18]
#         print(f'number of subpackets = {to_decimal(number_of_sub_packets)}')


linx_filename = "input.txt"
windows_filename = "AOC_2021\Day-16-Packet-Decoder\input.txt"

s = ''
with open(windows_filename) as reader:
    for line in reader:
        s += str(line)

binary = bin(int.from_bytes(bytes.fromhex(s), 'big'))[2:].rjust(len(s)*4, '0')
print(binary)

part1 = 0


def parse_packets(b_str: str, max_packets: int):
    global part1
    packets = []
    i = 0
    while i+6 < len(b_str) and len(packets) < max_packets:
        ver = int(b_str[i:i+3], 2)
        part1 += ver
        typ_id = int(b_str[i+3:i+6], 2)
        i += 6
        if typ_id == 4:
            n = ''
            while b_str[i] == '1':
                n += b_str[i+1:i+5]
                i += 5
            n += b_str[i+1:i+5]
            i += 5
            packets.append(int(n, 2))
        else:  # operator
            len_id = int(b_str[i], 2)
            i += 1
            if len_id == 0:  # next 15 bits
                total_len_of_subpackets = int(b_str[i:i+15], 2)
                i += 15
                added, added_len = parse_packets(
                    b_str[i:i+total_len_of_subpackets], float('inf'))
            elif len_id == 1:  # next 11 bits
                number_of_subpackets = int(b_str[i:i+11], 2)
                i += 11
                added, added_len = parse_packets(
                    b_str[i:], number_of_subpackets)
            i += added_len

            if typ_id == 0:
                packets.append(sum(added))
            elif typ_id == 1:
                packets.append(prod(added))
            elif typ_id == 2:
                packets.append(min(added))
            elif typ_id == 3:
                packets.append(max(added))
            elif typ_id == 5:
                assert len(added) == 2
                packets.append(int(bool(added[0] > added[1])))
            elif typ_id == 6:
                assert len(added) == 2
                packets.append(int(bool(added[0] < added[1])))
            elif typ_id == 7:
                assert len(added) == 2
                packets.append(int(bool(added[0] == added[1])))
    return packets, i


print('part2:', parse_packets(binary, float('inf'))[0][0])
print(part1)
