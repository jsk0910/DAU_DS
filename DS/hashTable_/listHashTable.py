# 책에는 포함되지 않음
class ListHashTable:
    def __init__(self, n:int):
        self.__table = [[] for i in range(n)]
        self.__numItems = 0

    def __hash(self, x:int):
        return x % len(self.__table)

    def insert(self, x):
        slot = self.__hash(x)
        self.__table[slot].insert(0, x)
        self.__numItems += 1

    def search(self, x):
        slot = self.__hash(x)
        if len(self.__table[slot]) == 0:
            return None # null list
        else:
            i = self.__table[slot].index(x)
            if i < 0:
                return None # not exist
            else:
                return (self.__table[slot], i)

    def delete(self, x):
        if self.isEmpty():
            """ 에러 처리 """
        else:
            slot = self.__hash(x)
            self.__table[slot].remove(x)
            self.__numItems -= 1

    def isEmpty(self) -> bool:
        return self.__numItems == 0

    def clear(self):
        self.__table = [[] for i in range(len(self.__table))]
        self.__numItems = 0

    def printAll(self):
        for i in range(len(self.__table)):
            print("Slot ", i, " : ", end=" ")
            if len(self.__table[i]) == 0:
                print("Empty")
            else:
                for j in range(len(self.__table[i])):
                    print(self.__table[i][j], end=" ")
                print()

print("List Hash Table Demo!")
h = ListHashTable(11)
h.insert(10)
h.insert(21)
#h.delete(20)   # 아무 영향 없어야 함
h.insert(20)
h.insert(5)
h.insert(80)
h.insert(32)
h.printAll()

h.delete(20)
h.delete(80)

# Just for checking purpose
item = 21
(i, j) = h.search(item)
if i == None:
    print("Search Failed!")
else:
    print("Search:", item, "List:", i, ", item index", j)