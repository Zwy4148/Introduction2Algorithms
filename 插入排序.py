'''
插入排序
最坏情况：n²
'''


def insertion_sort(array) -> list:
    # 从头遍历n次
    for i in range(len(array)):
        j = i
        # 选中的值和后面的值比较，如果前面的小于后面的则交换，然后往前比较直至比较完所有
        while j - 1 >= 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
    return array


if __name__ == '__main__':
    print(insertion_sort([1, 5, 6, 56, 56, 856, 86, 5, 3625, 3, 25]))
