import sorting
import random


def isSorted(A, f):
    for i in range(0, len(A)-1):
        if not f(A[i], A[i+1]):
            return [False, i]
    return [True, -1]

def notSortedMsg(A, A_wrong, sortingAlgo):
    print("{} is wrong".format(sortingAlgo))
    print("The original problem is: \n {}".format(A))
    print("The error is: \n {}".format(A_wrong))
    

def testAlgo(A, sort_algo, name, errors, f):
    if not isSorted(sort_algo, f)[0]:
        notSortedMsg(A, sort_algo, name)
        errors[name] += 1

def main():
    number_of_random_tests = 100
    size_of_problems = 5
    filename = "test.txt"
    f = lambda x,y: x>y
    errors = {"insertion sort":0, "merge sort":0, "quick sort":0}
    
    for _ in range(number_of_random_tests):
        A = random.sample(range(size_of_problems), size_of_problems)
        insertion_sort = sorting.insertionSort([x for x in A], f)
        merge_sort = sorting.mergeSort([x for x in A], f)
        quick_sort = [x for x in A]
        sorting.quickSort(quick_sort, f, 0, len(A)-1)
   
        testAlgo(A, insertion_sort, "insertion sort", errors, f)
        testAlgo(A, merge_sort, "merge sort", errors, f)
        testAlgo(A, quick_sort, "quick sort", errors, f)

    print("errors: \n {}".format(errors))

    
if __name__ == "__main__":
    main()

