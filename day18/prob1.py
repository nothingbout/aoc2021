class Node:
    def __init__(self, num = None, left_node = None, right_node = None):
        self.parent = None
        self.num = num
        self.set_left_node(left_node)
        self.set_right_node(right_node)

    def __str__(self):
        if self.is_num():
            return f'{self.num}'
        else:
            left_str = str(self.left_node)
            right_str = str(self.right_node)

            if self.left_node and self.left_node.parent != self:
                left_str = '*' + left_str

            if self.right_node and self.right_node.parent != self:
                right_str = '*' + right_str

            return f'[{left_str},{right_str}]'

    def set_left_node(self, node):
        self.left_node = node
        if node: node.parent = self

    def set_right_node(self, node):
        self.right_node = node
        if node: node.parent = self

    def replace_node(self, old_node, new_node):
        if old_node == self.left_node:
            self.set_left_node(new_node)
        elif old_node == self.right_node:
            self.set_right_node(new_node)
        else:
            raise "wut"

    def is_num(self):
        return True if self.num is not None else False

    def is_pair(self):
        return True if self.num is None else False

    def is_leaf(self, pair_can_be_leaf):
        if self.is_num(): return True
        if pair_can_be_leaf and self.left_node.is_num() and self.right_node.is_num(): return True
        return False

    def depth(self):
        if not self.parent: return 0
        return 1 + self.parent.depth()

    def magnitude(self):
        if self.is_num(): return self.num
        return 3 * self.left_node.magnitude() + 2 * self.right_node.magnitude()

def parse_and_ignore(input_str, input_index, str):
    check_str = input_str[input_index:input_index + len(str)]
    if check_str != str:
        raise f'Unexpected str: {check_str}, expected: {str}'
    return input_index + len(str)
    
def parse_num_node(input_str, input_index):
    num_str = ''
    while True:
        c = str(input_str[input_index])
        if not c.isnumeric(): break
        num_str += c
        input_index += 1
    return (input_index, Node(num = int(num_str)))

def parse_pair_node(input_str, input_index):
    input_index = parse_and_ignore(input_str, input_index, '[')

    if input_str[input_index] == '[':
        (input_index, left_node) = parse_pair_node(input_str, input_index)
    else:
        (input_index, left_node) = parse_num_node(input_str, input_index)

    input_index = parse_and_ignore(input_str, input_index, ',')

    if input_str[input_index] == '[':
        (input_index, right_node) = parse_pair_node(input_str, input_index)
    else:
        (input_index, right_node) = parse_num_node(input_str, input_index)

    input_index = parse_and_ignore(input_str, input_index, ']')

    return (input_index, Node(left_node = left_node, right_node = right_node))

with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

input_pairs = []
for line in lines:
    (_, pair) = parse_pair_node(line, 0)
    # print(pair)
    input_pairs.append(pair)

def get_leftmost_leaf(node, pair_can_be_leaf):
    while True:
        if node.is_leaf(pair_can_be_leaf): 
            return node
        elif node.left_node:
            node = node.left_node
        elif node.right_node:
            node = node.right_node
        else:
            raise "wut"
        

def get_next_left_leaf(node, pair_can_be_leaf):
    while True:
        if not node.parent: return None
        if node == node.parent.right_node: 
            node = node.parent.left_node
            break
        node = node.parent
    
    while not node.is_leaf(pair_can_be_leaf): node = node.right_node
    return node

def get_next_right_leaf(node, pair_can_be_leaf):
    while True:
        if not node.parent: return None
        if node == node.parent.left_node: 
            node = node.parent.right_node
            break
        node = node.parent
    
    while not node.is_leaf(pair_can_be_leaf): node = node.left_node
    return node

def add_pairs(a, b):
    pair = Node(left_node=a, right_node=b)
    return pair

def explode_leftmost(root_pair):
    node = get_leftmost_leaf(root_pair, True)
    while node:
        if node.is_pair() and node.depth() >= 4:
            # print(node)
            
            next_left = get_next_left_leaf(node.left_node, False)
            # print(next_left)
            if next_left: next_left.num += node.left_node.num

            next_right = get_next_right_leaf(node.right_node, False)
            # print(next_right)
            if next_right: next_right.num += node.right_node.num

            node.parent.replace_node(node, Node(num = 0))
            return True

        node = get_next_right_leaf(node, True)
    return False

def split_leftmost(root_pair):
    node = get_leftmost_leaf(root_pair, False)
    while node:
        if node.num >= 10:
            left_node = Node(num = node.num // 2)
            right_node = Node(num = node.num // 2 + node.num % 2)
            node.parent.replace_node(node, Node(left_node=left_node, right_node=right_node))
            return True

        node = get_next_right_leaf(node, False)
    return False

root_pair = input_pairs[0]

for pair in input_pairs[1:]:
    root_pair = add_pairs(root_pair, pair)
    # print(f'{root_pair}')
    while explode_leftmost(root_pair) or split_leftmost(root_pair):    
    #     print(f'{root_pair}')
        pass
    # print('')
    print(f'{root_pair}')

print(f'magnitude: {root_pair.magnitude()}')