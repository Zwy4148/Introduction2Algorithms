"""
和归并算法一样，快速排序也是用了分治法
快速排序：最坏情况 n² 但他的期望时间是 nlgn
步骤：
    1 将数组划分为两个子数组a,b(a为左边，b为右边)
    2 递归
    3 使得a中数组没一个元素都小于等于mid，mid也始终小于b数组的元素
"""
from random import random, randint

"""
快速排序常规版本
    通过不断把数组以最后一位的值为中点，分为左侧，右侧两部分数组，左侧小于A[n]，右侧大于，然后把最后的值放置分界处
返回分界处的下标，左右两侧都不断进行递归，就可以排序完成
"""


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


"""
快速排序随机版本
为了达到期望预期值，把原本最后一位的A[n]换成随机的A[Random]
"""


def random_partition(A, p, r):
    i = int(randint(p, r))
    A[r], A[i] = A[i], A[r]
    q = partition(A, p, r)
    return q


def random_quicksort(A, p, r):
    if p < r:
        q = random_partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


if __name__ == '__main__':
    A = [1, 8, 9, 6, 5, 4, 1, 2, 5]
    random_quicksort(A, 0, 8)
    print(A)
