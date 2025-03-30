import random

def create_array(n, m, min=1, max=100):
    array = [[0] * m for q in range(n)]
    mini = min
    for i in range(n):
        for j in range(m):
            array[i][j] = mini + random.randint(0, (max - mini) // (n * m - i * m - j)
            if (n * m - i * m - j) > 0 else 0)
            mini = array[i][j] + 1
    return array


def find_number(array, k):
    n = len(array)
    m = len(array[0])
    row = 0
    col = m - 1
    steps = 0

    while row < n and col >= 0:
        steps += 1
        if array[row][col] == k:
            return True, steps
        elif array[row][col] < k:
            row += 1 # вниз
        else:
            col -= 1 # влево
    return False, steps

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
array = create_array(n, m)
print('\n')
for row in array:
    print(row)
k = int(input("Enter the number found: "))
result, steps = find_number(array, k)
if result:
    print(f"Number {k} found; {steps} steps")
else:
    print(f"Number {k} not found")
