import os
os.system("clear")

def pop_blocks(blocks):
    massiv = []

    for block in blocks:
        if massiv and block == massiv[-1]:
            while massiv and block == massiv[-1]:
                massiv.pop()
        else:
            massiv.append(block)

    return massiv

print(pop_blocks(['B', 'B', 'A', 'C', 'A', 'A', 'C']))

# Answer must be [A]
