# reference:
# https://visualgo.net/en/sorting?slide=1


# Bubble Sort algorithm
def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list


my_list = [4, 3, 6, 5, 1, 2]

print('bubble sort')
print(bubble_sort(my_list))


# Selection sort algorithm
# one exchange for each pass, required n-1 passes
def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


print('selection sort')
print(selection_sort([4, 3, 6, 5, 1, 2]))

# insertion sort algorithm
# insert one at at time


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


print('insertion sort')
print(insertion_sort([4, 3, 6, 5, 1, 2]))

# shell sort algorithm


def shell_sort(my_list):
    sub_list_count = len(my_list) // 2

    while sub_list_count > 0:
        for start in range(sub_list_count):
            gap_insertion_sort(my_list, start, sub_list_count)

        sub_list_count = sub_list_count // 2

    return my_list


def gap_insertion_sort(arr, start, gap):

    for i in range(start + gap, len(arr), gap):
        current = arr[i]
        position = i

        while position >= gap and arr[position - gap] > current:
            arr[position] = arr[position - gap]
            position = position - gap

        arr[position] = current


print('shell sort')
print(shell_sort([7, 4, 8, 6, 5, 1, 2, 3, 9]))

# Merge sort algorithm
# divide and conquer algorithm
# helper function for the merge sort


def merge(list1, list2):
    combined = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):

        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list

    mid = int(len(my_list)/2)
    left = my_list[:mid]
    right = my_list[mid:]

    return merge(merge_sort(left), merge_sort(right))


print('merge sort')
print(merge_sort([4, 3, 6, 5, 1, 2, 9, 8, 7]))

# O(n) for merge sort space complexity
# O(n log n) for time complexity for merge sort

# Quick sort algorithm
# divide and conquer algorithm
# helper function for quick sort
# O(n log n) best and average case
# worst case O(n^2) if already sorted data


def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort(my_list):

    def sort_helper(my_list, left, right):
        if left < right:
            pivot_index = pivot(my_list, left, right)
            sort_helper(my_list, left, pivot_index-1)
            sort_helper(my_list, pivot_index+1, right)

    sort_helper(my_list, 0, len(my_list) - 1)

    return my_list


print('quick sort')
quick_list = [4, 6, 1, 7, 3, 2, 5]
print(pivot(quick_list, 0, 6))
print(quick_list)

print(quick_sort(quick_list))


# alternative implemenatation
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print('quicksort alternative')
print(quicksort([4, 6, 1, 7, 3, 2, 5]))
