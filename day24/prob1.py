input_file = 'input.txt'

def parse_param(param):
    return int(param) if param[-1].isnumeric() else param[0]

def parse_input():
    with open(input_file, 'r') as f:
        lines = [line.rstrip('\r\n') for line in f.readlines()]

    instructions = []
    for line in lines:
        parts = line.split()
        if len(parts) == 3: instructions.append((parts[0], parse_param(parts[1]), parse_param(parts[2])))
        else: instructions.append((parts[0], parse_param(parts[1]), None))

    return instructions

def get_param_value(param, memory):
    if isinstance(param, int): return param
    match param:
        case 'w': return memory[0]
        case 'x': return memory[1]
        case 'y': return memory[2]
        case 'z': return memory[3]

def eval_instruction(instruction, memory, input = None):
    op, param1, param2 = instruction
    match op:
        case 'inp': 
            out_val = input
        case 'add':
            out_val = get_param_value(param1, memory) + get_param_value(param2, memory)
        case 'mul':
            out_val = get_param_value(param1, memory) * get_param_value(param2, memory)
        case 'div':
            out_val = int(get_param_value(param1, memory) / get_param_value(param2, memory))
        case 'mod':
            out_val = get_param_value(param1, memory) % get_param_value(param2, memory)
        case 'eql':
            out_val = 1 if get_param_value(param1, memory) == get_param_value(param2, memory) else 0

    w, x, y, z = memory
    match param1:
        case 'w': w = out_val
        case 'x': x = out_val
        case 'y': y = out_val
        case 'z': z = out_val
    return (w, x, y, z)

def get_inputs(input_num):
    return [int(x) for x in str(input_num)]

instructions = parse_input()

# input_num = 99999999999999
# while True:
#     input_index = 0
#     inputs = get_inputs(input_num)
#     if not 0 in inputs:
#         memory = (0, 0, 0, 0)
#         for instr in instructions:
#             memory = eval_instruction(instr, memory, inputs[input_index] if input_index < len(inputs) else None)
#             if instr[0] == 'inp': 
#                 # print(f'{input_index} -> {inputs[input_index]}')
#                 input_index += 1
#                 # print(f'{instr} {memory}')

#         print(f'{input_num} -> {memory}')
#     if memory[0] == 0: 
#         # print(f'{input_num} -> {memory}')
#         break
#     input_num -= 1

def add_memory(memories, memory, input_num):
    existing = memories.get(memory, -1)
    if input_num > existing:
        memories[memory] = input_num

memories = {}
memories[(0, 0, 0, 0)] = 0

for instr_index in range(len(instructions)):
    instr = instructions[instr_index]
    # print(f'{memory}  {instr}')

    if instr[0] == 'inp':
        nm = {}
        for (memory, input_num) in memories.items(): 
            add_memory(nm, (0, 0, 0, memory[3]), input_num)
        memories = nm

    new_memories = {}
    for (memory, input_num) in memories.items():
        if instr[0] == 'inp':
            if memory[3] > 10000000: continue 
            for i in range(1, 10):
                new_memory = eval_instruction(instr, memory, i)
                add_memory(new_memories, new_memory, input_num * 10 + i)
        else:
            new_memory = eval_instruction(instr, memory)
            add_memory(new_memories, new_memory, input_num)

    print(f'{instr_index + 1} / {len(instructions)}: {len(new_memories)}')

    memories = new_memories

# print(len(list(filter(lambda m: m[3] == 0, memories))))

for (memory, input_num) in memories.items():
    if memory[3] == 0:
        print(input_num)
