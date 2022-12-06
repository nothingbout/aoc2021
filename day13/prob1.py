with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

dots = []
folds = []
parsing_folds = False

for line in lines:
    if len(line) == 0:
        parsing_folds = True
        continue

    if not parsing_folds:
        dots.append(tuple([int(x) for x in line.split(',')]))
    else:
        folds.append(tuple(line.split()[2].split('=')))

dots = set(dots)

#print(dots)
#print(folds)

def do_fold(dot, fold):
    sep = int(fold[1])
    if fold[0] == 'x':
        if dot[0] > sep:
            return (sep + (sep - dot[0]), dot[1])
    elif fold[0] == 'y':
        if dot[1] > sep:
            return (dot[0], sep + (sep - dot[1]))
    return dot

for fold in folds[:1]:
    dots = set(map(lambda x: do_fold(x, fold), dots))

print(len(dots))
