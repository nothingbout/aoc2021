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

visited = set()

def find_paths(node):
    node_name = node['name']
    if node_name == 'end': return 1
    if node['big'] == False and node_name in visited: return 0

    visited.add(node_name)

    count = 0
    for dst in node['dests']:
        count += find_paths(nodes[dst])

    if node_name in visited:
        visited.remove(node_name)
    return count

print(find_paths(nodes['start']))