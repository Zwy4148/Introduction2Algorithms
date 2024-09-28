"""
优先队列：一种用来维护元素构成的集合S的数据结构，其中每个元素都有一个关键字key，关键字key就是值本身大小
优先队列可以用堆来实现,所以模仿书本的实现，需要用到堆排序的库
python中优先队列在heapq库中，需要注意的是heapq是小堆排序，heapq[0]是最小值


优先队列包含以下功能：
    1 insert（S,X）把元素x插入集合S中
    2 maximum（s）返回s中的最大关键字元素
    3 extract-max（S） 去除和返回s中的最大关键字元素
    4 increase-key（s，x，k）将元素s的关键字增加到k

小问题：如何使用优先队列实现先进先出队列，以及用其来实现栈
"""
import heapq
import 堆排序 as heap_sort


# 返回s中的最大关键词元素，类似heap[0]，但其返回的是最小值
def heap_maximum(A):
    return A[0]


#返回最大值并删除，就是pop，类似heappop(heap)，但其返回的是最小值
def heap_extract_max(A):
    n = len(A)
    assert n == 0, "error heap underflow"
    max = A[0]
    # 交换头尾，重新排序前n-1个，截断
    A[0], A[n - 1] = A[n - 1], A[0]
    heap_sort.max_heapify(A, 0, n - 1)
    A = A[:n - 1]
    return max



