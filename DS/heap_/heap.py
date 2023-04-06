class Heap:
	def __init__(self, *args):
		if len(args) != 0:
			self.__A = args[0] # 파라미터로 온 리스트
		else:
			self.__A = []
 
	# [알고리즘 8-2] 구현: 힙에 원소 삽입하기(재귀 알고리즘 버전)
	def insert(self, x):
		self.__A.append(x)
		self.__percolateUp(len(self.__A)-1)

	# 스며오르기
	def __percolateUp(self, i:int):
		parent = (i - 1) // 2
		if i > 0 and self.__A[i] > self.__A[parent]:
			self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
			self.__percolateUp(parent)

	# [알고리즘 8-2] 구현: 힙에서 원소 삭제하기
	def deleteMax(self):
		# heap is in self.__A[0...len(self.__A)-1]
		if (not self.isEmpty()):
			max = self.__A[0]
			self.__A[0] = self.__A.pop() # *.pop(): 리스트의 끝원소 삭제 후 원소 리턴
			self.__percolateDown(0)
			return max
		else:
			return None

	# 스며내리기
	def __percolateDown(self, i:int):
		# Percolate down w/ self.__A[i] as the root
		child = 2 * i + 1  # left child
		right = 2 * i + 2  # right child
		if (child <= len(self.__A)-1):
			if (right <= len(self.__A)-1 and self.__A[child] < self.__A[right]):
				child = right  # index of larger child
			if self.__A[i] < self.__A[child]:
				self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
				self.__percolateDown(child)

	def max(self):
		return self.__A[0]

	# 힙 만들기
	def buildHeap(self):
		for i in range((len(self.__A) - 2) // 2, -1, -1):
			self.__percolateDown(i)

	# 힙이 비었는지 확인하기
	def isEmpty(self) -> bool:
		return len(self.__A) == 0

	def clear(self):
		self.__A = []

	def size(self) -> int:
		return len(self.__A)

# 코드 8-8