from sort.bucketSort import *

def main():
    A = [0.35, .24, .16, .21, .4, .72, .23, .9, .23, .14, .58, .12, 0]
    print("A[]:       ", A)
    bucketSort(A)
    print("Sorted A[]:", A)

if __name__ == "__main__":
    main()
