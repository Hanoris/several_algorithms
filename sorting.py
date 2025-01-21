#  Efficient for sorting small number of elements.
#  Represents the way you sort cards by rank in your hand.
#  O(n^2) in time, O(1) in memory
def insertion_sort(array: list) -> list:
    for i in range(1, len(array)):
        element = array[i]
        j = i - 1
        while j > -1 and array[j] > element:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = element
    return array


#  Efficient for sorting small number of elements.
#  You look for the smallest number in a subarray A[i:N] and exchange it with i.
#  O(n^2) in time, O(1) in memory
def selection_sort(array: list) -> list:
    for i in range(len(array) - 1):
        min_number = array[i]
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < min_number:
                min_number = array[j]
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


#  Efficient for sorting small number of elements.
#  You compare numbers that are near each other and swap them if needed.
#  The "heaviest" numbers gradually float up like a bubble.
#  O(n^2) in time, O(1) in memory
def bubble_sort(array: list) -> list:
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    print(insertion_sort([5, 2, 4, 6, 1, 3]))  # O(n^2) time, O(1) memory
    print(selection_sort([5, 2, 4, 6, 1, 3]))  # O(n^2) time, O(1) memory
    print(bubble_sort([5, 2, 4, 6, 1, 3]))  # O(n^2) time, O(1) memory


