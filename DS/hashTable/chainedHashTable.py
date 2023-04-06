from list.circularLinkedList import *
from list.listNode import *

class ChainedHashTable:
	def __init__(self, n):
		self.__table = [CircularLinkedList() for i in range(n)]
		self.__numItems = 0;

	def __hash(self, x:int): # 편의상 int 타입으로 제한
		return x % len(self.__table)

	# [알고리즘 12-1] 구현: 검색, 삽입, 삭제
	def insert(self, x:int):
		slot = self.__hash(x)
		self.__table[slot].insert(0, x)
		self.__numItems += 1

	def search(self, x:int) -> ListNode:
		slot = self.__hash(x)
		if self.__table[slot].isEmpty():
			return None # null list
		else:
			head = prev = self.__table[slot].getNode(-1)  # 더미 헤드
			curr = prev.next  # 0번 노드
			while curr != head:
				if curr.item == x:
					return curr
				else:
					prev = curr; curr = curr.next
			return None
	def delete(self, x:int):
		slot = self.__hash(x)
		success = self.__table[slot].remove(x)
		if success != None:
			self.__numItems -= 1
 	# 기타
	def isEmpty(self):
		return self.__numItems == 0

	def clear(self):
		for i in range(len(self.__table)):
			self.__table[i] = CircularLinkedList()
		self.__numItems = 0

# 코드 12-1