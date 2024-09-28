"""
一般计算矩阵乘法，通过分解n*n为n/2 * n/2然后递归计算，需要进行8次乘法运算，8次加法运算
strassen算法，只需要十次加法和7次乘法运算

ps:
ndarray.shape() 返回的是行列数的list[row,col]
shape[0] 返回行，1为列
numpy.concatenate((a1, a2, ...), axis=0, out=None) 用于合并数组
axis代表沿着哪个轴合并，0则为沿着按行合并，1则为按列合并
"""
import numpy as np

"""
以下算法为书上给出的方法，仅仅适用于2的幂次方的矩阵间相乘
"""


def strassen_2(A: np.ndarray, B: np.ndarray):
    n = A.shape[0]
    if n == 1:
        return A * B
    # A矩阵分四组
    A11 = A[:n // 2, :n // 2]
    A12 = A[:n // 2, n // 2:]
    A21 = A[n // 2:, :n // 2]
    A22 = A[n // 2:, n // 2:]
    # B矩阵分四组
    B11 = B[:n // 2, :n // 2]
    B12 = B[:n // 2, n // 2:]
    B21 = B[n // 2:, :n // 2]
    B22 = B[n // 2:, n // 2:]

    S1 = B12 - B22
    S2 = A11 + A12
    S3 = A21 + A22
    S4 = B21 - B11
    S5 = A11 + A22
    S6 = B11 + B22
    S7 = A12 - A22
    S8 = B21 + B22
    S9 = A11 - A21
    S10 = B11 + B12
    # 递归计算出P值
    P1 = strassen_2(A11, S1)
    P2 = strassen_2(S2, B22)
    P3 = strassen_2(S3, B11)
    P3 = strassen_2(S3, B11)
    P4 = strassen_2(A22, S4)
    P5 = strassen_2(S5, S6)
    P6 = strassen_2(S7, S8)
    P7 = strassen_2(S9, S10)

    # 求出总合
    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7

    # 拼接
    return np.concatenate([np.concatenate([C11, C12], axis=1),
                           np.concatenate([C21, C22], axis=1)], axis=0)


"""

以下为可以适用于非2的幂次方的方法：填充为2次幂的矩阵
"""

def start_strassen(A: np.ndarray, B: np.ndarray):
    n = A.shape[0]
    if n % 2 != 0:
        row = pow(2,int(np.ceil(np.log2(n))))
        n_A = np.zeros([row,row])
        n_B = np.zeros([row,row])
        n_A[:n,:n] = A
        n_B[:n,:n] = B
        A = n_A
        B = n_B
    C = strassen_2(A,B)

    return C[:n,:n]


if __name__ == '__main__':
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    # 使用普通矩阵乘法进行比较
    result_normal = A.dot(B)
    result_strassen = start_strassen(A, B)
    print(result_normal)
    print(result_strassen)
