# efficient

"""
def searchMatrix(matrix, target):
    if not matrix or target is None:
        return False

    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1

    while low <= high:
        mid = (low + high) // 2
        num = matrix[mid / cols][mid % cols]

        if num == target:
            return True
        elif num < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


# brute force:
def searchMatrix2(matrix, target):
    if not len(matrix):
        return False

    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    return False

a = list(map(int, input().split()))
n1 = int(input())
print(searhcMatrix(a, n1))
"""


def search_matrix(matrix, target):


    for row in matrix:
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2

            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

    return False


a = []
for i in range(int(input())):
    a.append(list(map(int, input().split())))
n = int(input())
print(search_matrix(a, n))






