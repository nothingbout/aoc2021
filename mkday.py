import os
import shutil
import sys

def mkfile(path):
    with open(path, 'w') as _:
        pass    

dirname = sys.argv[1]

os.mkdir(dirname)
# mkfile(os.path.join(dirname, 'prob1.py'))
shutil.copyfile('templates/prob_template.py', os.path.join(dirname, 'prob1.py'))
mkfile(os.path.join(dirname, 'prob2.py'))
mkfile(os.path.join(dirname, 'input.txt'))
mkfile(os.path.join(dirname, 'example_input.txt'))
