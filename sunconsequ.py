def rotate_matrix_clockwise(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

# Original matrix
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Rotated matrix
rotated_matrix = rotate_matrix_clockwise(original_matrix)
print(rotated_matrix)
