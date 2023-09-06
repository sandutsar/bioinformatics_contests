import os
from tqdm import tqdm

ERROR = 1e-4

path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(path, 'tests.txt'), 'r') as file:
    data = [line.strip() for line in file.readlines()]

lines = int(data[0])
result = list()

for x in tqdm(range(1, lines + 1)):
    n1, a, b = map(float, data[x].split())
    for _  in range(int(1e3)):
        n1 = a*n1 - b*n1*n1
    if n1 < ERROR:
        result += [0]
    elif n1 == 'nan':
        result += [-1]
    else:
        result += [n1]

print('\n'.join([str(x) for x in result]))
