""""
一、分治法求解（分解，解决，合并）
将问题划分为两个规模求解，可以出现三种情况：
    1、最大数组位于左侧（low-mid）；
    2、最大数组位于右侧（mid-height）；
    3、最大数组包括了中点（i-mid)+(mid+1-j);
分治法子步骤：
    1、求每一侧的最大子数组，只需要从mid为起点一直相加，如果大于则保存
    2、判断最大子数组是否包括mid，如果包括则合并两侧
    3、返回最大子数组
"""

"""
    算法导论中演示的是一个必定跨中点的情况,所以这个递归是用来解决必定跨中点问题的,所以只需要考虑从mid出发至哪一点的情况即可
    花费时间 -> n=1,Θ(1)   n>1,2T(n/2)+θ(n)
"""


def find_max_crossing_subarray(l_array: list, r_array: list):
    # 左侧求最大
    left_i = 0
    max_left = float("-inf")  # 设定为负无穷
    l_sum = 0
    for i in reversed(range(len(l_array))):
        l_sum += l_array[i]
        if l_sum > max_left:
            max_left = l_sum
            left_i = i
    # 右侧求最大        
    right_i = 0
    max_right = float("-inf")
    r_sum = 0
    for i in range(len(r_array)):
        r_sum += r_array[i]
        if r_sum > max_right:
            max_right = r_sum
            right_i = i
    return max_left, left_i, max_right, right_i


def find_maximum_subarray(array: list):
    # 如果只有一个值，则返回
    if len(array) == 1:
        return array
    # 分别计算 左右两侧的最大连续数组
    mid = len(array) // 2
    l_subarray = find_maximum_subarray(array[0:mid])
    r_subarray = find_maximum_subarray(array[mid::])
    # 求得左，右两侧最大和与数组下标
    max_left, left_i, max_right, right_i = find_max_crossing_subarray(l_subarray, r_subarray)

    # 因为分成两array后，不能单独取右部分的array，所以只有两种情况，左>=左+右 和 左+右，不存在单独右，如果只取单独右则数组不连续
    if max_left >= max_right + max_left and max_left >= max_right:
        return l_subarray[left_i::]
    else:
        a_array = l_subarray[left_i::] + r_subarray[0:right_i + 1]
        return a_array


if __name__ == '__main__':
    print(find_maximum_subarray([-1, -2, -3, -4, -7, -6,-8]))
