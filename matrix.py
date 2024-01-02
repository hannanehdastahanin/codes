def get():
    rows = int(input("enter number of rows: "))
    columns = int(input("enter number of columns: "))
    matrix = []
    print("enter matrix elements: ")
    for i in range(rows):
        row = list(map(int, input(f" ").split()))
        matrix.append(row)
    return matrix
input = get()
def bomb(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    def t(row,col):
         return 0 <= row < rows and 0 <= col < columns
    result = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 1:
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if t(x,y):
                        result[x][y] += 1
    return result
print("input matrix:")
for row in input:
    print(row)
output= bomb(input)
print("output matrix: ")
for row in output:
    print(row)
