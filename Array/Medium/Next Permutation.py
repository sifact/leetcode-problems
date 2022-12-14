# Computes the next lexicographical permutation of the specified
# list in place, returning weather a next permutation existed
# Returns False when the argument is already the last possible permutation


def next_permutation(arr):
    # Find non-increasing suffix
    arr = list(arr)
    i = len(arr) - 1

    while i > 0 and arr[i - 1] >= arr[i]:  # pivot arr[i - 1]
        i -= 1
    if i == 0:
        return sorted(arr)

    # Find rightmost successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:  # greater than pivot
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]  # swap pivot

    # Reverse suffix
    arr[i:] = arr[len(arr) - 1: i - 1: - 1]

    return arr


n = input()
print(next_permutation(n))
