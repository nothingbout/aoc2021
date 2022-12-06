with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

nodes = {}

def add_node(name):
    node = {'name': name, 'dests': [], 'big': name.isupper()}
    nodes[name] = node
    return node

for line in lines:
    a, b = tuple(line.split('-'))

    if not a in nodes: add_node(a)
    if not b in nodes: add_node(b)

    nodes[a]['dests'].append(b)
    nodes[b]['dests'].append(a)

visit_counts = {}
for node_name in nodes:
    visit_counts[node_name] = 0

def find_paths(node, multivisits):
    node_name = node['name']
    if node_name == 'end': return 1
    if node['big'] == False and visit_counts[node_name] > 0: 
        if multivisits > 0: return 0
        multivisits += 1

    visit_counts[node_name] += 1

    count = 0
    for dst in node['dests']:
        if dst == 'start': continue
        count += find_paths(nodes[dst], multivisits)

    visit_counts[node_name] -= 1

    return count

print(find_paths(nodes['start'], 0))