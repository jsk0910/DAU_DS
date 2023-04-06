from sort_.mergeSort import *

def main():
    print("Mergesort test")
    A = [3, 8, 2, 24, 8, 1, 12,1, 0, 55, 0, 256, 333, 23, 65]
    print("A[]:       ", A)
    mergeSort(A, 0, len(A)-1)
    print("Sorted A[]:", A)

if __name__ == "__main__":
    main()