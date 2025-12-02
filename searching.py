# Takes a sorted array and searches the needed element by splitting it down the middle
# Each guess attempt takes away half of the remaining options.
# O(log2n) efficient in time, O(n) efficient in memory

def binary_search(array: list, number: int) -> int | None:
    low, high = 0, len(array) - 1
    while low <= high:
        guess = int((high + low) / 2)
        if array[guess] == number:
            return guess
        if array[guess] < number:
            low = guess + 1
        if array[guess] > number:
            high = guess - 1
    return None

if __name__ == '__main__':
    print(binary_search([3, 6, 78, 100, 5678], 100))
    print(binary_search([3, 6, 78, 100, 5678], 4))