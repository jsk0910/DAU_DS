def bubbleSort(A):
	for numElements in range(len(A), 0, -1):
		for i in range(numElements-1):
			if A[i] > A[i+1]:
				A[i], A[i+1] = A[i+1], A[i]