from sort.heapSort import *

def main():
    print("Heapsort!")
    A = [3, 8, 2, 4, 8, 1, 2, 0, 5, 9]
    print("A[]:       ", A)
    heapSort(A)
    print("Sorted A[]:", A)

if __name__ == "__main__":
    main()
