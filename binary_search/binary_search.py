def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = int((low + high) / 2) + 1
        if my_list[mid] == target:
            return mid
        elif target < my_list[mid]:
            high = mid - 1
        elif target > my_list:
            low = mid + 1
        else:
            return None


if __name__ == '__main__':
    my_list = [1, 2, 4, 6, 8, 9]
    target = 2
    print(binary_search(my_list, target))
