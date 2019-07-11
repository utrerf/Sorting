import sys
import utils
import sorting

def loadProblem(file="problem.txt", delimeter=",", data_type="int"):
    with open(file) as handle:
        # read the file, split using delimeter, and apply the data type
        problem = [eval(data_type)(x) for x in handle.read().split(delimeter)]
    return problem


def main():
    if len(sys.argv) > 4:
        problem = loadProblem(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        filename = utils.getOpenFileName("problem.txt")
        delimeter = utils.getDelimeter(",")
        data_type = utils.getDataType("int")
        problem = loadProblem(filename, delimeter, data_type)
        comparisson_function = utils.getComparissonFunction("lambda x,y: x>y")
    
    print("Sample items in the problem: %s" % problem[:10])
    
    f = eval(comparisson_function)
    insertion_sorted = sorting.insertionSort([x for x in problem], f)
    merge_sorted = sorting.mergeSort([x for x in problem], f)
    quick_sorted = sorting.quickSort([x for x in problem], f, 0, len(problem)-1)
    print("insertion sorted: %s" % insertion_sorted)
    print("merge sorted: %s" % merge_sorted)
               

if __name__ == "__main__":
    main()
