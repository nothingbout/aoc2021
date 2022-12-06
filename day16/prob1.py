with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

hex_to_bits = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',  
}

def bits_to_int(bits):
    num = 0
    for b in bits:
        num <<= 1
        if b == '1': num |= 1
    return num

def get_bits(input_bits, bits_index, bits_count):
    return (bits_index + bits_count, input_bits[bits_index:bits_index+bits_count])

class Packet:
    def __init__(self):
        self.version = None
        self.type_id = None
        self.sub_packets_bits_count = None
        self.sub_packets_count = None
        self.literal_value = None
        self.sub_packets = None

    def __str__(self):
        ss = f'version: {self.version}, type_id: {self.type_id}'
        if self.sub_packets_bits_count: ss += f', sub_packets_bits_count: {self.sub_packets_bits_count}'
        if self.sub_packets_count: ss += f', sub_packets_count: {self.sub_packets_count}'
        if self.literal_value: ss += f', literal_value: {self.literal_value}'
        if self.sub_packets:
            ss += f', len(sub_packets): {len(self.sub_packets)}'
        return ss

def parse_packet(input_bits, start_index):
    packet = Packet()

    # print(f'start_index: {start_index}')

    i = start_index
    (i, version_bits) = get_bits(input_bits, i, 3)
    packet.version = bits_to_int(version_bits)

    (i, type_id_bits) = get_bits(input_bits, i, 3)
    packet.type_id = bits_to_int(type_id_bits)

    # print(f'version: {packet.version}, type_id: {packet.type_id}')

    if packet.type_id == 4:
        all_num_bits = ''
        while True:
            (i, prefix) = get_bits(input_bits, i, 1)
            (i, num_bits) = get_bits(input_bits, i, 4)
            all_num_bits += num_bits
            if prefix == '0': break

        packet.literal_value = bits_to_int(all_num_bits)

    else:
        (i, length_type_id) = get_bits(input_bits, i, 1)
        if length_type_id == '0':
            (i, sub_packets_bits_count_bits) = get_bits(input_bits, i, 15)
            packet.sub_packets_bits_count = bits_to_int(sub_packets_bits_count_bits)
            # print(f'sub_packets_bits_count: {packet.sub_packets_bits_count}')
        else:
            (i, sub_packets_count_bits) = get_bits(input_bits, i, 11)
            packet.sub_packets_count = bits_to_int(sub_packets_count_bits)
            # print(f'sub_packets_count: {packet.sub_packets_count}')

    if packet.sub_packets_count:
        packet.sub_packets = []
        for _ in range(packet.sub_packets_count):
            (i, sub_packet) = parse_packet(input_bits, i)
            packet.sub_packets.append(sub_packet)
    elif packet.sub_packets_bits_count:
        packet.sub_packets = []
        sub_packets_start_index = i
        while i - sub_packets_start_index < packet.sub_packets_bits_count:
            (i, sub_packet) = parse_packet(input_bits, i)
            packet.sub_packets.append(sub_packet)

    # print(packet)

    return (i, packet)

def print_packet_hierarchy(packet, depth):
    print('  ' * depth + f'{packet}')
    if packet.sub_packets:
        for sub_packet in packet.sub_packets:
            print_packet_hierarchy(sub_packet, depth + 1)

def get_version_sum(packet):
    sum = packet.version
    if packet.sub_packets:
        for sub in packet.sub_packets:
            sum += get_version_sum(sub)
    return sum

for line in lines:
    input_bits = ''.join([hex_to_bits[c] for c in line])

    (_, root_packet) = parse_packet(input_bits, 0)
    # print_packet_hierarchy(root_packet, 0)
    print(f'version sum: {get_version_sum(root_packet)}')
