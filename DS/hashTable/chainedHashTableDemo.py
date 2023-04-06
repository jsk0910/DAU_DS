from hashTable.chainedHashTable import *
from list.circularLinkedList import *
from list.listNode import *

h = ChainedHashTable(7)
h.insert(10)
h.insert(21)
h.delete(20) # 아무 영향 없어야 함
h.insert(20)
h.insert(5)
h.insert(12)
h.insert(19)
h.insert(80)
h.insert(32)
h.delete(20)
h.delete(44)

item = 21
slot = h.search(item)
if slot == None:
	print("Search Failed for", item)
else:
	print("Search for", item, "successful at slot", slot)

# 코드 12-2