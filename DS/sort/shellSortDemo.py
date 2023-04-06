from sort.shellSort import *

def main():
    print("shellSort test")
    A = [3, 8, 2, 24, 8, 1, 12,1, 0, 55, 23, 44, 3, 57, 256, 11, 9, 3, 4, 5, 6, 36, 912, 23, 4, 2, 55, 0, 256, 333, 23, 65]
    print("A[]:       ", A)
    shellSort(A)
    print("Sorted A[]:", A)

if __name__ == "__main__":
    main()