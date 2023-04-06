from list.linkedListBasic import *

list = LinkedListBasic()
list.append(30); list.insert(0, 20)
a = LinkedListBasic()
a.append(4); a.append(3); a.append(3); a.append(2); a.append(1)
list.extend(a)
list.reverse()
list.pop(0)
print("count(3):", list.count(3))
print("get(2):", list.get(2))
list.printList()

# 코드 5-16