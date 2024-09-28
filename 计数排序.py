"""
计数排序：

"""

def counting_sort(A,B,k):
    C = [0] * k
    B = [0] * len(A)
    # 计算A中的各个值数量
    for j in range(len(A)):
        C[A[j]] += 1
    # 把每个元素出现的最后坐标位置标出在C中，例如有2个0.C[0] = 2,3个1则C[1]=C[0]+3

    for n in range(1,k):
        C[n] = C[n] + C[n-1]
    # 1、循环放元素到B中，例如A[N] = 0,首先通过C[0]获取到这个元素应该放在B中哪个位置,B[2]
    # 2、然后通过C[0] -1 = 1 ，来保证下一个0要放在B[1]位置
    for x in reversed(range(1,len(A))):
        # 由于数组的下标是由0开始，所以需要-1来确保数的位置正确
        B[C[A[x]] -1] = A[x]
        C[A[x]] -= 1

    print(B)


if __name__ == '__main__':
    counting_sort([0,0,1,2,3,1,1,2,3,1,3],[],4)