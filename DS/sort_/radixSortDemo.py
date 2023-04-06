from sort_.radixSort import *

def main():
    print("Quicksort test")
    A = [3, 8, 2, 4, 8, 77, 1, 2, 0, 5, 56, 28]
    print("A[]:       ", A)
    radixSort(A)
    print("Sorted A[]:", A)

if __name__ == "__main__":
    main()
