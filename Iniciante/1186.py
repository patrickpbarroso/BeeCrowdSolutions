def fill_matrix():
    matrix = []
    for i in range(0, 12):
        row = []
        for j in range(0, 12):
            value = float(input())
            row.append(value)
        matrix.append(row)
    return matrix

def get_sum_or_mean(operation, matrix):
    first = 11
    result = 0
    for i in range(1, 12):
        for j in range(first, 12):
            result += matrix[i][j]
        first -= 1
    if operation == 'M':
        n = (len(matrix)**2 - len(matrix))/2
        return result/n
    return result

operation = input()
matrix = fill_matrix()
result = get_sum_or_mean(operation, matrix)
print("{:.1f}".format(result))