'''
冒泡排序
最坏情况：n²
'''


def bubble_sort(array: list) -> list:
    # 需要循环n -1次,因为最后一次只有一个数无需排序
    for i in range(len(array) - 1):
        # 每次都需要从头比较，但第n遍过后末尾第n位起都是排序好的所以，只需要比较到n-i次，还-1是因为底下有个j+1
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    print(bubble_sort([9, 6, 5, 4, 82, 14, 54, 5, 45, 47, 64, 546, 54, 1, 2, 3]))
