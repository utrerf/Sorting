def insertionSort(A, f):
    """ Inputs
            A: python list
            f: comparisson function
        Output
            A: Ordered python list using f
        Implementation details
            - A will be modified from it's original
            - O(n**2)
        Correctness
            - Initialization: A[0] is sorted
            - Maintenance: Assume A[0 to i-1] is sorted.
                           At i, we initialize j from i to 0
                           and swap A[j] with A[j-1] according 
                           to f until we don't need to swap
                           Thus, A[0 to i] is sorted
            - End: By maintenance, A[0 to len(A)-1] is sorted
    """
    for i in range(1, len(A)):
        for j in range(i, 0, -1):
            if f(A[j], A[j-1]):
                temp = A[j-1]
                A[j-1] = A[j]
                A[j] = temp
            else:
                break

    return A


def mergeSort(A, f):
    if len(A) > 1:
        A1 = mergeSort(A[:len(A)//2], f)
        A2 = mergeSort(A[len(A)//2:], f)
        return merge(A1, A2, f)
    return A


def merge(A1, A2, f):
    A = []
    i1,i2 = 0, 0
    while i1 < len(A1) or i2 < len(A2):
        if i1 >= len(A1) or (i2 < len(A2) and f(A2[i2], A1[i1])):
            A.append(A2[i2])
            i2 += 1
        else:
            A.append(A1[i1])
            i1 += 1
    return A


def quickSort(A, f, start, end):
    if start < end:
        pivot = partition(A, f, start, end)
        quickSort(A, f, start, pivot-1)
        quickSort(A, f, pivot+1, end)


def partition(A, f, start, end):
    x = A[end]
    i = start
    for j in range(start, end):
        if f(A[j], x):
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
            i += 1
    A[end] = A[i]
    A[i] = x
    return i

############################################################
################### DO NOT USE #############################
############################################################


def mergeSortFast(A, f):
    R = [x for x in A]
    mergeSortFastHelper(A, f, R, 0, len(A))


def mergeSortFastHelper(A, f, R, start, end):
    import pdb; pdb.set_trace()
    # ends are not looked at
    offset = (end - start)//2 
    mid = start + offset
    if offset > 0:
        mergeSortFastHelper(A, f, R, start, mid)
        mergeSortFastHelper(A, f, R, mid, end)
        mergeFast(A, f, R, start, mid, end)


def mergeFast(A, f, R, start, mid, end):
    i = start
    p1, p2 = start, mid
    end1, end2 = mid, end
    while i < end:
        if p1 >= end1 or f(R[p2], R[p1]):
            A[i] = R[p2]
            p2 += 1
        else:
            A[i] = R[p2]
            p1 += 1
        i += 1


###############################################################
################## END OF DO NOT USE ##########################
###############################################################

