def is_border(matrix, i, j):
    if (i == 0 or i == len(matrix)-1) or (j == 0 or j == len(matrix)-1):
        return True
    else:
        return False

def in_bounds(matrix, i, j):
    if i < 0 or i > len(matrix)-1 or j < 0 or j > len(matrix)-1:
        return False
    else:
        return True

def get_neighbors(matrix, i, j):
    n = [
        (i+1,j),
        (i-1,j),
        (i,j-1),
        (i,j+1)
    ]
    return n

def recurse(matrix, i, j, connections):
    neighbors = get_neighbors(matrix, i, j)
    for n in neighbors: 
        new_i = n[0]
        new_j = n[1]
        key = f'{new_i}{new_j}'
        if in_bounds(matrix, new_i, new_j) and matrix[new_i][new_j] == 1 and key not in connections:
            connections.append(key)
            recurse(matrix, new_i, new_j, connections)
        else:
            continue

def test(matrix):
    connections = []
    for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 1 and is_border(matrix, i, j):
                    recurse(matrix, i, j, connections)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                if f'{i}{j}' not in connections:
                    matrix[i][j] = 0
    
    return matrix

sample_in = [
    [1,0,0,0,0,0],
    [0,1,0,1,1,1],
    [0,0,1,0,1,0],
    [1,1,0,0,1,0],
    [1,0,1,1,0,0],
    [1,0,0,0,0,1]
]

test(sample_in)