'''
归并排序
最坏情况：nlgn
'''

def merge(l1,l2):
    i,j = 0,0;
    result = []
    #判断时候有一边已经为空
    while  i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    #直接相加剩余的数组
    result += l1[i:]
    result += l2[j:]
    return result
def merge_sort(array:list) -> list:
    middle = len(array) //2
    l_sort = array
    #判断是否已经归底
    if middle >= 1:
        l1 = merge_sort(array[:middle])
        l2 = merge_sort(array[middle:])
        l_sort = merge(l1,l2)
    return l_sort

if __name__ == '__main__':
    print(merge_sort([1, 3, 4, 5, 3, 2, 4, 5,2,3,4,52,2,31,3,213,21,3,1,31,3]))