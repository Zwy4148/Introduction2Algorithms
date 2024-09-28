"""
堆排序：分为大堆和小堆，以下为大堆方法
步骤：
1、把数组排序成大堆
2、把大堆头尾互换，然后把尾排除在数组外，对数组进行构造大堆，重复过程
"""
import numpy as np

# 该函数用来调整一个堆为最大堆
# 为了最后排序方便，增加一个参数n，是A要排序的长度
def max_heapify(A: list, i, n):
    max_node = i
    left = (i << 1) + 1  # 因为这是从0开始的根节点，所以直接左移有1的偏差值
    right = (i << 1) + 2
    # 判断左节点
    if left < n and A[left] > A[max_node]:
        max_node = left
    # 判断右节点
    if right < n and A[right] > A[max_node]:
        max_node = right
    # 如果堆变化了，则交换然后一直往下递归，把小的值下推
    if max_node != i:
        A[max_node], A[i] = A[i], A[max_node]
        max_heapify(A, max_node, n)


# 该函数用来调整一个list成为最大堆，先从叶子节点开始向上排序成最大堆
def build_max_heap(A):
    for i in range(int(len(A) / 2), -1, -1):
        max_heapify(A, i, len(A))


# 堆排序算法主体
def heapsort(A):
    build_max_heap(A)
    a_len = len(A)
    # n -1 开始 到 0，进行n次头尾互换
    for i in range(a_len - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, 0, i)
    print(A)


if __name__ == '__main__':
    heapsort([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
