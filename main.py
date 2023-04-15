'''
Merge Sort
-------------------------------------------------------------
'''


def merge_sort(aList):
    print("Dividing ", aList)

    if len(aList) > 1:
        mid_point = len(aList) // 2
        left_half = aList[:mid_point]
        right_half = aList[mid_point:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                aList[k] = left_half[i]
                i += 1
            else:
                aList[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            aList[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            aList[k] = right_half[j]
            j += 1
            k += 1

    print("Merging ", aList)


if __name__ == '__main__':
    a_list = [45, 7, 85, 24, 60, 25, 38, 63, 1]
    merge_sort(a_list)
    print(a_list)